# ==========================================================
# SITAPEL v4
# providers/storage.py
#
# OAuth Token Storage
# ==========================================================

import json
import os


TOKEN_FILE = "oauth_token.json"


def save_or_update_token(token_data):
    """
    Menyimpan refresh token OAuth admin
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
    """

    if not os.path.exists(TOKEN_FILE):
        return None

    with open(
        TOKEN_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)



def delete_oauth_token():

    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)



def has_oauth_token():

    return os.path.exists(TOKEN_FILE)