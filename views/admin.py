# ==========================================================
# SITAPEL PDPB 2026
# views/admin.py
# DASHBOARD ADMIN
# KOMISI PEMILIHAN UMUM KOTA BENGKULU
# ==========================================================

import streamlit as st

from providers.sheets import (
    read_dict,
    update_status_permohonan
)

from auth.admin_auth import (
    is_admin_logged_in,
    logout_admin,
)


# ==========================================================
# DASHBOARD ADMIN
# ==========================================================

def show_admin():

    # ======================================================
    # PROTEKSI LOGIN
    # ======================================================

    if not is_admin_logged_in():

        st.warning(
            "Silakan login sebagai Admin terlebih dahulu."
        )

        if st.button(
            "Login Admin",
            type="primary",
            use_container_width=True
        ):

            st.session_state.page = "login_admin"

            st.rerun()

        return

    # ======================================================
    # LOAD DATA
    # ======================================================

    try:

        data = read_dict()

    except Exception as e:

        st.error(
            f"Gagal membaca data Google Sheets.\n\n{e}"
        )

        return

    # ======================================================
    # HITUNG STATISTIK
    # ======================================================

    total_permohonan = len(data)

    menunggu = sum(
        1
        for item in data
        if item.get(
            "Status",
            ""
        ) == "Menunggu"
    )

    diproses = sum(
        1
        for item in data
        if item.get(
            "Status",
            ""
        ) == "Diproses"
    )

    selesai = sum(
        1
        for item in data
        if item.get(
            "Status",
            ""
        ) == "Selesai"
    )

    ditolak = sum(
        1
        for item in data
        if item.get(
            "Status",
            ""
        ) == "Ditolak"
    )

    # ======================================================
    # HEADER
    # ======================================================

    st.title(
        "Dashboard Admin SITAPEL"
    )

    st.caption(
        "Komisi Pemilihan Umum Kota Bengkulu"
    )

    st.divider()

    # ======================================================
    # MENU
    # ======================================================

    menu = st.radio(

        "",

        [

            "📊 Dashboard",

            "📋 Data Permohonan",

            "🚪 Logout"

        ],

        horizontal=True,

        label_visibility="collapsed"

    )

    # ======================================================
    # LOGOUT
    # ======================================================

    if menu == "🚪 Logout":

        logout_admin()

        return

    # ======================================================
    # DASHBOARD
    # ======================================================

    if menu == "📊 Dashboard":

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:

            st.metric(
                "Total",
                total_permohonan
            )

        with col2:

            st.metric(
                "Menunggu",
                menunggu
            )

        with col3:

            st.metric(
                "Diproses",
                diproses
            )

        with col4:

            st.metric(
                "Selesai",
                selesai
            )

        with col5:

            st.metric(
                "Ditolak",
                ditolak
            )

        st.divider()

        st.subheader(
            "Statistik Permohonan"
        )

        st.info(
            """
Dashboard statistik sudah aktif.

Pada Bagian 2 akan ditambahkan:

• Pencarian

• Filter Status

• Tabel Data Permohonan

• Tombol Detail
"""
        )

    # ======================================================
    # DATA PERMOHONAN
    # ======================================================

    elif menu == "📋 Data Permohonan":

        st.subheader(
            "Data Permohonan"
        )

        st.write("")

        # ==================================================
        # FILTER
        # ==================================================

        col1, col2, col3 = st.columns(
            [2, 2, 1]
        )

        with col1:

            cari = st.text_input(
                "Cari Nomor / Nama",
                placeholder="Masukkan nomor permohonan atau nama..."
            )

        with col2:

            status_filter = st.selectbox(
                "Filter Status",
                [
                    "Semua",
                    "Menunggu",
                    "Diproses",
                    "Selesai",
                    "Ditolak"
                ]
            )

        with col3:

            st.write("")

            st.write("")

            refresh = st.button(
                "🔄 Refresh",
                use_container_width=True
            )

        # ==================================================
        # FILTER DATA
        # ==================================================

        filtered_data = []

        for item in data:

            nomor = item.get(
                "Nomor Permohonan",
                ""
            )

            nama = item.get(
                "Nama Pemohon",
                ""
            )

            status = item.get(
                "Status",
                ""
            )

            if cari:

                keyword = cari.lower()

                if (
                    keyword not in nomor.lower()
                    and
                    keyword not in nama.lower()
                ):

                    continue

            if status_filter != "Semua":

                if status != status_filter:

                    continue

            filtered_data.append(item)

        st.write("")

        st.success(
            f"Total data : {len(filtered_data)} permohonan"
        )

        st.divider()

        # ==================================================
        # TABEL DATA
        # ==================================================

        if not filtered_data:

            st.info(
                "Tidak ada data yang ditemukan."
            )

        else:

            for index, item in enumerate(
                filtered_data,
                start=1
            ):

                with st.container(border=True):

                    col1, col2, col3 = st.columns(
                        [5, 2, 1]
                    )

                    with col1:

                        st.markdown(
                            f"""
**{index}. {item.get("Nama Pemohon","")}**

Nomor : {item.get("Nomor Permohonan","")}

Layanan : {item.get("Jenis Layanan","")}
"""
                        )

                    with col2:

                        st.write("")

                        st.write(
                            f"**{item.get('Status','')}**"
                        )

                    with col3:

                        if st.button(
                            "Lihat Detail",
                            key=f"lihat_{index}",
                            use_container_width=True
                        ):

                            st.session_state.detail_permohonan = item

                            st.session_state.admin_menu = "detail"

                            st.rerun()

        # ==================================================
        # DETAIL PERMOHONAN
        # ==================================================

        detail = st.session_state.get(
            "detail_permohonan"
        )

        if detail:

            st.divider()

            st.subheader(
                "Detail Permohonan"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.text_input(
                    "Nomor Permohonan",
                    detail.get(
                        "Nomor Permohonan",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Nama Pemohon",
                    detail.get(
                        "Nama Pemohon",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "WhatsApp",
                    detail.get(
                        "WhatsApp",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Email",
                    detail.get(
                        "Email",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Jenis Layanan",
                    detail.get(
                        "Jenis Layanan",
                        ""
                    ),
                    disabled=True
                )

            with col2:

                st.text_input(
                    "Nama yang Diajukan",
                    detail.get(
                        "Nama Diajukan",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Kecamatan",
                    detail.get(
                        "Kecamatan",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Kelurahan",
                    detail.get(
                        "Kelurahan",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Status",
                    detail.get(
                        "Status",
                        ""
                    ),
                    disabled=True
                )

            st.text_area(
                "Keterangan Pemohon",
                detail.get(
                    "Keterangan Pemohon",
                    ""
                ),
                disabled=True,
                height=120
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.button(
                    "✔ Verifikasi",
                    disabled=True,
                    use_container_width=True
                )

            with col2:

                st.button(
                    "❌ Tolak",
                    disabled=True,
                    use_container_width=True
                )

            with col3:

                if st.button(
                    "Tutup",
                    use_container_width=True
                ):

                    del st.session_state.detail_permohonan

                    st.rerun()



