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

        "Menu",

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

        col1, col2, col3, col4 = st.columns(4)

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
                "Selesai",
                selesai
            )

        with col4:

            st.metric(
                "Ditolak",
                ditolak
            )

        st.divider()

        st.subheader(
            "Ringkasan Status Permohonan"
        )

        persen_selesai = (
            round(
                (selesai / total_permohonan) * 100,
                1
            )
            if total_permohonan > 0
            else 0
        )

        persen_ditolak = (
            round(
                (ditolak / total_permohonan) * 100,
                1
            )
            if total_permohonan > 0
            else 0
        )

        col_a, col_b = st.columns(
            2
        )

        with col_a:

            st.progress(
                persen_selesai / 100,
                text=f"Permohonan Selesai ({persen_selesai}%)"
            )

        with col_b:

            st.progress(
                persen_ditolak / 100,
                text=f"Permohonan Ditolak ({persen_ditolak}%)"
            )

            st.info(
                f"""
**Informasi Dashboard**

• Total Permohonan : **{total_permohonan}**

• Menunggu : **{menunggu}**

• Selesai : **{selesai}**

• Ditolak : **{ditolak}**
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
### {index}. {item.get("Nama Pemohon","")}

**Nomor Permohonan**

{item.get("Nomor Permohonan","")}

**Jenis Layanan**

{item.get("Jenis Layanan","")}

**Tanggal**

{item.get("Tanggal","")}
"""
                        )

                    with col2:

                        st.write("")

                        status = item.get(
                            "Status",
                            ""
                        )

                        warna = {

                            "Menunggu": "🟡",

                            "Selesai": "🟢",

                            "Ditolak": "🔴"

                        }.get(
                            status,
                            "⚪"
                        )

                        st.markdown(
                            f"""
### {warna}

**{status}**
"""
                        )

                    with col3:

                        st.write("")

                        st.write("")

                        if st.button(
                            "👁 Lihat Detail",
                            key=f"detail_{index}",
                            use_container_width=True
                        ):

                            st.session_state.detail_permohonan = item

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

            # ==============================================
            # INFORMASI TAMBAHAN
            # ==============================================

            st.divider()

            st.subheader(
                "Informasi Permohonan"
            )

            col_info1, col_info2 = st.columns(2)

            with col_info1:

                st.text_input(
                    "Tanggal Pengajuan",
                    detail.get(
                        "Tanggal",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Jam Pengajuan",
                    detail.get(
                        "Jam",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Tahun",
                    detail.get(
                        "Tahun",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Bulan",
                    detail.get(
                        "Bulan",
                        ""
                    ),
                    disabled=True
                )

            with col_info2:

                st.text_input(
                    "Anggota Keluarga",
                    detail.get(
                        "Anggota Keluarga",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Kategori TMS",
                    detail.get(
                        "Kategori TMS",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Sudah Memiliki KTP-el",
                    detail.get(
                        "Sudah Memiliki KTP-el",
                        ""
                    ),
                    disabled=True
                )

                st.text_input(
                    "Tanggal Verifikasi",
                    detail.get(
                        "Tanggal Verifikasi",
                        ""
                    ),
                    disabled=True
                )

            st.text_area(
                "Alamat Baru",
                detail.get(
                    "Alamat Baru",
                    ""
                ),
                disabled=True,
                height=80
            )

            st.text_area(
                "Catatan Admin",
                detail.get(
                    "Catatan Admin",
                    ""
                ),
                disabled=True,
                height=100
            )

            # ==============================================
            # DOKUMEN PERMOHONAN
            # ==============================================

            st.divider()

            st.subheader(
                "Dokumen Permohonan"
            )

            if detail.get(
                "Link Folder Drive"
            ):

                st.link_button(
                    "📂 Buka Folder Dokumen",
                    detail.get(
                        "Link Folder Drive"
                    ),
                    use_container_width=True
                )

            st.divider()

            col1, col2, col3 = st.columns(3)

            with col1:

                if st.button(
                    "✔ Verifikasi & Selesaikan",
                    type="primary",
                    use_container_width=True
                ):

                    berhasil = update_status_permohonan(

                        detail.get(
                            "Nomor Permohonan",
                            ""
                        ),

                        "Selesai"

                    )

                    if berhasil:

                        st.success(
                            "Permohonan berhasil diverifikasi dan diselesaikan."
                        )

                        del st.session_state.detail_permohonan

                        st.rerun()

                    else:

                        st.error(
                            "Gagal memperbarui status."
                        )

            with col2:

                if st.button(
                    "❌ Tolak",
                    use_container_width=True
                ):

                    st.session_state.tolak_permohonan = True

            with col3:

                if st.button(
                    "Tutup",
                    use_container_width=True
                ):

                    del st.session_state.detail_permohonan

                    st.rerun()

            # ==============================================
            # FORM PENOLAKAN
            # ==============================================

            if st.session_state.tolak_permohonan:

                st.divider()

                st.warning(
                    "Permohonan akan ditolak."
                )

                catatan = st.text_area(
                    "Alasan Penolakan",
                    placeholder="Tuliskan alasan penolakan..."
                )

                col_batal, col_simpan = st.columns(2)

                with col_batal:

                    if st.button(
                        "Batal",
                        use_container_width=True
                    ):

                        st.session_state.tolak_permohonan = False

                        st.rerun()

                with col_simpan:

                    if st.button(
                        "Simpan Penolakan",
                        type="primary",
                        use_container_width=True
                    ):

                        if catatan.strip() == "":

                            st.error(
                                "Alasan penolakan wajib diisi."
                            )

                        else:

                            berhasil = update_status_permohonan(

                                detail.get(
                                    "Nomor Permohonan",
                                    ""
                                ),

                                "Ditolak",

                                catatan

                            )

                            if berhasil:

                                st.success(
                                    "Permohonan berhasil ditolak."
                                )

                                st.session_state.tolak_permohonan = False

                                del st.session_state.detail_permohonan

                                st.rerun()

                            else:

                                st.error(
                                    "Gagal memperbarui status."
                                )

