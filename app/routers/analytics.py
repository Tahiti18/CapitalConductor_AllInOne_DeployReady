from fastapi import APIRouter, Body
import os, json, time

router = APIRouter()

# Optional deps, loaded lazily to keep container light if not configured
def _post_ghl(url, payload):
    import httpx
    with httpx.Client(timeout=10) as c:
        r = c.post(url, json=payload)
        r.raise_for_status()

def _append_sheet(sheet_id, sa_path, row):
    import gspread
    from google.oauth2.service_account import Credentials
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(sa_path, scopes=scopes)
    gc = gspread.authorize(creds)
    sh = gc.open_by_key(sheet_id)
    ws = sh.sheet1
    ws.append_row(row, value_input_option="RAW")

@router.post("/track")
def track(event: dict = Body(...)):
    # event: {type, id, email, ts, ...}
    ok = True
    errors = []
    # Google Sheets logging
    sheet_id = os.getenv("SHEET_ID","")
    sa_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON","")
    if sheet_id and sa_path and os.path.exists(sa_path):
        try:
            _append_sheet(sheet_id, sa_path, [
                event.get("type",""), event.get("id",""), event.get("email",""),
                int(event.get("ts", time.time()*1000)),
                json.dumps(event)
            ])
        except Exception as e:
            errors.append(f"sheets:{e}")
    # GoHighLevel Incoming Webhook
    ghl_url = os.getenv("GHL_INCOMING_WEBHOOK_URL","")
    if ghl_url:
        try:
            _post_ghl(ghl_url, event)
        except Exception as e:
            errors.append(f"ghl:{e}")

    return {"ok": ok, "errors": errors}
