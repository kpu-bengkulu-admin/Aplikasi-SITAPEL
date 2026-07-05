# ==========================================================
# SITAPEL v3 FINAL
# pages/permohonan.py
# ==========================================================

import streamlit as st

# ==========================================================
# SESSION STATE
# SITAPEL v3 FINAL
# ==========================================================

DEFAULT_STATE = {

    # ======================================================
    # NAVIGASI
    # ======================================================

    "step": 1,

    # Jenis layanan yang dipilih
    "layanan": "",

    # Nomor permohonan
    "nomor_permohonan": "",

    # ======================================================
    # DATA PEMOHON
    # ======================================================

    "nama_pemohon": "",
    "email": "",
    "whatsapp": "",

    # ======================================================
    # DATA PERMOHONAN
    # ======================================================

    # Nama Kepala Keluarga / Nama yang diajukan
    "nama_diajukan": "",

    # Jumlah anggota keluarga
    "jumlah_anggota": 1,

    # Daftar anggota keluarga
    "anggota_pindah": [],

    # Tujuan pindah
    "kabupaten": "",
    "kecamatan": "",
    "kelurahan": "",
    "alamat_baru": "",

    # Alasan
    "alasan": "Pindah Domisili / Tempat Tinggal",
    "alasan_lainnya": "",
    # Keterangan
    "keterangan": "",

    # Khusus TMS
    "kategori_tms": "",

    # Khusus Pemilih Baru
    "sudah_ktp": "Sudah",

    # ======================================================
    # DOKUMEN
    # ======================================================

    # Tidak perlu kk_file, ktp_file, dll
    # karena file_uploader akan membuat
    # session_state sendiri melalui key.

    # ======================================================
    # REVIEW
    # ======================================================

    "persetujuan": False,

    # ======================================================
    # HASIL SUBMIT
    # ======================================================

    "status_permohonan": "Draft",

    "folder_link": "",

    "waktu_submit": "",

}

for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ==========================================================
# HALAMAN PERMOHONAN
# ==========================================================

def show_permohonan():

    st.title("📝 Pengajuan Permohonan")

    if st.session_state.layanan:
        st.info(f"Layanan : **{st.session_state.layanan}**")

    TOTAL_STEP = 4

    st.progress(st.session_state.step / TOTAL_STEP)

    st.caption(
        f"Langkah {st.session_state.step} dari {TOTAL_STEP}"
    )

    st.divider()

    if st.session_state.step == 1:

        tampil_step1()

    elif st.session_state.step == 2:

        tampil_step2()

    elif st.session_state.step == 3:

        tampil_step3()

    elif st.session_state.step == 4:

        tampil_step4()

    elif st.session_state.step == 5:

        tampil_step5()

    elif st.session_state.step == 6:

        tampil_step6()


# ==========================================================
# STEP 1
# DATA PEMOHON
# ==========================================================

def tampil_step1():

    st.subheader("👤 Data Pemohon")

    st.write(
        """
        Silakan mengisi data pemohon.

        Data ini digunakan oleh petugas KPU Kota Bengkulu
        apabila diperlukan proses konfirmasi atau verifikasi
        terhadap permohonan yang diajukan.
        """
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "Nama Pemohon *",
            key="nama_pemohon",
            placeholder="Masukkan nama lengkap"
        )

        st.text_input(
            "Email Aktif *",
            key="email",
            placeholder="contoh@email.com"
        )

    with col2:

        st.text_input(
            "Nomor WhatsApp *",
            key="whatsapp",
            placeholder="08xxxxxxxxxx"
        )

        st.info(
            """
            Pastikan nomor WhatsApp aktif.

            Petugas akan menghubungi nomor tersebut
            apabila diperlukan verifikasi data.
            """
        )

    st.divider()

    kiri, kanan = st.columns([5,1])

    with kiri:

        if st.button(
            "← Kembali",
            use_container_width=True
        ):

            st.session_state.page = "dashboard"

            st.session_state.step = 1

            st.rerun()

    with kanan:

        if st.button(
            "Lanjut →",
            use_container_width=True
        ):

            if st.session_state.nama_pemohon.strip() == "":

                st.warning(
                    "Nama pemohon wajib diisi."
                )

                return

            if st.session_state.email.strip() == "":

                st.warning(
                    "Email wajib diisi."
                )

                return

            if "@" not in st.session_state.email:

                st.warning(
                    "Format email belum benar."
                )

                return

            if st.session_state.whatsapp.strip() == "":

                st.warning(
                    "Nomor WhatsApp wajib diisi."
                )

                return

            if not st.session_state.whatsapp.startswith("08"):

                st.warning(
                    "Nomor WhatsApp harus diawali 08."
                )

                return

            st.session_state.step = 2

            st.rerun()



