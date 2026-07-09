# ==========================================================
# SITAPEL PDPB 2026
# views/cek_status.py
# ==========================================================

import streamlit as st

from providers.sheets import find_by

# ==========================================================
# HALAMAN CEK STATUS
# ==========================================================

def show_cek_status():

    st.title("🔍 Cek Status Permohonan")

    st.caption(
        """
Pemutakhiran Data Pemilih Berkelanjutan (PDPB)

Komisi Pemilihan Umum Kota Bengkulu
"""
    )

    st.divider()

    # ======================================================
    # NOMOR PERMOHONAN
    # ======================================================

    nomor = st.text_input(
        "Nomor Permohonan",
        value=st.session_state.get("nomor_permohonan", ""),
        placeholder="Contoh : SITAPEL-2026-000001"
    )

    col1, col2 = st.columns(2)

    with col1:

        cari = st.button(
            "🔍 Cari",
            type="primary",
            use_container_width=True
        )

    with col2:

        if st.button(
            "🏠 Dashboard",
            use_container_width=True
        ):

            st.session_state.page = "dashboard"
            st.rerun()

    # ======================================================
    # PENCARIAN
    # ======================================================

    if cari:

        if nomor.strip() == "":

            st.warning(
                "Masukkan Nomor Permohonan terlebih dahulu."
            )

            st.stop()

        data = find_by(
            "Nomor Permohonan",
            nomor.strip()
        )

        if data is None:

            st.error(
                "Nomor Permohonan tidak ditemukan."
            )

            st.stop()

        # ==================================================
        # HASIL
        # ==================================================

        st.success("Data permohonan ditemukan.")

        st.divider()

        st.subheader("Informasi Permohonan")

        col1, col2 = st.columns(2)

        with col1:

            st.text_input(
                "Nomor Permohonan",
                value=data.get("Nomor Permohonan", "-"),
                disabled=True
            )

            st.text_input(
                "Status",
                value=data.get("Status", "-"),
                disabled=True
            )

            st.text_input(
                "Jenis Layanan",
                value=data.get("Jenis Layanan", "-"),
                disabled=True
            )

            st.text_input(
                "Nama Pemohon",
                value=data.get("Nama Pemohon", "-"),
                disabled=True
            )

            st.text_input(
                "Nomor WhatsApp",
                value=data.get("WhatsApp", "-"),
                disabled=True
            )

        with col2:

            st.text_input(
                "Nama Yang Diajukan",
                value=data.get("Nama Diajukan", "-"),
                disabled=True
            )

            st.text_input(
                "Tanggal Pengajuan",
                value=data.get("Tanggal", "-"),
                disabled=True
            )

            st.text_input(
                "Jam Pengajuan",
                value=data.get("Jam", "-"),
                disabled=True
            )

            st.text_input(
                "Tanggal Verifikasi",
                value=data.get("Tanggal Verifikasi", "-"),
                disabled=True
            )

            st.text_input(
                "Petugas Verifikator",
                value=data.get("Petugas Verifikator", "-"),
                disabled=True
            )

        st.divider()

        # ==================================================
        # CATATAN PETUGAS
        # ==================================================

        st.subheader("Catatan Petugas")

        catatan = data.get(
            "Catatan Petugas",
            ""
        )

        if catatan:

            st.info(catatan)

        else:

            st.info(
                "Belum ada catatan dari petugas verifikator."
            )

        st.divider()

        # ==================================================
        # STATUS
        # ==================================================

        status = data.get("Status", "")

        if status == "Menunggu Verifikasi":

            st.warning(
                """
Permohonan telah diterima dan sedang menunggu proses
verifikasi oleh petugas KPU Kota Bengkulu.
"""
            )

        elif status == "Sedang Diverifikasi":

            st.info(
                """
Permohonan sedang diperiksa oleh petugas verifikator.
"""
            )

        elif status == "Perlu Perbaikan":

            st.error(
                """
Permohonan memerlukan perbaikan dokumen.
Silakan membaca catatan petugas.
"""
            )

        elif status == "Selesai":

            st.success(
                """
Permohonan telah selesai diproses.
Terima kasih telah menggunakan SITAPEL.
"""
            )

        elif status == "Ditolak":

            st.error(
                """
Permohonan tidak dapat diproses.
Silakan membaca catatan petugas.
"""
            )

        st.divider()

        # ==================================================
        # LINK GOOGLE DRIVE
        # ==================================================

        folder = data.get(
            "Link Folder Drive",
            ""
        )

        if folder:

            st.link_button(
                "📂 Lihat Dokumen Permohonan",
                folder,
                use_container_width=True
            )

        st.write("")

        # ==================================================
        # TOMBOL
        # ==================================================

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🔄 Cek Nomor Lain",
                use_container_width=True
            ):

                st.rerun()

        with col2:

            if st.button(
                "🏠 Kembali ke Dashboard",
                use_container_width=True
            ):

                st.session_state.page = "dashboard"
                st.rerun()

    st.divider()

    st.caption(
        "SITAPEL • Pemutakhiran Data Pemilih Berkelanjutan (PDPB) Tahun 2026 • Komisi Pemilihan Umum Kota Bengkulu"
    )