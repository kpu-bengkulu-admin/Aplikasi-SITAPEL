# ==========================================================
# SITAPEL PDPB 2026
# app.py
# CONTROLLER UTAMA
# KOMISI PEMILIHAN UMUM KOTA BENGKULU
# ==========================================================

import os
import streamlit as st

from config import APP_NAME


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title=APP_NAME,

    page_icon="assets/logo_kpu.png",

    layout="wide",

    initial_sidebar_state="collapsed"

)

# ==========================================================
# LOAD CSS
# ==========================================================

CSS_FILE = "assets/style.css"

if os.path.exists(CSS_FILE):

    with open(CSS_FILE, encoding="utf-8") as css:

        st.markdown(

            f"<style>{css.read()}</style>",

            unsafe_allow_html=True

        )

# ==========================================================
# IMPORT HALAMAN
# ==========================================================

from views.dashboard import show_dashboard
from views.permohonan import show_permohonan
from views.success import show_success
from views.cek_status import show_cek_status

from views.login_admin import show_login_admin
from views.admin import show_admin


# ==========================================================
# INIT SESSION
# ==========================================================

DEFAULT_SESSION = {

    "page": "dashboard",

    "admin_login": False,

    "admin_nama": "",

    "step": 1,

    "jenis_layanan": "",

    "nomor_permohonan": "",

    "status_permohonan": "",

    "waktu_submit": "",

    "nama_pemohon": "",

    "whatsapp": "",

    "email": "",

    "nama_diajukan": "",

    "anggota_keluarga": "",

    "kecamatan": "",

    "kelurahan": "",

    "alamat_baru": "",

    "kategori_tms": "",

    "sudah_ktpel": "",

    "keterangan_pemohon": "",

    "detail_permohonan": None,

    "tolak_permohonan": False,

}

for key, value in DEFAULT_SESSION.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ==========================================================
# JUDUL APLIKASI (HIDDEN)
# ==========================================================

st.markdown(

    """
    <style>

    #MainMenu {

        visibility:hidden;

    }

    footer {

        visibility:hidden;

    }

    header {

        visibility:hidden;

    }

    </style>
    """,

    unsafe_allow_html=True

)

# ==========================================================
# ROUTER APLIKASI
# ==========================================================

page = st.session_state.get(
    "page",
    "dashboard"
)

# ==========================================================
# HALAMAN PUBLIK
# ==========================================================

if page == "dashboard":

    show_dashboard()

elif page == "permohonan":

    show_permohonan()

elif page == "success":

    show_success()

elif page == "cek_status":

    show_cek_status()


# ==========================================================
# LOGIN ADMIN
# ==========================================================

elif page == "login_admin":

    show_login_admin()

# ==========================================================
# HALAMAN ADMIN
# ==========================================================

elif page == "admin":

    show_admin()


# ==========================================================
# HALAMAN TIDAK DITEMUKAN
# ==========================================================

else:

    st.error(
        f"Halaman '{page}' tidak ditemukan."
    )

    if st.button(
        "Kembali ke Dashboard",
        use_container_width=True
    ):

        st.session_state.page = "dashboard"

        st.rerun()

