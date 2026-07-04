# ==========================================================
# SITAPEL v3
# services/sheets.py
# Google Sheets Database Layer (FINAL)
# ==========================================================

from datetime import datetime

import gspread
import streamlit as st
from google.oauth2.service_account import Credentials


# ==========================================================
# CONFIG
# ==========================================================

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

SPREADSHEET_NAME = "SITAPEL_DB"
WORKSHEET_NAME = "permohonan"


# ==========================================================
# CLIENT
# ==========================================================

def get_client():

    credentials = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=SCOPES
    )

    return gspread.authorize(credentials)


# ==========================================================
# WORKSHEET
# ==========================================================

def get_worksheet():

    client = get_client()

    spreadsheet = client.open(
        SPREADSHEET_NAME
    )

    return spreadsheet.worksheet(
        WORKSHEET_NAME
    )


# ==========================================================
# FORMAT ANGGOTA PINDAH
# ==========================================================

def format_anggota():

    anggota = st.session_state.get(
        "anggota_pindah",
        []
    )

    if not anggota:
        return ""

    hasil = []

    for i, item in enumerate(anggota, start=1):

        nama = item.get(
            "nama",
            ""
        ).strip()

        if nama:

            hasil.append(
                f"{i}. {nama}"
            )

    return "\n".join(hasil)


# ==========================================================
# FORMAT ALASAN
# ==========================================================

def format_alasan():

    alasan = st.session_state.get(
        "alasan",
        ""
    )

    if alasan == "Lainnya":

        return st.session_state.get(
            "alasan_lainnya",
            ""
        )

    return alasan


# ==========================================================
# SIMPAN DATA
# ==========================================================

def simpan_ke_sheets(
    nomor_permohonan,
    folder_link
):

    ws = get_worksheet()

    timestamp = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    row = [

        # ==================================================
        # A
        # ==================================================

        nomor_permohonan,

        # ==================================================
        # B
        # ==================================================

        timestamp,

        # ==================================================
        # C
        # ==================================================

        "Menunggu Verifikasi",

        # ==================================================
        # D
        # ==================================================

        st.session_state.get(
            "layanan",
            ""
        ),

        # ==================================================
        # E
        # ==================================================

        st.session_state.get(
            "nama_pemohon",
            ""
        ),

        # ==================================================
        # F
        # ==================================================

        st.session_state.get(
            "email",
            ""
        ),

        # ==================================================
        # G
        # ==================================================

        st.session_state.get(
            "whatsapp",
            ""
        ),

        # ==================================================
        # H
        # ==================================================

        st.session_state.get(
            "kabupaten",
            ""
        ),

        # ==================================================
        # I
        # ==================================================

        st.session_state.get(
            "kecamatan",
            ""
        ),

        # ==================================================
        # J
        # ==================================================

        st.session_state.get(
            "kelurahan",
            ""
        ),

        # ==================================================
        # K
        # ==================================================

        st.session_state.get(
            "alamat_baru",
            ""
        ),

        # ==================================================
        # L
        # ==================================================

        st.session_state.get(
            "nama_diajukan",
            ""
        ),

        # ==================================================
        # M
        # ==================================================

        st.session_state.get(
            "kategori_tms",
            ""
        ),

        # ==================================================
        # N
        # ==================================================

        st.session_state.get(
            "sudah_ktp",
            ""
        ),

        # ==================================================
        # O
        # ==================================================

        format_alasan(),

        # ==================================================
        # P
        # ==================================================

        format_anggota(),

        # ==================================================
        # Q
        # ==================================================

        folder_link,

        # ==================================================
        # R
        # ==================================================

        ""

    ]

    ws.append_row(
        row,
        value_input_option="USER_ENTERED"
    )

    return True