# ==========================================================
# STEP 2
# ==========================================================

# ==========================================================
# HELPER
# STEP 2
# ==========================================================

def sinkronkan_anggota():
    """
    Menyesuaikan jumlah anggota keluarga.
    """

    jumlah = st.session_state.jumlah_anggota

    anggota = st.session_state.get(
        "anggota_pindah",
        []
    )

    while len(anggota) < jumlah:

        anggota.append({
            "nama": ""
        })

    while len(anggota) > jumlah:

        anggota.pop()

    st.session_state.anggota_pindah = anggota

def ubah_nama_anggota(index):

    anggota = st.session_state.anggota_pindah

    anggota[index]["nama"] = st.session_state[
        f"anggota_{index}"
    ]

    st.session_state.anggota_pindah = anggota

def tampil_step2():

    st.subheader("📋 Data Permohonan")

    layanan = st.session_state.layanan

    # =====================================================
    # PINDAH DOMISILI
    # =====================================================

    if layanan == "Pindah Domisili":

        st.markdown("### 👨‍👩‍👧 Data Kepala Keluarga")

        st.text_input(
            "Nama Kepala Keluarga *",
            key="nama_diajukan",
            placeholder="Masukkan nama kepala keluarga sesuai KK"
        )

        st.divider()

        st.markdown("### 👨‍👩‍👧‍👦 Anggota Keluarga yang Akan Pindah")

        st.selectbox(
            "Jumlah anggota keluarga yang ikut pindah",
            options=list(range(1, 17)),
            key="jumlah_anggota",
            on_change=sinkronkan_anggota
        )

        sinkronkan_anggota()

        for i in range(st.session_state.jumlah_anggota):

            if len(st.session_state.anggota_pindah) <= i:

                st.session_state.anggota_pindah.append({
                    "nama": ""
                })

            st.text_input(
                f"Nama Anggota {i+1} *",
                value=st.session_state.anggota_pindah[i]["nama"],
                key=f"anggota_{i}",
                on_change=ubah_nama_anggota,
                args=(i,),
                placeholder="Sesuai Kartu Keluarga"
            )

        st.info(
            "💡 Masukkan nama seluruh anggota keluarga yang akan pindah memilih sesuai Kartu Keluarga."
        )

        st.divider()

        st.markdown("### 📍 Tujuan Pindah")

        col1, col2 = st.columns(2)

        with col1:

            st.text_input(
                "Kabupaten / Kota Tujuan *",
                key="kabupaten"
            )

            st.text_input(
                "Kecamatan *",
                key="kecamatan"
            )

        with col2:

            st.text_input(
                "Kelurahan / Desa *",
                key="kelurahan"
            )

            st.text_area(
                "Alamat Lengkap Tujuan *",
                key="alamat_baru",
                height=120
            )

        st.selectbox(
            "Alasan Mengajukan Pindah Memilih",
            [
                "Pindah Domisili / Tempat Tinggal",
                "Pekerjaan",
                "Pendidikan",
                "Mengikuti Keluarga",
                "Perawatan Kesehatan",
                "Penugasan Dinas",
                "Lainnya"
            ],
            key="alasan"
        )

        if st.session_state.alasan == "Lainnya":

            st.text_input(
                "Tuliskan alasan",
                key="alasan_lainnya"
            )

    # =====================================================
    # TMS
    # =====================================================

    elif layanan == "TMS":

        st.markdown("### 👤 Data Pemilih")

        st.text_input(
            "Nama Pemilih *",
            key="nama_diajukan",
            placeholder="Masukkan nama sesuai KTP-el atau Kartu Keluarga"
        )

        st.selectbox(
            "Kategori Tidak Memenuhi Syarat (TMS) *",
            [
                "Meninggal Dunia",
                "Menjadi Anggota TNI",
                "Menjadi Anggota POLRI",
                "Di bawah 17 Tahun (Belum Menikah)"
            ],
            key="kategori_tms"
        )

        st.text_area(
            "Keterangan (Opsional)",
            key="keterangan",
            height=100,
            placeholder="Tambahkan informasi apabila diperlukan."
        )

        st.info(
            "📌 Dokumen pendukung akan diunggah pada langkah berikutnya sesuai kategori yang dipilih."
        )

    # =====================================================
    # PEMILIH BARU
    # =====================================================

    elif layanan == "Pemilih Baru":

        st.markdown("### 👤 Data Pemilih Baru")

        st.text_input(
            "Nama Pemilih *",
            key="nama_diajukan",
            placeholder="Masukkan nama sesuai KTP-el atau Kartu Keluarga"
        )

        st.text_area(
            "Alamat Domisili *",
            key="alamat_baru",
            height=120,
            placeholder="Masukkan alamat domisili lengkap."
        )

        st.radio(
            "Status KTP-el",
            [
                "Sudah Memiliki KTP-el",
                "Belum Memiliki KTP-el"
            ],
            horizontal=True,
            key="sudah_ktp"
        )

        st.text_area(
            "Keterangan (Opsional)",
            key="alasan_lainnya",
            height=100,
            placeholder="Tambahkan informasi apabila diperlukan."
        )

        st.info(
            "📌 Dokumen pendukung akan diunggah pada langkah berikutnya."
        )

    st.divider()

    kiri, kanan = st.columns(2)

    with kiri:

        if st.button(
            "← Sebelumnya",
            use_container_width=True
        ):

            st.session_state.step = 1
            st.rerun()

    with kanan:

        if st.button(
            "Lanjut →",
            type="primary",
            use_container_width=True
        ):

            errors = []

            layanan = st.session_state.layanan

            # ==========================================
            # PINDAH DOMISILI
            # ==========================================

            if layanan == "Pindah Domisili":

                if not st.session_state.nama_diajukan.strip():
                    errors.append("Nama Kepala Keluarga wajib diisi.")

                if not st.session_state.kabupaten.strip():
                    errors.append("Kabupaten/Kota tujuan wajib diisi.")

                if not st.session_state.kecamatan.strip():
                    errors.append("Kecamatan wajib diisi.")

                if not st.session_state.kelurahan.strip():
                    errors.append("Kelurahan/Desa wajib diisi.")

                if not st.session_state.alamat_baru.strip():
                    errors.append("Alamat tujuan wajib diisi.")

                for i, anggota in enumerate(st.session_state.anggota_pindah):

                    if not anggota["nama"].strip():
                        errors.append(
                            f"Nama Anggota {i+1} wajib diisi."
                        )

                if (
                    st.session_state.alasan == "Lainnya"
                    and not st.session_state.alasan_lainnya.strip()
                ):
                    errors.append(
                        "Tuliskan alasan pindah."
                    )

            # ==========================================
            # TMS
            # ==========================================

            elif layanan == "TMS":

                if not st.session_state.nama_diajukan.strip():
                    errors.append("Nama Pemilih wajib diisi.")

                if not st.session_state.kategori_tms.strip():
                    errors.append("Kategori TMS wajib dipilih.")

            # ==========================================
            # PEMILIH BARU
            # ==========================================

            elif layanan == "Pemilih Baru":

                if not st.session_state.nama_diajukan.strip():
                    errors.append("Nama Pemilih wajib diisi.")

                if not st.session_state.alamat_baru.strip():
                    errors.append("Alamat domisili wajib diisi.")

            # ==========================================
            # TAMPILKAN ERROR
            # ==========================================

            if errors:

                st.error(
                    "Silakan lengkapi data berikut:"
                )

                for pesan in errors:

                    st.write(f"• {pesan}")

                st.stop()

            st.session_state.step = 3
            st.rerun()


