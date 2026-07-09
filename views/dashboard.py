# ==========================================================
# SITAPEL PDPB 2026
# views/dashboard.py
# BAGIAN 1
# ==========================================================

import os
import streamlit as st


# ==========================================================
# DASHBOARD
# ==========================================================

def show_dashboard():

    # ======================================================
    # HEADER
    # ======================================================

    col_logo, col_title = st.columns([1, 5])

    with col_logo:

        logo_path = "assets/logo_kpu.png"

        if os.path.exists(logo_path):

            st.image(
                logo_path,
                width=150
            )

    with col_title:

        st.title(
            "SITAPEL KPU KOTA BENGKULU"
        )

        st.subheader(
            "Pemutakhiran Data Pemilih "
            "Berkelanjutan (PDPB) 2026"
        )

    st.divider()

    # ======================================================
    # HERO
    # ======================================================

    st.info(
        """
### Selamat Datang di SITAPEL

SITAPEL merupakan layanan digital KPU Kota Bengkulu
yang digunakan masyarakat Kota Bengkulu untuk mengajukan
permohonan pelayanan Pemutakhiran Data Pemilih
Berkelanjutan (PDPB) Tahun 2026.

Silakan memilih salah satu jenis layanan
sesuai kebutuhan Anda.
"""
    )

    st.write("")

    # ======================================================
    # ALUR PELAYANAN
    # ======================================================

    st.subheader(
        "🔄 Alur Pelayanan"
    )

    langkah = [

        "1️⃣ Pilih Jenis Layanan",

        "2️⃣ Isi Data Pemohon",

        "3️⃣ Upload Dokumen Persyaratan",

        "4️⃣ Verifikasi Oleh Petugas KPU",

        "5️⃣ Permohonan Selesai"

    ]

    for item in langkah:

        st.success(item)

    st.write("")

    # ======================================================
    # PILIH JENIS LAYANAN
    # ======================================================

    st.subheader(
        "📌 Pilih Jenis Layanan"
    )

    st.write(
        """
Silakan memilih salah satu jenis layanan
yang tersedia di bawah ini.
"""
    )

    st.write("")

    # ======================================================
    # LAYANAN 1
    # ======================================================

    with st.container():

        st.markdown("### 🏠 Pindah Domisili / Tempat Tinggal")

        st.write(
            """
Pelayanan bagi Masyarakat yang berpindah
domisili atau tempat tinggal dalam wilayah
Kota Bengkulu.
"""
        )

        if st.button(
            "Ajukan Permohonan",
            key="layanan_pindah",
            use_container_width=True
        ):

            st.session_state.step = 1

            st.session_state["jenis_layanan"] = (
                "Pindah Domisili/Tempat Tinggal"
            )

            st.session_state["page"] = "permohonan"

            st.rerun()

    st.divider()

    # ======================================================
    # LAYANAN 2
    # ======================================================

    with st.container():

        st.markdown(
            "### 🆕 Pemilih Baru / Belum Terdaftar Dalam DPT"
        )

        st.write(
            """
Pelayanan bagi pemilih pemula,
pemilih yang belum terdaftar dalam DPT,
serta pensiunan TNI/POLRI yang telah
memenuhi syarat sebagai pemilih.
"""
        )

        if st.button(
            "Ajukan Permohonan",
            key="layanan_baru",
            use_container_width=True
        ):

            st.session_state.step = 1

            st.session_state["jenis_layanan"] = (
                "Pemilih Baru/Belum Terdaftar Dalam DPT"
            )

            st.session_state["page"] = "permohonan"

            st.rerun()

    st.divider()

    # ======================================================
    # LAYANAN 3
    # ======================================================

    with st.container():

        st.markdown(
            "### 📄 Pemilih Tidak Memenuhi Syarat (TMS)"
        )

        st.write(
            """
Pelayanan untuk pemilih yang
sudah tidak memenuhi syarat,
seperti meninggal dunia,
menjadi anggota TNI,
atau menjadi anggota POLRI.
"""
        )

        if st.button(
            "Ajukan Permohonan",
            key="layanan_tms",
            use_container_width=True
        ):

            st.session_state.step = 1

            st.session_state["jenis_layanan"] = (
                "Pemilih Tidak Memenuhi Syarat (TMS)"
            )

            st.session_state["page"] = "permohonan"

            st.rerun()

    st.write("")

    # ======================================================
    # PERSYARATAN UMUM
    # ======================================================

    st.subheader(
        "📂 Persyaratan Umum"
    )

    st.info(
        """
Sebelum mengajukan permohonan, siapkan dokumen berikut:

✅ KTP Elektronik

✅ Kartu Keluarga (KK)

✅ Dokumen pendukung sesuai jenis layanan.
"""
    )

    st.write("")

    # ======================================================
    # PERSYARATAN SETIAP LAYANAN
    # ======================================================

    st.subheader(
        "📋 Persyaratan Berdasarkan Jenis Layanan"
    )

    with st.expander(
        "🏠 Pindah Domisili / Tempat Tinggal",
        expanded=False
    ):

        st.markdown(
            """
**Persyaratan:**

- KTP Elektronik
- Kartu Keluarga
- Alamat domisili baru di Kota Bengkulu

**Keterangan**

Digunakan bagi masyarakat yang pindah
domisili atau tempat tinggal dalam
wilayah Kota Bengkulu.
"""
        )

    with st.expander(
        "🆕 Pemilih Baru / Belum Terdaftar Dalam DPT",
        expanded=False
    ):

        st.markdown(
            """
**Persyaratan:**

- Kartu Keluarga
- KTP Elektronik (apabila sudah memiliki)

**Kategori:**

- Pemilih Pemula
- Belum terdaftar dalam DPT
- Pensiunan TNI
- Pensiunan POLRI
"""
        )

    with st.expander(
        "📄 Pemilih Tidak Memenuhi Syarat (TMS)",
        expanded=False
    ):

        st.markdown(
            """
**Persyaratan:**

- KTP Elektronik
- Kartu Keluarga
- Dokumen pendukung sesuai kategori

**Kategori TMS:**

- Meninggal Dunia
- Menjadi Anggota TNI
- Menjadi Anggota POLRI
"""
        )

    st.write("")

    # ==========================================================
    # PERSYARATAN UMUM
    # ==========================================================

    st.write("")

    st.subheader("📂 Persyaratan Umum")

    st.info(
        """
Sebelum mengajukan permohonan, siapkan dokumen berikut:

✅ KTP Elektronik

✅ Kartu Keluarga (KK)

✅ Dokumen pendukung sesuai jenis layanan yang dipilih.
"""
    )

    st.write("")

    # ==========================================================
    # CEK STATUS PERMOHONAN
    # ==========================================================

    st.subheader("🔎 Cek Status Permohonan")

    nomor = st.text_input(
        "Nomor Permohonan",
        placeholder="Contoh : SITAPEL-2026-000001"
    )

    if st.button(
        "Cek Status",
        use_container_width=True
    ):

        if nomor.strip() == "":

            st.warning(
                "Silakan masukkan Nomor Permohonan."
            )

        else:

            st.session_state["nomor_permohonan"] = nomor.strip()

            st.session_state["page"] = "cek_status"

            st.rerun()

    st.write("")

    # ==========================================================
    # FOOTER
    # ==========================================================

    st.markdown(
        """
        ---
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align:center;padding:20px;">

        <h4 style="color:#0b4da2;margin-bottom:5px;">
        KOMISI PEMILIHAN UMUM KOTA BENGKULU
        </h4>

        <b>SITAPEL PDPB 2026</b><br>

        Sistem Informasi Pelayanan Data Pemilih
        secara Berkelanjutan

        <br><br>

        © 2026 KPU Kota Bengkulu

        </div>
        """,
        unsafe_allow_html=True
    )

