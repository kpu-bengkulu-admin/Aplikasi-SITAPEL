from pathlib import Path
import streamlit as st

from pages.dashboard import show_dashboard
from pages.permohonan import show_permohonan

from auth.token import is_logged_in
from auth.oauth import get_authorization_url, fetch_token_from_request


# ======================================================
# CONFIG
# ======================================================
st.set_page_config(
    page_title="SITAPEL | KPU Kota Bengkulu",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ======================================================
# OAUTH CALLBACK (PRODUCTION SAFE)
# ======================================================

if "code" in st.query_params:
    st.session_state["oauth_code"] = st.query_params["code"]

code = st.session_state.get("oauth_code")

if code and not st.session_state.get("oauth_done"):
    st.session_state["oauth_done"] = True

    try:
        token = fetch_token_from_request(st.query_params)

        st.session_state["logged_in"] = True
        st.session_state["token_data"] = token

    except Exception as e:
        st.error(f"OAuth error: {e}")


# ======================================================
# SESSION INIT
# ======================================================

if "page" not in st.session_state:
    st.session_state.page = "dashboard"


# ======================================================
# LOGIN GUARD
# ======================================================

if not is_logged_in():

    st.title("SITAPEL - Login Admin")

    auth_url = get_authorization_url()

    st.markdown(f"""
        <a href="{auth_url}" target="_self">
            🔐 Login dengan Google
        </a>
    """, unsafe_allow_html=True)

    st.stop()


# ======================================================
# ROUTER
# ======================================================

if st.session_state.page == "dashboard":
    show_dashboard()

elif st.session_state.page == "permohonan":
    show_permohonan()


# ======================================================
# FOOTER
# ======================================================

st.divider()

st.markdown("""
<center>
<h3>🗳️ SITAPEL</h3>
Sistem Informasi Pelayanan Pemutakhiran Data Pemilih
<br>
© 2026 KPU Kota Bengkulu
</center>
""", unsafe_allow_html=True)