# ==========================================================
# HELPER UPLOAD DOKUMEN
# ==========================================================

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_FILE_TYPES = [
    "pdf",
    "jpg",
    "jpeg",
    "png"
]


def format_file_size(size):

    """
    Mengubah ukuran file menjadi format yang mudah dibaca.
    """

    if size < 1024:
        return f"{size} B"

    if size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"

    return f"{size / (1024 * 1024):.2f} MB"


def validasi_file(uploaded_file, wajib=False):

    """
    Validasi file upload.

    Return:
        True  = valid
        False = tidak valid
    """

    if uploaded_file is None:

        if wajib:
            return False

        return True

    # ======================================================
    # VALIDASI UKURAN
    # ======================================================

    if uploaded_file.size > MAX_FILE_SIZE:

        st.error(
            f"❌ {uploaded_file.name} melebihi batas maksimal 10 MB."
        )

        return False

    # ======================================================
    # VALIDASI EKSTENSI
    # ======================================================

    ekstensi = uploaded_file.name.split(".")[-1].lower()

    if ekstensi not in ALLOWED_FILE_TYPES:

        st.error(
            f"❌ Format file {uploaded_file.name} tidak didukung."
        )

        return False

    return True


def tampilkan_info_file(uploaded_file, judul):

    """
    Menampilkan informasi file yang telah dipilih.
    """

    if uploaded_file is None:

        st.caption(f"Belum ada {judul.lower()} yang dipilih.")

        return

    st.success(f"✅ {judul}")

    col1, col2 = st.columns([4, 1])

    with col1:

        st.write(uploaded_file.name)

    with col2:

        st.caption(
            format_file_size(uploaded_file.size)
        )

