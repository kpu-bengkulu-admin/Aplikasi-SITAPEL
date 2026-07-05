# ==========================================================
# SITAPEL v3
# services/sheets.py
# Google Sheets API (OAuth Refresh Token)
# ==========================================================

import streamlit as st

from googleapiclient.discovery import build

from auth.token import get_credentials


SHEET_ID = st.secrets["SHEET_ID"]
SHEET_NAME = st.secrets["SHEET_NAME"]


# ==========================================================
# GET SERVICE
# ==========================================================

def get_sheets_service():

    return build(
        "sheets",
        "v4",
        credentials=get_credentials()
    )


# ==========================================================
# SIMPAN KE GOOGLE SHEETS
# ==========================================================

def simpan_ke_sheets(
    nomor_permohonan,
    folder_link
):

    service = get_sheets_service()

    values = [[

        nomor_permohonan,

        st.session_state.layanan,

        st.session_state.nama_pemohon,

        st.session_state.whatsapp,

        st.session_state.email,

        st.session_state.nama_diajukan,

        folder_link,

        "Menunggu Verifikasi"

    ]]

    body = {
        "values": values
    }

    service.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range=f"{SHEET_NAME}!A:H",
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()