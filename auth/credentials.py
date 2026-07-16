# ==========================================================
# SITAPEL v4
# auth/credentials.py
#
# Google API Credentials
# OAuth Admin
# ==========================================================

from google.oauth2.credentials import Credentials

from config import GOOGLE

from providers.storage import get_oauth_token


def get_google_credentials():
    """
    Membuat credentials Google API
    menggunakan OAuth refresh token admin
    """

    token_data = get_oauth_token()

    if not token_data:
        raise Exception(
            "OAuth admin belum dikonfigurasi"
        )


    credentials = Credentials(
        token=token_data.get("token"),
        refresh_token=token_data.get("refresh_token"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=GOOGLE.client_id,
        client_secret=GOOGLE.client_secret,
        scopes=list(GOOGLE.scopes),
    )


    return credentials