def tampil_card_persyaratan(judul, daftar):

    """
    Menampilkan daftar persyaratan dokumen.
    """

    with st.container(border=True):

        st.markdown(f"#### 📋 {judul}")

        for item in daftar:

            st.markdown(f"✅ {item}")

def upload_field(
    label,
    key,
    wajib=False,
    help_text=None
):
    """
    Widget upload dokumen.
    """

    uploaded = st.file_uploader(
        label,
        type=ALLOWED_FILE_TYPES,
        key=key,
        help=help_text
    )

    tampilkan_info_file(
        uploaded,
        label
    )

    valid = validasi_file(
        uploaded,
        wajib=wajib
    )

    return uploaded, valid

def tampil_judul_step3():

    st.subheader(
        "📂 Upload Dokumen"
    )

    st.caption(
        "Unggah dokumen sesuai persyaratan layanan yang dipilih."
    )

    st.divider()

# ==========================================================
# STEP 3
# UPLOAD DOKUMEN
# UPLOAD PINDAH DOMISILI
# ==========================================================

def upload_pindah_domisili():

    tampil_card_persyaratan(
        "Persyaratan Dokumen",
        [
            "Kartu Keluarga (Wajib)",
            "KTP-el Pemohon (Wajib)",
            "Dokumen Pendukung (Opsional)",
            "Format file: PDF, JPG, JPEG atau PNG",
            "Ukuran maksimal setiap file: 10 MB"
        ]
    )

    st.markdown("### 📎 Upload Dokumen")

    kk_file, kk_valid = upload_field(
        label="🏠 Kartu Keluarga *",
        key="kk_file",
        wajib=True,
        help_text="Unggah scan atau foto Kartu Keluarga."
    )

    ktp_file, ktp_valid = upload_field(
        label="🪪 KTP-el Pemohon *",
        key="ktp_file",
        wajib=True,
        help_text="Unggah scan atau foto KTP-el."
    )

    dokumen_file, dokumen_valid = upload_field(
        label="📄 Dokumen Pendukung (Opsional)",
        key="dokumen_file",
        wajib=False,
        help_text="Unggah dokumen pendukung apabila diperlukan."
    )

