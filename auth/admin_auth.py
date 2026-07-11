# ==========================================================
# SITAPEL PDPB 2026
# auth/admin_auth.py
# AUTHENTIKASI ADMIN
# KOMISI PEMILIHAN UMUM KOTA BENGKULU
# ==========================================================

import bcrypt
import streamlit as st


# ==========================================================
# LOGIN
# ==========================================================

def login_admin(
    username: str,
    password: str
) -> bool:
    """
    Validasi login admin menggunakan
    username dan password hash
    yang disimpan di st.secrets.
    """

    admin_username = st.secrets["ADMIN"]["username"]
    admin_password_hash = st.secrets["ADMIN"]["password_hash"]

    if username != admin_username:
        return False

    return bcrypt.checkpw(
        password.encode("utf-8"),
        admin_password_hash.encode("utf-8")
    )


# ==========================================================
# STATUS LOGIN
# ==========================================================

def is_admin_logged_in() -> bool:
    """
    Mengecek apakah admin
    sudah login.
    """

    return st.session_state.get(
        "admin_login",
        False
    )


# ==========================================================
# SIMPAN SESSION LOGIN
# ==========================================================

def set_admin_login():

    st.session_state.admin_login = True


# ==========================================================
# LOGOUT
# ==========================================================

def logout_admin():

    st.session_state.admin_login = False

    st.session_state.page = "dashboard"

    st.rerun()