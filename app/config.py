import os

class Settings:
    LIVE_DECK_PASSWORD = os.getenv("LIVE_DECK_PASSWORD", "Conductor2025")
    # GoHighLevel Incoming Webhook (from your Workflow trigger)
    GHL_INCOMING_WEBHOOK_URL = os.getenv("GHL_INCOMING_WEBHOOK_URL", "")
    # Google Sheets
    SHEET_ID = os.getenv("SHEET_ID", "")
    GOOGLE_SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    # CORS origins
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

settings = Settings()
