import streamlit as st

from auth.oauth import get_authorization_url
from auth.token import is_logged_in


def show_admin():

    st.title("Admin SITAPEL")

    if is_logged_in():

        st.success("Google Drive sudah terhubung.")

    else:

        st.warning("Belum login.")

        st.link_button(
            "Login Google",
            get_authorization_url()
        )