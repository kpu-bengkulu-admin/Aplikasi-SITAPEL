# ==========================================================
# SITAPEL PDPB 2026
# views/permohonan.py
# BAGIAN 1
# ==========================================================

import streamlit as st

from datetime import datetime

from providers.drive import upload_folder_permohonan

from providers.sheets import (
    get_next_id,
    generate_nomor_permohonan,
    simpan_permohonan,
)

# ==========================================================
# DATA WILAYAH KOTA BENGKULU
# ==========================================================

WILAYAH = {

    "Gading Cempaka": [
        "Cempaka Permai",
        "Jalan Gedang",
        "Lingkar Barat",
        "Padang Harapan",
        "Sidomulyo"
    ],

    "Kampung Melayu": [
        "Kandang",
        "Kandang Mas",
        "Muara Dua",
        "Padang Serai",
        "Sumber Jaya",
        "Teluk Sepang"
    ],

    "Muara Bangkahulu": [
        "Bentiring",
        "Bentiring Permai",
        "Beringin Raya",
        "Kandang Limun",
        "Pematang Gubernur",
        "Rawa Makmur",
        "Rawa Makmur Permai"
    ],

    "Ratu Agung": [
        "Kebun Beler",
        "Kebun Kenanga",
        "Kebun Tebeng",
        "Lempuing",
        "Nusa Indah",
        "Sawah Lebar",
        "Sawah Lebar Baru",
        "Tanah Patah"
    ],

    "Ratu Samban": [
        "Anggut Atas",
        "Anggut Bawah",
        "Anggut Dalam",
        "Belakang Pondok",
        "Kebun Geran",
        "Kebun Dahri",
        "Pengantungan",
        "Padang Jati",
        "Penurunan"
    ],

    "Selebar": [
        "Betungan",
        "Bumi Ayu",
        "Pagar Dewa",
        "Pekan Sabtu",
        "Sukarami",
        "Sumur Dewa"
    ],

    "Singaran Pati": [
        "Dusun Besar",
        "Jembatan Kecil",
        "Lingkar Timur",
        "Panorama",
        "Padang Nangka",
        "Timur Indah"
    ],

    "Sungai Serut": [
        "Kampung Kelawi",
        "Pasar Bengkulu",
        "Semarang",
        "Tanjung Agung",
        "Tanjung Jaya",
        "Surabaya",
        "Sukamerindu"
    ],

    "Teluk Segara": [
        "Bajak",
        "Berkas",
        "Jitra",
        "Kebun Keling",
        "Kebun Roos",
        "Kampung Bali",
        "Malabero",
        "Pasar Baru",
        "Pasar Melintang",
        "Pondok Besi",
        "Pintu Batu",
        "Sumur Meleleh",
        "Tengah Padang"
    ],

}

# ==========================================================
# HALAMAN PERMOHONAN
# ==========================================================

