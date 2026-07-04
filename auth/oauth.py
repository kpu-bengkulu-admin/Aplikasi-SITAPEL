import streamlit as st
from google_auth_oauthlib.flow import Flow

SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile"
]

CLIENT_CONFIG = {
    "web": {
        "client_id": st.secrets["GOOGLE_CLIENT_ID"],
        "client_secret": st.secrets["GOOGLE_CLIENT_SECRET"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": [
            "https://aplikasi-sitapel-kpu-kota-bengkulu.streamlit.app/"
        ]
    }
}


def get_flow():
    return Flow.from_client_config(
        CLIENT_CONFIG,
        scopes=SCOPES,
        redirect_uri=CLIENT_CONFIG["web"]["redirect_uris"][0]
    )


def get_authorization_url():

    client_id = st.secrets["GOOGLE_CLIENT_ID"]

    redirect_uri = "https://aplikasi-sitapel-kpu-kota-bengkulu.streamlit.app/"

    scope = "https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"

    auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        f"?response_type=code"
        f"&client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&scope={scope}"
        f"&access_type=offline"
        f"&prompt=consent%20select_account"
        f"&include_granted_scopes=false"
    )

    return auth_url


def fetch_token_from_request(request_url):
    flow = get_flow()
    flow.fetch_token(authorization_response=request_url)
    return flow.credentials