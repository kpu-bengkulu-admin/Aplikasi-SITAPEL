# ==========================================================
# SITAPEL v4
# pages/admin.py
#
# Admin OAuth Setup
#
# Login Google hanya dilakukan oleh Admin KPU sekali
# ==========================================================


import streamlit as st
from urllib.parse import urlparse, parse_qs


from auth.oauth import (
    get_authorization_url,
    exchange_code
)


from providers.storage import (
    get_oauth_token,
    delete_oauth_token
)



# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="Admin SITAPEL",
    page_icon="🔐",
    layout="centered"
)



# ==========================================================
# HEADER
# ==========================================================

st.title(
    "🔐 Admin SITAPEL v4"
)


st.write(
    """
    Halaman ini hanya digunakan oleh Admin KPU Kota Bengkulu
    untuk menghubungkan SITAPEL dengan akun Google resmi.

    Setelah OAuth aktif, masyarakat dapat menggunakan SITAPEL
    tanpa login Google.
    """
)


st.divider()



# ==========================================================
# STATUS TOKEN
# ==========================================================

token = get_oauth_token()


if token:

    st.success(
        "✅ OAuth Google sudah aktif"
    )


    st.info(
        """
        SITAPEL sudah terhubung dengan:

        ✔ Google Drive API
        ✔ Google Sheets API
        """
    )


    with st.expander(
        "Informasi OAuth"
    ):

        st.write(
            {
                "Client ID":
                    token.get("client_id"),

                "Scopes":
                    token.get("scopes")
            }
        )


    if st.button(
        "🗑 Hapus OAuth"
    ):

        delete_oauth_token()

        st.success(
            "Token OAuth berhasil dihapus."
        )

        st.rerun()



else:


    st.warning(
        "⚠ OAuth Admin belum aktif."
    )



    st.subheader(
        "Hubungkan Google KPU"
    )


    if "oauth_url" not in st.session_state:


        if st.button(
            "🔑 Login Google KPU"
        ):


            url, state, flow = get_authorization_url()


            st.session_state.oauth_url = url

            st.session_state.oauth_state = state

            st.session_state.oauth_flow = flow


    if "oauth_url" in st.session_state:


        st.markdown(
            f"""
            ### Langkah 1

            Klik link berikut:

            👉 [Login Google KPU]({st.session_state.oauth_url})


            Setelah login berhasil,
            Google akan mengarahkan kembali ke URL callback.
            Copy URL tersebut.
            """
        )



        st.divider()



        st.subheader(
            "Aktivasi OAuth"
        )


        callback_url = st.text_input(
            "Paste URL Callback Google"
        )


        if st.button(
            "Aktifkan OAuth"
        ):


            if not callback_url:

                st.error(
                    "URL callback belum dimasukkan."
                )


            else:

                try:

                    parsed = urlparse(
                        callback_url
                    )


                    params = parse_qs(
                        parsed.query
                    )


                    code = params.get(
                        "code"
                    )[0]


                    exchange_code(
                        st.session_state.oauth_flow,
                        code
                    )


                    st.success(
                        "🎉 OAuth Google berhasil diaktifkan!"
                    )


                    st.session_state.pop(
                        "oauth_url",
                        None
                    )


                    st.rerun()



                except Exception as e:


                    st.error(
                        f"Gagal OAuth: {e}"
                    )