# ==========================================================
# UPLOAD TMS
# ==========================================================

def upload_tms():

    kategori = st.session_state.kategori_tms

    persyaratan = {
        "Meninggal Dunia": [
            "Surat Keterangan Kematian atau Akta Kematian",
            "Dokumen pendukung lainnya (jika ada)",
            "Format file: PDF, JPG, JPEG atau PNG",
            "Ukuran maksimal setiap file: 10 MB"
        ],
        "Menjadi Anggota TNI": [
            "SK Pengangkatan atau Kartu Tanda Anggota TNI",
            "Dokumen pendukung lainnya (jika ada)",
            "Format file: PDF, JPG, JPEG atau PNG",
            "Ukuran maksimal setiap file: 10 MB"
        ],
        "Menjadi Anggota POLRI": [
            "SK Pengangkatan atau Kartu Tanda Anggota POLRI",
            "Dokumen pendukung lainnya (jika ada)",
            "Format file: PDF, JPG, JPEG atau PNG",
            "Ukuran maksimal setiap file: 10 MB"
        ],
        "Di bawah 17 Tahun (Belum Menikah)": [
            "Kartu Keluarga",
            "Dokumen pendukung lainnya (jika ada)",
            "Format file: PDF, JPG, JPEG atau PNG",
            "Ukuran maksimal setiap file: 10 MB"
        ]
    }

    tampil_card_persyaratan(
        "Persyaratan Dokumen",
        persyaratan.get(kategori, [])
    )

    st.markdown("### 📎 Upload Dokumen")

    dokumen_file, dokumen_valid = upload_field(
        label="📄 Dokumen Pendukung *",
        key="dokumen_file",
        wajib=True,
        help_text="Unggah dokumen sesuai kategori TMS yang dipilih."
    )

# ==========================================================
# UPLOAD PEMILIH BARU
# ==========================================================

def upload_pemilih_baru():

    tampil_card_persyaratan(
        "Persyaratan Dokumen",
        [
            "KTP-el atau Surat Keterangan Perekaman (Wajib jika sudah memiliki)",
            "Kartu Keluarga (Wajib)",
            "Dokumen Pendukung (Opsional)",
            "Format file: PDF, JPG, JPEG atau PNG",
            "Ukuran maksimal setiap file: 10 MB"
        ]
    )

    st.markdown("### 📎 Upload Dokumen")

    kk_file, kk_valid = upload_field(
        label="🏠 Kartu Keluarga *",
        key="kk_file",
        wajib=True,
        help_text="Unggah scan atau foto Kartu Keluarga."
    )

    if st.session_state.sudah_ktp == "Sudah Memiliki KTP-el":

        ktp_file, ktp_valid = upload_field(
            label="🪪 KTP-el *",
            key="ktp_file",
            wajib=True,
            help_text="Unggah scan atau foto KTP-el."
        )

    else:

        ktp_file, ktp_valid = upload_field(
            label="📄 Surat Keterangan Perekaman (Opsional)",
            key="ktp_file",
            wajib=False,
            help_text="Unggah Surat Keterangan Perekaman apabila sudah ada."
        )

    dokumen_file, dokumen_valid = upload_field(
        label="📎 Dokumen Pendukung (Opsional)",
        key="dokumen_file",
        wajib=False,
        help_text="Unggah dokumen pendukung apabila diperlukan."
    )

# ==========================================================
# NAVIGASI STEP 3
# ==========================================================

