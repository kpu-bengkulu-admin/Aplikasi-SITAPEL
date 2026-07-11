# ==========================================================
# SITAPEL v4
# auth/oauth.py
# ==========================================================

from google_auth_oauthlib.flow import Flow

from config import GOOGLE
from providers.storage import save_or_update_token


CLIENT_CONFIG = {
    "web": {
        "client_id": GOOGLE.client_id,
        "client_secret": GOOGLE.client_secret,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": [
            GOOGLE.redirect_uri
        ],
    }
}


def create_flow():

    return Flow.from_client_config(
        CLIENT_CONFIG,
        scopes=list(GOOGLE.scopes),
        redirect_uri=GOOGLE.redirect_uri
    )


def get_authorization_url():

    flow = create_flow()

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        prompt="consent",
        include_granted_scopes="false"
    )

    return (
        authorization_url,
        state,
        flow
    )



def exchange_code(flow, code):

    flow.fetch_token(
        code=code
    )

    credentials = flow.credentials


    token_data = {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": list(credentials.scopes),
    }


    save_or_update_token(
        token_data
    )


    return credentials