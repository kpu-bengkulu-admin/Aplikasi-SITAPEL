from pathlib import Path
import streamlit as st

from pages.dashboard import show_dashboard
from pages.permohonan import show_permohonan


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
# SESSION INIT
# ======================================================

DEFAULT_SESSION = {
    "page": "dashboard",
    "step": 1,
    "layanan": "",
}

for key, value in DEFAULT_SESSION.items():
    if key not in st.session_state:
        st.session_state[key] = value


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