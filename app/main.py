from fastapi import FastAPI, HTTPException, Body
import os, time

app = FastAPI(title="CapitalConductor API (Override)")

@app.get("/health")
def health():
    return {"ok": True, "service": "cc-api", "ts": int(time.time())}

@app.post("/deck/unlock")
def unlock(payload: dict = Body(...)):
    if payload.get("password") != os.getenv("LIVE_DECK_PASSWORD", "Conductor2025"):
        raise HTTPException(401, "Invalid password")
    return {"ok": True}

@app.post("/analytics/track")
def track(event: dict = Body(...)):
    return {"ok": True, "received": event}
