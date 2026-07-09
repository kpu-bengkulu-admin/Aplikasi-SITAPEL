# ==========================================================
# SITAPEL PDPB 2026
# views/success.py
# HALAMAN BERHASIL
# KOMISI PEMILIHAN UMUM KOTA BENGKULU
# ==========================================================

import streamlit as st


# ==========================================================
# RESET SESSION PERMOHONAN
# ==========================================================

def reset_permohonan():

    keys = [

        "step",

        "jenis_layanan",

        "nama_pemohon",
        "whatsapp",
        "email",

        "nama_diajukan",
        "anggota_keluarga",

        "kecamatan",
        "kelurahan",
        "alamat_baru",

        "kategori_tms",
        "sudah_ktpel",

        "keterangan_pemohon",

        "upload_ktp",
        "upload_kk",
        "upload_pendukung",

        "status_permohonan",
        "waktu_submit",

    ]

    for key in keys:

        if key in st.session_state:

            del st.session_state[key]

    st.session_state.step = 1


# ==========================================================
# HALAMAN SUCCESS
# ==========================================================

def show_success():

    # ======================================================
    # VALIDASI SESSION
    # ======================================================

    if st.session_state.get("nomor_permohonan", "") == "":

        st.warning(
            "Data permohonan tidak ditemukan."
        )

        if st.button(
            "Kembali ke Dashboard",
            use_container_width=True
        ):

            st.session_state.page = "dashboard"
            st.rerun()

        st.stop()

    # ======================================================
    # HEADER
    # ======================================================

    st.balloons()

    st.markdown(
        """
        <div style="
            background:#ffffff;
            border-radius:15px;
            padding:25px;
            border:1px solid #E5E5E5;
            text-align:center;
        ">

        <h1 style="color:#00843D;">
        ✅ Permohonan Berhasil Dikirim
        </h1>

        <h4>
        Sistem Informasi Pelayanan Data Pemilih
        secara Berkelanjutan (PDPB)
        </h4>

        <p>
        Komisi Pemilihan Umum Kota Bengkulu
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ======================================================
    # INFORMASI
    # ======================================================

    st.success(
        """
Permohonan Anda telah berhasil diterima.

Silakan simpan Nomor Permohonan berikut untuk
melakukan pengecekan status permohonan.
"""
    )

    st.divider()

    # ======================================================
    # NOMOR PERMOHONAN
    # ======================================================

    st.subheader("Nomor Permohonan")

    st.code(
        st.session_state.nomor_permohonan,
        language=None
    )

    st.divider()

    # ======================================================
    # DETAIL PERMOHONAN
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "Status",
            value=st.session_state.get(
                "status_permohonan",
                "Menunggu Verifikasi"
            ),
            disabled=True
        )

        st.text_input(
            "Jenis Layanan",
            value=st.session_state.get(
                "jenis_layanan",
                "-"
            ),
            disabled=True
        )

    with col2:

        st.text_input(
            "Tanggal & Waktu Pengajuan",
            value=st.session_state.get(
                "waktu_submit",
                "-"
            ),
            disabled=True
        )

        st.text_input(
            "Nomor WhatsApp",
            value=st.session_state.get(
                "whatsapp",
                "-"
            ),
            disabled=True
        )

    st.divider()

    # ======================================================
    # INFORMASI LANJUTAN
    # ======================================================

    st.markdown(
        """
### Tahapan Selanjutnya

1. Petugas KPU akan memverifikasi data.

2. Bila ada kekurangan dokumen,
   status berubah menjadi
   **Perlu Perbaikan Dokumen**.

3. Bila seluruh dokumen lengkap,
   permohonan diproses.

4. Gunakan Nomor Permohonan
   untuk mengecek status.
"""
    )

    st.info(
        """
Estimasi verifikasi mengikuti jam kerja
KPU Kota Bengkulu.
"""
    )

    st.divider()

    # ======================================================
    # TOMBOL
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔍 Cek Status Permohonan",
            type="primary",
            use_container_width=True
        ):

            st.session_state.page = "cek_status"
            st.rerun()

    with col2:

        if st.button(
            "🏠 Kembali ke Dashboard",
            use_container_width=True
        ):

            reset_permohonan()

            st.session_state.page = "dashboard"
            st.rerun()

    st.divider()

    # ======================================================
    # INFORMASI PENTING
    # ======================================================

    st.warning(
        """
**Penting**

Simpan Nomor Permohonan Anda.

Nomor tersebut digunakan untuk:

• Cek Status Permohonan

• Perbaikan Dokumen

• Melihat Hasil Verifikasi
"""
    )

    st.divider()

    # ======================================================
    # KONTAK
    # ======================================================

    st.markdown(
        """
### Informasi

Apabila mengalami kendala,
silakan menghubungi:

**Komisi Pemilihan Umum Kota Bengkulu**

📍 Jl. WR. Supratman No. 01 Kota Bengkulu

☎️ (0736) XXXXXXX

📧 kotabengkulu@kpu.go.id
"""
    )

    st.divider()

    # ======================================================
    # FOOTER
    # ======================================================

    st.markdown(
        """
<div style="text-align:center;color:#666;font-size:14px;">

<b>SITAPEL PDPB 2026</b>

<br>

Sistem Informasi Pelayanan Data Pemilih
secara Berkelanjutan

<br><br>

Komisi Pemilihan Umum Kota Bengkulu

</div>
""",
        unsafe_allow_html=True
    )