def show_permohonan():

    # ======================================================
    # VALIDASI JENIS LAYANAN
    # ======================================================

    if "jenis_layanan" not in st.session_state:

        st.warning(
            "Silakan memilih jenis layanan terlebih dahulu."
        )

        if st.button(
            "⬅ Kembali",
            key="back_step1",
            use_container_width=True
        ):

            st.session_state["page"] = "dashboard"
            st.rerun()

        st.stop()

    jenis_layanan = st.session_state["jenis_layanan"]

    # ======================================================
    # SESSION
    # ======================================================

    if "step" not in st.session_state:

        st.session_state.step = 1

    # ======================================================
    # CSS
    # ======================================================

    st.markdown(
        """
<style>

.block-container {

    padding-top: 1.5rem;
    max-width: 1150px;

}

.form-box {

    background: white;

    padding: 25px;

    border-radius: 15px;

    border: 1px solid #E5E5E5;

    margin-bottom: 20px;

}

.step-box {

    background: #F8F9FB;

    padding: 15px;

    border-left: 6px solid #005BAC;

    border-radius: 10px;

    margin-bottom: 20px;

}

/* ======================================================
   TOMBOL PRIMARY
   ====================================================== */

div.stButton > button[kind="primary"],
div.stFormSubmitButton > button[kind="primary"] {

    background: #8B001C !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;

    font-weight: 700 !important;

}

div.stButton > button[kind="primary"]:hover,
div.stFormSubmitButton > button[kind="primary"]:hover {

    background: #700016 !important;

    color: white !important;

}

</style>
""",
        unsafe_allow_html=True,
    )

    # ======================================================
    # HEADER
    # ======================================================

    col_logo, col_title = st.columns([1, 6])

    with col_logo:

        st.image(
            "assets/logo_kpu.png",
            width=95
        )

    with col_title:

        st.markdown(
            """
### SITAPEL

**Sistem Informasi Pelayanan Data Pemilih Berkelanjutan (PDPB)**

Komisi Pemilihan Umum Kota Bengkulu

Tahun 2026
"""
        )

    st.divider()

    # ======================================================
    # INFO LAYANAN
    # ======================================================

    st.info(
        f"""
Jenis Layanan yang dipilih :

**{jenis_layanan}**
"""
    )

    # ======================================================
    # PROGRESS
    # ======================================================

    progress = st.session_state.step / 4

    st.progress(progress)

    judul_step = {

        1: "STEP 1 dari 4 • Data Pemohon",

        2: "STEP 2 dari 4 • Data Permohonan",

        3: "STEP 3 dari 4 • Upload Dokumen",

        4: "STEP 4 dari 4 • Review"

    }

    st.markdown(
        f"""
<div class="step-box">

<b>{judul_step[st.session_state.step]}</b>

</div>
""",
        unsafe_allow_html=True
    )

    # ======================================================
    # STEP 1
    # ======================================================

    if st.session_state.step == 1:

        st.markdown(
            '<div class="form-box">',
            unsafe_allow_html=True
        )

        st.subheader("Data Pemohon")

        col1, col2 = st.columns(2)

        with col1:

            nama_pemohon = st.text_input(
                "Nama Pemohon *",
                value=st.session_state.get(
                    "nama_pemohon",
                    ""
                )
            )

            whatsapp = st.text_input(
                "Nomor WhatsApp *",
                value=st.session_state.get(
                    "whatsapp",
                    ""
                ),
                placeholder="08xxxxxxxxxx"
            )

        with col2:

            email = st.text_input(
                "Email",
                value=st.session_state.get(
                    "email",
                    ""
                )
            )

        keterangan_pemohon = st.text_area(

            "Keterangan Pemohon",

            value=st.session_state.get(
                "keterangan_pemohon",
                ""
            ),

            height=120,

            placeholder="""
Tuliskan penjelasan singkat
mengenai permohonan yang diajukan.
"""
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        st.write("")

        kosong, next_col = st.columns([6, 2])

        col_back, col_next = st.columns(2)

        with col_back:

            if st.button(
                "⬅ Kembali ke Dashboard",
                key="back_dashboard",
                use_container_width=True
            ):

                st.session_state.page = "dashboard"

                st.session_state.step = 1

                st.rerun()

        with col_next:

            if st.button(
                "Selanjutnya ➜",
                key="next_step1",
                type="primary",
                use_container_width=True
            ):

                if nama_pemohon.strip() == "":

                    st.error(
                        "Nama Pemohon wajib diisi."
                    )

                elif whatsapp.strip() == "":

                    st.error(
                        "Nomor WhatsApp wajib diisi."
                    )

                else:

                    st.session_state.nama_pemohon = nama_pemohon

                    st.session_state.whatsapp = whatsapp

                    st.session_state.email = email

                    st.session_state.keterangan_pemohon = keterangan_pemohon

                    st.session_state.step = 2

                    st.rerun()

    # ======================================================
    # STEP 2
    # ======================================================

    elif st.session_state.step == 2:

        st.markdown(
            '<div class="form-box">',
            unsafe_allow_html=True
        )

        st.subheader("Data Permohonan")

        kecamatan = st.session_state.get("kecamatan", "")
        kelurahan = st.session_state.get("kelurahan", "")
        alamat_baru = st.session_state.get("alamat_baru", "")
        kategori_tms = st.session_state.get("kategori_tms", "")
        sudah_ktpel = st.session_state.get("sudah_ktpel", "")
        anggota_keluarga = st.session_state.get(
            "anggota_keluarga",
            ""
        )

        # =====================================================
        # TMS
        # =====================================================

        if jenis_layanan == "Pemilih Tidak Memenuhi Syarat (TMS)":

            kategori_list = [
                "",
                "Meninggal Dunia",
                "Menjadi Anggota TNI",
                "Menjadi Anggota POLRI"
            ]

            kategori_tms = st.selectbox(
                "Kategori TMS *",
                kategori_list,
                index=(
                    kategori_list.index(kategori_tms)
                    if kategori_tms in kategori_list
                    else 0
                )
            )

            st.divider()

            nama_diajukan = st.text_input(
                "Nama yang Diajukan *",
                value=st.session_state.get(
                    "nama_diajukan",
                    ""
                )
            )

        # =====================================================
        # PINDAH DOMISILI & PEMILIH BARU
        # =====================================================

        else:

            nama_diajukan = st.text_input(
                "Nama yang Diajukan *",
                value=st.session_state.get(
                    "nama_diajukan",
                    ""
                )
            )

            anggota_keluarga = st.text_area(
                "Anggota Keluarga",
                value=anggota_keluarga,
                placeholder="""
Contoh :

1. Ahmad
2. Siti
3. Budi

Kosongkan apabila hanya satu orang.
"""
            )

        # =====================================================
        # PINDAH DOMISILI
        # =====================================================

        if jenis_layanan == "Pindah Domisili/Tempat Tinggal":

            st.divider()

            st.markdown("##### Tujuan Domisili/Tempat Tinggal")

            col1, col2 = st.columns(2)

            with col1:

                kecamatan = st.selectbox(
                    "Kecamatan",
                    [""] + sorted(WILAYAH.keys()),
                    index=(
                        ([""] + sorted(WILAYAH.keys())).index(kecamatan)
                        if kecamatan in WILAYAH
                        else 0
                    )
                )

            with col2:

                if kecamatan:

                    kel_list = [""] + WILAYAH[kecamatan]

                    kelurahan = st.selectbox(
                        "Kelurahan",
                        kel_list,
                        index=(
                            kel_list.index(kelurahan)
                            if kelurahan in kel_list
                            else 0
                        )
                    )

                else:

                    st.selectbox(
                        "Kelurahan",
                        ["Pilih Kecamatan Terlebih Dahulu"],
                        disabled=True
                    )

            alamat_baru = st.text_area(
                "Alamat Baru",
                value=alamat_baru
            )

        # =====================================================
        # PEMILIH BARU
        # =====================================================

        elif jenis_layanan == "Pemilih Baru/Belum Terdaftar Dalam DPT":

            st.divider()

            sudah_ktpel = st.radio(
                "Sudah Memiliki KTP-el?",
                ["Sudah", "Belum"],
                horizontal=True,
                index=0 if sudah_ktpel != "Belum" else 1
            )

            col1, col2 = st.columns(2)

            with col1:

                kecamatan = st.selectbox(
                    "Kecamatan",
                    [""] + sorted(WILAYAH.keys()),
                    index=(
                        ([""] + sorted(WILAYAH.keys())).index(kecamatan)
                        if kecamatan in WILAYAH
                        else 0
                    )
                )

            with col2:

                if kecamatan:

                    kel_list = [""] + WILAYAH[kecamatan]

                    kelurahan = st.selectbox(
                        "Kelurahan",
                        kel_list,
                        index=(
                            kel_list.index(kelurahan)
                            if kelurahan in kel_list
                            else 0
                        )
                    )

                else:

                    st.selectbox(
                        "Kelurahan",
                        ["Pilih Kecamatan Terlebih Dahulu"],
                        disabled=True
                    )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        st.write("")

        col_back, col_next = st.columns(2)

        with col_back:

            if st.button(
                "⬅ Kembali",
                key="back_step2",
                use_container_width=True
            ):

                st.session_state.step = 1
                st.rerun()

        with col_next:

            if st.button(
                "Selanjutnya ➜",
                key="next_step2",
                type="primary",
                use_container_width=True
            ):

                if nama_diajukan.strip() == "":

                    st.error(
                        "Nama yang diajukan wajib diisi."
                    )

                else:

                    st.session_state.nama_diajukan = nama_diajukan

                    if jenis_layanan == "Pemilih Tidak Memenuhi Syarat (TMS)":

                        st.session_state.anggota_keluarga = ""

                    else:

                        st.session_state.anggota_keluarga = anggota_keluarga

                    st.session_state.kecamatan = kecamatan
                    st.session_state.kelurahan = kelurahan
                    st.session_state.alamat_baru = alamat_baru
                    st.session_state.kategori_tms = kategori_tms
                    st.session_state.sudah_ktpel = sudah_ktpel

                    st.session_state.step = 3

                    st.rerun()

    # ======================================================
    # STEP 3
    # ======================================================

    elif st.session_state.step == 3:


        st.markdown(
            '<div class="form-box">',
            unsafe_allow_html=True
        )

        st.subheader("Upload Dokumen Persyaratan")

        # ======================================================
        # INFORMASI PERSYARATAN
        # ======================================================

        if jenis_layanan == "Pindah Domisili/Tempat Tinggal":

            st.info(
                """
**Persyaratan Dokumen**

• KTP-el
• Kartu Keluarga
• Dokumen Pendukung (Opsional)
"""
            )

        elif jenis_layanan == "Pemilih Baru/Belum Terdaftar Dalam DPT":

            st.info(
                """
**Persyaratan Dokumen**

• Kartu Keluarga
• KTP-el (Wajib apabila sudah memiliki)
• Dokumen Pendukung (Opsional)
"""
            )

        elif jenis_layanan == "Pemilih Tidak Memenuhi Syarat (TMS)":

            kategori = st.session_state.get(
                "kategori_tms",
                ""
            )

            if kategori == "Meninggal Dunia":

                st.info(
                    """
**Persyaratan Dokumen**

• KTP-el
• Kartu Keluarga
• Surat Keterangan Kematian
"""
                )

            elif kategori == "Menjadi Anggota TNI":

                st.info(
                    """
**Persyaratan Dokumen**

• KTP-el
• Kartu Keluarga
• SK / Bukti Menjadi Anggota TNI
"""
                )

            elif kategori == "Menjadi Anggota POLRI":

                st.info(
                    """
**Persyaratan Dokumen**

• KTP-el
• Kartu Keluarga
• SK / Bukti Menjadi Anggota POLRI
"""
                )

        st.divider()

        # ======================================================
        # UPLOAD KTP
        # ======================================================

        upload_ktp = st.file_uploader(
            "Upload KTP-el",
            type=[
                "pdf",
                "jpg",
                "jpeg",
                "png"
            ]
        )

        # ======================================================
        # UPLOAD KK
        # ======================================================

        upload_kk = st.file_uploader(
            "Upload Kartu Keluarga",
            type=[
                "pdf",
                "jpg",
                "jpeg",
                "png"
            ]
        )

        # ======================================================
        # LABEL DOKUMEN PENDUKUNG
        # ======================================================

        label_pendukung = "Upload Dokumen Pendukung"

        if jenis_layanan == "Pemilih Tidak Memenuhi Syarat (TMS)":

            if st.session_state.kategori_tms == "Meninggal Dunia":

                label_pendukung = (
                    "Upload Akta Kematian/Surat Keterangan Kematian dari Kelurahan"
                )

            elif st.session_state.kategori_tms == "Menjadi Anggota TNI":

                label_pendukung = (
                    "Upload SK / KTA / Bukti Menjadi Anggota TNI"
                )

            elif st.session_state.kategori_tms == "Menjadi Anggota POLRI":

                label_pendukung = (
                    "Upload SK / KTA / Bukti Menjadi Anggota POLRI"
                )

        upload_pendukung = st.file_uploader(
            label_pendukung,
            type=[
                "pdf",
                "jpg",
                "jpeg",
                "png"
            ]
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        st.write("")

        col_back, col_next = st.columns(2)

        with col_back:

            if st.button(
                "⬅ Kembali",
                key="back_step3",
                use_container_width=True
            ):

                st.session_state.step = 2

                st.rerun()

        with col_next:

            if st.button(
                "Selanjutnya ➜",
                key="next_step3",
                type="primary",
                use_container_width=True
            ):

                # ==========================================
                # VALIDASI KK
                # ==========================================

                if upload_kk is None:

                    st.error(
                        "Kartu Keluarga wajib diunggah."
                    )

                    st.stop()

                # ==========================================
                # VALIDASI KTP
                # ==========================================

                if (
                    jenis_layanan
                    == "Pindah Domisili/Tempat Tinggal"
                ):

                    if upload_ktp is None:

                        st.error(
                            "KTP-el wajib diunggah."
                        )

                        st.stop()

                elif (
                    jenis_layanan
                    == "Pemilih Baru/Belum Terdaftar Dalam DPT"
                ):

                    if (
                        st.session_state.sudah_ktpel == "Sudah"
                        and upload_ktp is None
                    ):

                        st.error(
                            "KTP-el wajib diunggah."
                        )

                        st.stop()

                elif (
                    jenis_layanan
                    == "Pemilih Tidak Memenuhi Syarat (TMS)"
                ):

                    if upload_ktp is None:

                        st.error(
                            "KTP-el wajib diunggah."
                        )

                        st.stop()

                    if upload_pendukung is None:

                        st.error(
                            "Dokumen pendukung wajib diunggah."
                        )

                        st.stop()

                # ==========================================
                # SIMPAN KE SESSION
                # ==========================================

                st.session_state.upload_ktp = upload_ktp
                st.session_state.upload_kk = upload_kk
                st.session_state.upload_pendukung = upload_pendukung

                st.session_state.step = 4

                st.rerun()


                # ======================================
                # VALIDASI KARTU KELUARGA
                # ======================================

                if upload_kk is None:

                    st.error(
                        "Kartu Keluarga wajib diunggah."
                    )

                    st.stop()

                # ======================================
                # VALIDASI BERDASARKAN JENIS LAYANAN
                # ======================================

                if jenis_layanan == "Pindah Domisili/Tempat Tinggal":

                    if upload_ktp is None:

                        st.error(
                            "KTP-el wajib diunggah."
                        )

                        st.stop()

                elif jenis_layanan == "Pemilih Baru/Belum Terdaftar Dalam DPT":

                    if (
                        st.session_state.sudah_ktpel == "Sudah"
                        and upload_ktp is None
                    ):

                        st.error(
                            "KTP-el wajib diunggah karena Anda memilih Sudah Memiliki KTP-el."
                        )

                        st.stop()

                elif jenis_layanan == "Pemilih Tidak Memenuhi Syarat (TMS)":

                    if upload_ktp is None:

                        st.error(
                            "KTP-el wajib diunggah."
                        )

                        st.stop()

                    if upload_pendukung is None:

                        st.error(
                            "Dokumen pendukung wajib diunggah."
                        )

                        st.stop()

                # ======================================
                # SIMPAN FILE KE SESSION
                # ======================================

                st.session_state.upload_ktp = upload_ktp
                st.session_state.upload_kk = upload_kk
                st.session_state.upload_pendukung = upload_pendukung

                # ======================================
                # LANJUT KE STEP 4
                # ======================================

                st.session_state.step = 4
                st.rerun()

    # ======================================================
    # STEP 4
    # ======================================================

    elif st.session_state.step == 4:

        st.markdown(
            '<div class="form-box">',
            unsafe_allow_html=True
        )

        st.subheader("Review Permohonan")

        st.success(
            "Pastikan seluruh data yang diisi sudah benar sebelum dikirim."
        )

        st.write("### Data Pemohon")

        st.write(
            "**Nama Pemohon :**",
            st.session_state.nama_pemohon
        )

        st.write(
            "**WhatsApp :**",
            st.session_state.whatsapp
        )

        st.write(
            "**Email :**",
            st.session_state.email
        )

        st.divider()

        st.write("### Data Permohonan")

        st.write(
            "**Jenis Layanan :**",
            jenis_layanan
        )

        st.write(
            "**Nama Yang Diajukan :**",
            st.session_state.nama_diajukan
        )

        if st.session_state.anggota_keluarga:

            st.write(
                "**Anggota Keluarga :**",
                st.session_state.anggota_keluarga
            )

        if st.session_state.kecamatan:

            st.write(
                "**Kecamatan :**",
                st.session_state.kecamatan
            )

        if st.session_state.kelurahan:

            st.write(
                "**Kelurahan :**",
                st.session_state.kelurahan
            )

        if st.session_state.alamat_baru:

            st.write(
                "**Alamat Baru :**",
                st.session_state.alamat_baru
            )

        if st.session_state.kategori_tms:

            st.write(
                "**Kategori TMS :**",
                st.session_state.kategori_tms
            )

        if st.session_state.sudah_ktpel:

            st.write(
                "**Sudah Memiliki KTP-el :**",
                st.session_state.sudah_ktpel
            )

        st.divider()

        pernyataan = st.checkbox(
            "Saya menyatakan seluruh data yang saya isi adalah benar."
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        st.write("")

        col_back, col_submit = st.columns(2)

        with col_back:

            if st.button(
                "⬅ Kembali",
                key="back_step4",
                use_container_width=True
            ):

                st.session_state.step = 3
                st.rerun()

        with col_submit:

            if st.button(
                "Kirim Permohonan",
                key="submit_permohonan",
                type="primary",
                use_container_width=True
            ):

                if not pernyataan:

                    st.error(
                        "Silakan centang pernyataan terlebih dahulu."
                    )

                    st.stop()

                with st.spinner(
                    "Mengirim permohonan..."
                ):

                    try:

                        nomor_permohonan = generate_nomor_permohonan()

                        folder_url = upload_folder_permohonan(

                            nomor_permohonan=nomor_permohonan,

                            ktp=st.session_state.upload_ktp,

                            kk=st.session_state.upload_kk,

                            pendukung=st.session_state.upload_pendukung,

                        )

                        now = datetime.now()

                        data = {

                            "ID": get_next_id(),

                            "Nomor Permohonan": nomor_permohonan,

                            "Tanggal": now.strftime("%d-%m-%Y"),

                            "Jam": now.strftime("%H:%M:%S"),

                            "Tahun": now.year,

                            "Bulan": now.strftime("%B"),

                            "Status": "Menunggu Verifikasi",

                            "Jenis Layanan": jenis_layanan,

                            "Nama Pemohon": st.session_state.nama_pemohon,

                            "WhatsApp": st.session_state.whatsapp,

                            "Email": st.session_state.email,

                            "Nama Diajukan": st.session_state.nama_diajukan,

                            "Anggota Keluarga": st.session_state.anggota_keluarga,

                            "Kecamatan": st.session_state.kecamatan,

                            "Kelurahan": st.session_state.kelurahan,

                            "Alamat Baru": st.session_state.alamat_baru,

                            "Kategori TMS": st.session_state.kategori_tms,

                            "Sudah Memiliki KTP-el": st.session_state.sudah_ktpel,

                            "Keterangan Pemohon": st.session_state.keterangan_pemohon,

                            "Link Folder Drive": folder_url,

                        }

                        simpan_permohonan(data)

                        st.session_state.nomor_permohonan = nomor_permohonan

                        st.session_state.status_permohonan = "Menunggu Verifikasi"

                        st.session_state.waktu_submit = now.strftime(
                            "%d-%m-%Y %H:%M:%S"
                        )

                        st.session_state["page"] = "success"

                        st.rerun()

                    except Exception as e:

                        st.error(
                            f"Gagal mengirim permohonan.\n\n{e}"
                        )