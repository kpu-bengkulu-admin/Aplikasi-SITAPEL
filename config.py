# ==========================================================
# SITAPEL v4
#
# File        : config.py
# Status      : FINAL
# Version     : 4.0.0
#
# Python      : 3.14+
# Streamlit   : 1.58+
#
# Description :
# Central Configuration
#
# ==========================================================

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import streamlit as st
APP_NAME: Final = "SITAPEL PDPB 2026"

# ==========================================================
# GOOGLE
# ==========================================================

@dataclass(frozen=True, slots=True)
class GoogleConfig:

    client_id: str

    client_secret: str

    redirect_uri: str

    scopes: tuple[str, ...]


# ==========================================================
# CRYPTO
# ==========================================================

@dataclass(frozen=True, slots=True)
class CryptoConfig:
    """
    Encryption Configuration.
    """

    fernet_key: str


# ==========================================================
# GOOGLE DRIVE
# ==========================================================

@dataclass(frozen=True, slots=True)
class DriveConfig:
    """
    Google Drive Configuration.
    """

    folder_id: str


# ==========================================================
# GOOGLE SHEETS
# ==========================================================

@dataclass(frozen=True, slots=True)
class SheetsConfig:
    """
    Google Sheets Configuration.
    """

    spreadsheet_id: str
    sheet_name: str


# ==========================================================
# STREAMLIT
# ==========================================================

@dataclass(frozen=True, slots=True)
class StreamlitConfig:
    """
    Streamlit Application Configuration.
    """

    page_title: str = "SITAPEL PDPB 2026"

    page_icon: str = "🗳️"

    layout: str = "wide"

    initial_sidebar_state: str = "expanded"


# ==========================================================
# GOOGLE SCOPES
# ==========================================================

GOOGLE_SCOPES: Final[tuple[str, ...]] = (

    "openid",

    "email",

    "profile",

    "https://www.googleapis.com/auth/drive.file",

    "https://www.googleapis.com/auth/spreadsheets",

)


# ==========================================================
# LOAD GOOGLE
# ==========================================================

GOOGLE: Final = GoogleConfig(

    client_id=st.secrets["google"]["client_id"],

    client_secret=st.secrets["google"]["client_secret"],

    redirect_uri=st.secrets["google"]["redirect_uri"],

    scopes=tuple(st.secrets["google"]["scopes"]),

)


# ==========================================================
# LOAD CRYPTO
# ==========================================================

CRYPTO: Final = CryptoConfig(

    fernet_key=st.secrets["crypto"]["fernet_key"],

)


# ==========================================================
# LOAD GOOGLE DRIVE
# ==========================================================

DRIVE: Final = DriveConfig(

    folder_id=st.secrets["drive"]["folder_id"],

)


# ==========================================================
# LOAD GOOGLE SHEETS
# ==========================================================

SHEETS: Final = SheetsConfig(

    spreadsheet_id=st.secrets["sheets"]["spreadsheet_id"],

    sheet_name=st.secrets["sheets"]["sheet_name"],

)


# ==========================================================
# LOAD STREAMLIT
# ==========================================================

STREAMLIT: Final = StreamlitConfig()


# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "APP_NAME",

    "GOOGLE",

    "CRYPTO",

    "DRIVE",

    "SHEETS",

    "STREAMLIT",

    "GOOGLE_SCOPES",

]