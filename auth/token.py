# ==========================================================
# auth/token.py
# OAuth Refresh Token Manager
# ==========================================================

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import streamlit as st

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]


def get_credentials():
    """
    Menghasilkan credentials Google yang selalu valid.
    Access token akan diperbarui otomatis menggunakan refresh token.
    """

    creds = Credentials(
        token=None,
        refresh_token=st.secrets["GOOGLE_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=st.secrets["GOOGLE_CLIENT_ID"],
        client_secret=st.secrets["GOOGLE_CLIENT_SECRET"],
        scopes=SCOPES,
    )

    # Minta access token baru
    creds.refresh(Request())

    return creds