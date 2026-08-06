raise Exception("CREDENTIALS.PY SEDANG DIPAKAI")

# ==========================================================
# SITAPEL v4
# auth/credentials.py
#
# Google API Credentials
# ==========================================================

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from config import GOOGLE
from providers.storage import get_oauth_token


def get_google_credentials():

    token_data = get_oauth_token()

    print("=" * 60)
    print("TOKEN DATA:", token_data)
    print("TOKEN KEYS:", list(token_data.keys()) if token_data else None)
    print("HAS REFRESH TOKEN:", bool(token_data.get("refresh_token")) if token_data else None)
    print("HAS TOKEN URI:", bool(token_data.get("token_uri")) if token_data else None)
    print("CLIENT ID:", GOOGLE.client_id)
    print("CLIENT SECRET:", bool(GOOGLE.client_secret))
    print("=" * 60)

    if not token_data:
        raise Exception(
            "oauth_token.json belum ditemukan."
        )

    print("TOKEN DATA:", token_data.keys())
    print("CLIENT ID:", GOOGLE.client_id)
    print("CLIENT SECRET ADA:", bool(GOOGLE.client_secret))

    credentials = Credentials(
        token=token_data.get("token"),
        refresh_token=token_data.get("refresh_token"),
        token_uri=token_data.get(
            "token_uri",
            "https://oauth2.googleapis.com/token"
        ),
        client_id=GOOGLE.client_id,
        client_secret=GOOGLE.client_secret,
        scopes=list(GOOGLE.scopes),
    )

    if not credentials.valid:
        credentials.refresh(Request())

    return credentials