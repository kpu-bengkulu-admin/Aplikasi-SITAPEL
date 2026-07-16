# ==========================================================
# SITAPEL v4
# views/oauth_admin.py
# ==========================================================

import streamlit as st

from auth.oauth import (
    get_authorization_url,
    exchange_code,
)


def show_oauth_admin():

    st.title("Generate OAuth Token")

    st.info(
        "Digunakan satu kali apabila Refresh Token sudah tidak berlaku."
    )

    if "oauth_flow" not in st.session_state:

        url, state, flow = get_authorization_url()

        st.session_state.oauth_flow = flow

        st.markdown(
            f"""
Klik link berikut untuk login Google.

{url}
"""
        )

        st.stop()

    code = st.text_input(
        "Authorization Code"
    )

    if st.button(
        "Simpan Token",
        type="primary"
    ):

        try:

            exchange_code(
                st.session_state.oauth_flow,
                code,
            )

            st.success(
                "OAuth Token berhasil disimpan."
            )

        except Exception as e:

            st.error(e)