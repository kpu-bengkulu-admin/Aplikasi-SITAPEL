# ==========================================================
# STEP 6
# HALAMAN SUKSES
# ==========================================================

from datetime import datetime

import streamlit as st


def show_success():

    # ======================================================
    # HEADER
    # ======================================================

    st.title("🎉 Permohonan Berhasil Dikirim")

    st.success(
        "Data Anda telah berhasil diproses oleh sistem SITAPEL."
    )

    st.write(
        """
        Terima kasih telah menggunakan layanan
        **Sistem Informasi Pelayanan Pemutakhiran Data Pemilih Berkelanjutan (SITAPEL)**.

        Permohonan Anda telah berhasil diterima dan akan diproses
        oleh petugas KPU Kota Bengkulu.
        """
    )

    st.divider()

    # ======================================================
    # NOMOR PERMOHONAN
    # ======================================================

    nomor = st.session_state.get(
        "nomor_permohonan"
    )

    if nomor:

        st.subheader("📌 Nomor Permohonan")

        st.code(
            nomor,
            language="text"
        )

    # ======================================================
    # STATUS
    # ======================================================

    st.subheader("📋 Status Permohonan")

    st.success(
        "Menunggu Verifikasi"
    )

    # ======================================================
    # TANGGAL SUBMIT
    # ======================================================

    tanggal = st.session_state.get(
        "tanggal_submit"
    )

    if tanggal:

        st.subheader("🗓️ Tanggal Pengajuan")

        st.write(
            tanggal.strftime("%d %B %Y %H:%M WIB")
        )

    st.divider()

    # ======================================================
    # RINGKASAN DATA
    # ======================================================

    st.subheader("👤 Ringkasan Data")

    st.write(
        f"**Nama Pemohon :** {st.session_state.get('nama_pemohon', '-')}"
    )

    st.write(
        f"**Jenis Layanan :** {st.session_state.get('layanan', '-')}"
    )

    st.write(
        f"**Email :** {st.session_state.get('email', '-')}"
    )

    st.write(
        f"**WhatsApp :** {st.session_state.get('whatsapp', '-')}"
    )

    st.divider()

    # ======================================================
    # GOOGLE DRIVE
    # ======================================================

    folder_link = st.session_state.get(
        "folder_link"
    )

    if folder_link:

        st.subheader("📂 Dokumen Permohonan")

        st.link_button(
            "🔗 Lihat Folder Google Drive",
            folder_link,
            use_container_width=True
        )

    st.divider()

    # ======================================================
    # INFORMASI LANJUTAN
    # ======================================================

    st.info(
        """
        📌 Simpan nomor permohonan untuk keperluan pengecekan status.

        📩 Petugas KPU Kota Bengkulu akan melakukan verifikasi
        terhadap data dan dokumen yang telah Anda kirimkan.

        📱 Apabila diperlukan konfirmasi tambahan,
        petugas akan menghubungi melalui Email atau WhatsApp
        yang telah didaftarkan.

        🗂️ Seluruh dokumen tersimpan dengan aman
        pada Google Drive.
        """
    )

    st.divider()

    # ======================================================
    # KEMBALI KE DASHBOARD
    # ======================================================

    if st.button(
        "🏠 Kembali ke Dashboard",
        use_container_width=True
    ):

        keys = list(
            st.session_state.keys()
        )

        keep = {

            "page",

            "step"

        }

        for key in keys:

            if key not in keep:

                del st.session_state[key]

        st.session_state.page = "dashboard"

        st.session_state.step = 1

        st.rerun()