def tampil_navigasi_step3():

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "← Sebelumnya",
            use_container_width=True
        ):

            st.session_state.step = 2
            st.rerun()

    with col2:

        if st.button(
            "Lanjut →",
            type="primary",
            use_container_width=True
        ):

            layanan = st.session_state.layanan

            errors = []

            # ==========================================
            # PINDAH DOMISILI
            # ==========================================

            if layanan == "Pindah Domisili":

                if st.session_state.get("kk_file") is None:
                    errors.append("Kartu Keluarga wajib diunggah.")

                if st.session_state.get("ktp_file") is None:
                    errors.append("KTP-el Pemohon wajib diunggah.")

            # ==========================================
            # TMS
            # ==========================================

            elif layanan == "TMS":

                if st.session_state.get("dokumen_file") is None:
                    errors.append("Dokumen pendukung wajib diunggah.")

            # ==========================================
            # PEMILIH BARU
            # ==========================================

            elif layanan == "Pemilih Baru":

                if st.session_state.get("kk_file") is None:
                    errors.append("Kartu Keluarga wajib diunggah.")

                if (
                    st.session_state.sudah_ktp == "Sudah Memiliki KTP-el"
                    and st.session_state.get("ktp_file") is None
                ):
                    errors.append("KTP-el wajib diunggah.")

            # ==========================================
            # TAMPILKAN ERROR
            # ==========================================

            if errors:

                st.warning("Silakan lengkapi dokumen berikut:")

                for err in errors:
                    st.markdown(f"✅ {err}")

                st.stop()

            st.session_state.step = 4
            st.rerun()

# ==========================================================
# STEP 3
# UPLOAD DOKUMEN
# ==========================================================

def tampil_step3():

    layanan = st.session_state.layanan

    tampil_judul_step3()

    if layanan == "Pindah Domisili":

        upload_pindah_domisili()

    elif layanan == "TMS":

        upload_tms()

    elif layanan == "Pemilih Baru":

        upload_pemilih_baru()

    tampil_navigasi_step3()

# ==========================================================
# STEP 4
# KONFIRMASI PERMOHONAN
# ==========================================================

def tampil_step4():
    st.write("STEP:", st.session_state.step)
    st.write(dict(st.session_state))

    st.subheader("📝 Konfirmasi Permohonan")

    st.info(
        """
        Periksa kembali seluruh data yang telah Anda isi.
        Pastikan data dan dokumen yang diunggah sudah benar sebelum mengirim permohonan.
        """
    )

    st.divider()

    # ======================================================
    # DATA PEMOHON
    # ======================================================

    with st.container(border=True):

        st.markdown("### 👤 Data Pemohon")

        st.write(f"**Nama** : {st.session_state.nama_pemohon}")
        st.write(f"**WhatsApp** : {st.session_state.whatsapp}")
        st.write(f"**Email** : {st.session_state.email}")

    st.markdown("")

    # ======================================================
    # DATA PERMOHONAN
    # ======================================================

    with st.container(border=True):

        st.markdown("### 📋 Data Permohonan")

        layanan = st.session_state.layanan

        st.write(f"**Jenis Layanan** : {layanan}")

        # ==============================================
        # PINDAH DOMISILI
        # ==============================================

        if layanan == "Pindah Domisili":

            st.write(
                f"**Nama Kepala Keluarga** : "
                f"{st.session_state.nama_diajukan}"
            )

            st.write("**Anggota Keluarga yang Pindah:**")

            for i, anggota in enumerate(
                st.session_state.anggota_pindah,
                start=1
            ):

                if anggota["nama"].strip():

                    st.write(
                        f"{i}. {anggota['nama']}"
                    )

            st.write(
                f"**Kabupaten/Kota Tujuan** : "
                f"{st.session_state.kabupaten}"
            )

            st.write(
                f"**Kecamatan** : "
                f"{st.session_state.kecamatan}"
            )

            st.write(
                f"**Kelurahan/Desa** : "
                f"{st.session_state.kelurahan}"
            )

            st.write(
                f"**Alamat Tujuan** : "
                f"{st.session_state.alamat_baru}"
            )

            if st.session_state.alasan == "Lainnya":

                alasan = st.session_state.alasan_lainnya

            else:

                alasan = st.session_state.alasan

            st.write(f"**Alasan** : {alasan}")

        # ==============================================
        # TMS
        # ==============================================

        elif layanan == "TMS":

            st.write(
                f"**Nama Pemilih** : "
                f"{st.session_state.nama_diajukan}"
            )

            st.write(
                f"**Kategori TMS** : "
                f"{st.session_state.kategori_tms}"
            )

            if st.session_state.keterangan.strip():

                st.write(
                    f"**Keterangan** : "
                    f"{st.session_state.keterangan}"
                )

        # ==============================================
        # PEMILIH BARU
        # ==============================================

        elif layanan == "Pemilih Baru":

            st.write(
                f"**Nama Pemilih** : "
                f"{st.session_state.nama_diajukan}"
            )

            st.write(
                f"**Alamat Domisili** : "
                f"{st.session_state.alamat_baru}"
            )

            st.write(
                f"**Status KTP-el** : "
                f"{st.session_state.sudah_ktp}"
            )

            if st.session_state.keterangan.strip():

                st.write(
                    f"**Keterangan** : "
                    f"{st.session_state.keterangan}"
                )

    # ======================================================
    # DOKUMEN YANG DIUNGGAH
    # ======================================================

    with st.container(border=True):

        st.markdown("### 📂 Dokumen")

        def tampilkan_file(label, key):

            file = st.session_state.get(key)

            if file is None:

                st.write(f"**{label}** : -")

            else:

                st.write(
                    f"**{label}** : {file.name}"
                )

        layanan = st.session_state.layanan

        if layanan == "Pindah Domisili":

            tampilkan_file(
                "Kartu Keluarga",
                "kk_file"
            )

            tampilkan_file(
                "KTP-el",
                "ktp_file"
            )

            tampilkan_file(
                "Dokumen Pendukung",
                "dokumen_file"
            )

        elif layanan == "TMS":

            tampilkan_file(
                "Dokumen Pendukung",
                "dokumen_file"
            )

        elif layanan == "Pemilih Baru":

            tampilkan_file(
                "Kartu Keluarga",
                "kk_file"
            )

            tampilkan_file(
                "KTP-el / Surat Keterangan",
                "ktp_file"
            )

            tampilkan_file(
                "Dokumen Pendukung",
                "dokumen_file"
            )

    st.divider()

    # ======================================================
    # PERSETUJUAN
    # ======================================================

    st.checkbox(
        "Saya menyatakan bahwa seluruh data dan dokumen yang saya "
        "unggah adalah benar dan dapat dipertanggungjawabkan.",
        key="persetujuan"
    )

    st.caption(
        "Dengan mengirim permohonan ini, Anda menyetujui bahwa "
        "data akan diproses oleh KPU Kota Bengkulu sesuai "
        "ketentuan yang berlaku."
    )

    st.divider()

    # ======================================================
    # NAVIGASI
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "← Sebelumnya",
            use_container_width=True
        ):

            st.session_state.step = 3
            st.rerun()

    with col2:

        if st.button(
            "📤 Kirim Permohonan",
            type="primary",
            use_container_width=True
        ):

            if not st.session_state.persetujuan:

                st.warning(
                    "Silakan centang pernyataan persetujuan terlebih dahulu."
                )

                st.stop()

            # Step 5 akan dipanggil di sini
            st.session_state.step = 5
            st.rerun()

# ==========================================================
# STEP 5
# PROSES PENGIRIMAN
# ==========================================================

def tampil_step5():

    from services.submit import submit_permohonan

    st.subheader("📤 Mengirim Permohonan")

    st.info(
        """
        Mohon tunggu beberapa saat.

        Sistem sedang:

        • Membuat nomor permohonan
        • Membuat folder Google Drive
        • Mengunggah dokumen
        • Menyimpan data ke database
        """
    )

    progress = st.progress(0)

    try:

        progress.progress(20)

        hasil = submit_permohonan()

        progress.progress(100)

        st.session_state.nomor_permohonan = (
            hasil["nomor_permohonan"]
        )

        st.session_state.folder_link = (
            hasil["folder_link"]
        )

        st.session_state.status_permohonan = (
            "Menunggu Verifikasi"
        )

        st.session_state.step = 6

        st.rerun()

    except Exception as e:

        st.error(
            f"Gagal mengirim permohonan.\n\n{e}"
        )

        if st.button(
            "← Kembali",
            use_container_width=True
        ):

            st.session_state.step = 4

            st.rerun()

