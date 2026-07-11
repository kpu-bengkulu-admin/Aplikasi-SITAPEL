# ==========================================================
# SITAPEL PDPB 2026
# views/login_admin.py
# LOGIN ADMIN
# KOMISI PEMILIHAN UMUM KOTA BENGKULU
# ==========================================================

import streamlit as st

from auth.admin_auth import (
    login_admin,
    set_admin_login
)


# ==========================================================
# HALAMAN LOGIN ADMIN
# ==========================================================

def show_login_admin():

    st.markdown(
        """
        <h2 style="text-align:center;">
            Login Admin SITAPEL
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown(
            '<div class="form-box">',
            unsafe_allow_html=True
        )

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        st.write("")

        col_back, col_login = st.columns(2)

        with col_back:

            if st.button(
                "⬅ Kembali",
                use_container_width=True
            ):

                st.session_state.page = "dashboard"

                st.rerun()

        with col_login:

            if st.button(
                "Login",
                type="primary",
                use_container_width=True
            ):

                if username.strip() == "":

                    st.error(
                        "Username wajib diisi."
                    )

                elif password.strip() == "":

                    st.error(
                        "Password wajib diisi."
                    )

                elif login_admin(
                    username,
                    password
                ):

                    set_admin_login()

                    st.session_state.page = "admin"

                    st.rerun()

                else:

                    st.error(
                        "Username atau Password salah."
                    )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )