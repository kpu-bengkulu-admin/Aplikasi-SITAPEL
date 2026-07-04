# ==========================================================
# SITAPEL v3
# auth/token.py
# OAuth Token Handler
# ==========================================================

import streamlit as st
from auth.oauth import get_flow


def fetch_token_from_code(code: str):

    flow = get_flow()

    flow.fetch_token(code=code)

    credentials = flow.credentials

    st.session_state["google_credentials"] = credentials

    return credentials


def is_logged_in():

    return "google_credentials" in st.session_state


def logout():

    if "google_credentials" in st.session_state:
        del st.session_state["google_credentials"]