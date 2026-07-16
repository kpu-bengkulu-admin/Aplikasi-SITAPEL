# ==========================================================
# SITAPEL v4
# auth/credentials.py
#
# Google API Credentials
# ==========================================================

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from providers.storage import get_oauth_token


def get_google_credentials():
    """
    Membuat credentials Google API
    menggunakan OAuth Desktop.
    """

    token_data = get_oauth_token()

    if not token_data:
        raise Exception(
            "oauth_token.json belum ditemukan."
        )

    credentials = Credentials(
        token=token_data.get("token"),
        refresh_token=token_data.get("refresh_token"),
        token_uri=token_data.get("token_uri"),
        client_id=GOOGLE.client_id,
        client_secret=GOOGLE.client_secret,
        scopes=list(GOOGLE.scopes),
    )

    # Refresh access token jika sudah kedaluwarsa
    if not credentials.valid:
        credentials.refresh(Request())

    return credentials