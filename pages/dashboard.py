# ==========================================================
# SITAPEL
# Dashboard
# KPU Kota Bengkulu
# ==========================================================

# ================= IMPORT =================
import streamlit as st
import os

# ================= DASHBOARD =================
def show_dashboard():

    # ================= HERO =================

    hero1, hero2 = st.columns(
        [
            1,
            4
        ],
        vertical_alignment="center"
    )

    with hero1:

        if os.path.exists("assets/logo_kpu.png"):

            st.image(
                "assets/logo_kpu.png",
                width=160
            )

    with hero2:

        st.markdown("# 🗳️ SITAPEL")
        st.markdown("### Sistem Informasi Pelayanan")
        st.markdown("### Pemutakhiran Data Pemilih Berkelanjutan")
        st.markdown("**Komisi Pemilihan Umum Kota Bengkulu**")

    st.write("")

    # ================= TOMBOL =================

    b1, b2 = st.columns(2)

    with b1:

        if st.button(
            "📝 AJUKAN PERMOHONAN",
            use_container_width=True
        ):

            st.session_state.page = "permohonan"

            st.rerun()

    with b2:

        if st.button(
            "🔍 CEK STATUS",
            use_container_width=True
        ):

            st.session_state.page = "cek_status"

            st.rerun()

    st.write("")

    # ================= INFO =================

    st.markdown(
        """
        <div class="info-box">

        <h3>
        📢 Informasi
        </h3>

        <p>

        Selamat datang di
        <strong>SITAPEL</strong>.

        Aplikasi ini digunakan untuk
        pengajuan pelayanan
        Pemutakhiran Data Pemilih
        Berkelanjutan (PDPB)
        secara online.

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ================= CSS TIMELINE =================
    st.markdown(
        """
        <style>
            .timeline {
                display: flex;
                justify-content: space-between;
                gap: 20px;
                margin-top: 20px;
                flex-wrap: wrap;
            }

            .timeline-item {
                flex: 1;
                min-width: 150px;
                background: #f8f8f8;
                padding: 15px;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            }

            .timeline-number {
                width: 35px;
                height: 35px;
                background: #7A0019;
                color: white;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 10px auto;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ================= ALUR PELAYANAN =================

    st.write("")

    st.markdown(
        """
        <h2 style="text-align:center;color:#7A0019;">
            Alur Pelayanan
        </h2>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    data = [
        ("1", "Pilih", "Jenis Layanan"),
        ("2", "Isi", "Data Pemohon"),
        ("3", "Upload", "Dokumen"),
        ("4", "Verifikasi", "Oleh Petugas"),
        ("5", "Selesai", "Permohonan"),
    ]

    for col, (no, judul, ket) in zip([c1, c2, c3, c4, c5], data):
        with col:
            st.markdown(
                f"""
                <div class="card" style="text-align:center;min-height:170px;">
                    <div class="timeline-number">{no}</div>
                    <b>{judul}</b>
                    <br>
                    {ket}
                </div>
                """,
                unsafe_allow_html=True
            )

    # ================= JENIS LAYANAN =================

    st.markdown(
        """
        <h2 style="text-align:center;color:#7A0019;">
            Jenis Layanan
        </h2>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        with st.container(border=True):

            st.markdown(
                "<h1 style='text-align:center;'>🏠</h1>",
                unsafe_allow_html=True
            )

            st.markdown(
                "<h4 style='text-align:center;color:#7A0019;'>Pindah Domisili</h4>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div style="text-align:center;">
                Melayani perpindahan pemilih
                ke alamat domisili yang baru.
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.button(
            "Pilih Pindah Domisili",
            key="btn_pindah",
            use_container_width=True
        ):
            st.session_state.layanan = "Pindah Domisili"
            st.session_state.page = "permohonan"
            st.rerun()

    with c2:

        with st.container(border=True):

            st.markdown(
                "<h1 style='text-align:center;'>📄</h1>",
                unsafe_allow_html=True
            )

            st.markdown(
                "<h4 style='text-align:center;color:#7A0019;'>TMS</h4>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div style="text-align:center;">
                Pemilih Tidak Memenuhi Syarat
                (Meninggal, TNI/POLRI,
                Belum 17 Tahun).
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.button(
            "Pilih TMS",
            key="btn_tms",
            use_container_width=True
        ):
            st.session_state.layanan = "TMS"
            st.session_state.page = "permohonan"
            st.rerun()

    with c3:

        with st.container(border=True):

            st.markdown(
                "<h1 style='text-align:center;'>🆕</h1>",
                unsafe_allow_html=True
            )

            st.markdown(
                "<h4 style='text-align:center;color:#7A0019;'>Pemilih Baru</h4>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div style="text-align:center;">
                Melayani masyarakat yang
                belum terdaftar sebagai
                pemilih dan telah memenuhi
                syarat.
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.button(
            "Pilih Pemilih Baru",
            key="btn_baru",
            use_container_width=True
        ):
            st.session_state.layanan = "Pemilih Baru"
            st.session_state.page = "permohonan"
            st.rerun()

    # ================= DOKUMEN =================

    st.markdown(
        """
        <h2 style="
            color:#7A0019;
            text-align:center;
        ">
            Dokumen yang Perlu Disiapkan
        </h2>
        """,
        unsafe_allow_html=True
    )

    info1, info2 = st.columns(2)

    with info1:

        st.info(
            """
📌 **Pindah Domisili**

• Kartu Keluarga terbaru

• KTP seluruh anggota keluarga yang pindah

• Pastikan data terbaca dengan jelas.
"""
        )

        st.info(
            """
📌 **Pemilih Baru**

• Kartu Keluarga

• KTP-el (jika sudah memiliki)

• Dokumen pendukung lainnya apabila diperlukan.
"""
        )

    with info2:

        st.info(
            """
📌 **Pemilih Tidak Memenuhi Syarat (TMS)**

Kategori:

• Meninggal Dunia

• Menjadi Anggota TNI

• Menjadi Anggota POLRI

• Belum berusia 17 Tahun dan belum menikah
"""
        )

        st.success(
            """
✅ Semua dokumen diunggah dalam format:

JPG • JPEG • PNG • PDF

Ukuran maksimum setiap file 10 MB.
"""
        )

    st.write("")
    st.write("")

    # ================= STATISTIK =================

    s1, s2, s3 = st.columns(3)

    with s1:

        st.metric(
            "Jenis Layanan",
            "3"
        )

    with s2:

        st.metric(
            "Status",
            "Online"
        )

    with s3:

        st.metric(
            "Pelayanan",
            "24 Jam"
        )

    st.write("")
    st.write("")

