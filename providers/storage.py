# ==========================================================
# SITAPEL v4
# providers/storage.py
#
# OAuth Token Storage
# ==========================================================

import json
import os
import streamlit as st


TOKEN_FILE = "oauth_token.json"


def save_or_update_token(token_data):
    """
    Menyimpan refresh token OAuth admin
    Lokal saja
    """

    with open(
        TOKEN_FILE,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            token_data,
            f,
            indent=4
        )


def get_oauth_token():
    """
    Mengambil token OAuth admin

    Prioritas:
    1. File lokal oauth_token.json
    2. Streamlit Secrets Cloud
    """

    # ===============================
    # MODE LOCAL
    # ===============================

    if os.path.exists(TOKEN_FILE):

        with open(
            TOKEN_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)


    # ===============================
    # MODE STREAMLIT CLOUD
    # ===============================

    try:

        if "oauth_token" in st.secrets:

            return dict(
                st.secrets["oauth_token"]
            )

    except Exception:
        pass


    return None



def delete_oauth_token():

    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)



def has_oauth_token():

    if os.path.exists(TOKEN_FILE):
        return True


    try:
        return "oauth_token" in st.secrets

    except Exception:
        return False