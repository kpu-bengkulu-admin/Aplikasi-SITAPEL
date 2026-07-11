# ==========================================================
# SITAPEL PDPB 2026
# views/dashboard.py
# BAGIAN 1 - UI REDESIGN
# ==========================================================

import os
import streamlit as st
from providers.sheets import find_by


# ==========================================================
# DASHBOARD
# ==========================================================

def show_dashboard():

    # ======================================================
    # CUSTOM PAGE POSITION
    # ======================================================

    st.markdown(
        """
        <style>

        .block-container {
            padding-top: 0rem;
            padding-bottom: 1rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>

        /* BUTTON AJUKAN PERMOHONAN */
        div.stButton > button {

            background-color:#7A0019;
            color:white;

            border-radius:12px;
            border:none;

            height:45px;

            font-size:16px;
            font-weight:600;

            transition:0.3s;

        }


        div.stButton > button:hover {

            background-color:#D4AF37;
            color:#7A0019;

            border:none;

        }


        </style>
        """,
        unsafe_allow_html=True
    )

    # ======================================================
    # HEADER HERO KPU STYLE
    # ======================================================

    col_logo, col_title = st.columns(
        [1, 5],
        vertical_alignment="center"
    )


    with col_logo:

        logo_path = "assets/logo_kpu.png"

        if os.path.exists(logo_path):

            st.image(
                logo_path,
                width=130
            )


    with col_title:

        st.markdown(
            """
            <h1 style="
                color:#7A0019;
                margin-bottom:0px;
                font-size:60px;
            ">
            SITAPEL KPU KOTA BENGKULU
            </h1>

            <p style="
                color:#D4AF37;
                font-size:30px;
                font-weight:600;
            ">
            Pemutakhiran Data Pemilih Berkelanjutan (PDPB) 2026
            </p>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        """
        <hr style="
        border:1px solid #D4AF37;
        margin-top:10px;
        ">
        """,
        unsafe_allow_html=True
    )



    # ======================================================
    # HERO SECTION
    # ======================================================


    st.markdown(
        """
        <div style="
            background:linear-gradient(
                135deg,
                #7A0019,
                #4A0010
            );
            padding:10px;
            border-radius:18px;
            color:white;
            margin-bottom:15px;
        ">

        <h2 style="
            color:white;
            margin-bottom:10px;
        ">
        Selamat Datang di SITAPEL
        </h2>


        <p style="
            font-size:17px;
            line-height:1.7;
        ">
        Sistem Pelayanan digital KPU Kota Bengkulu
        untuk masyarakat Kota Bengkulu dalam pengajuan permohonan
        Pemutakhiran Data Pemilih Berkelanjutan (PDPB)
        Tahun 2026.
        </p>


        <p style="
            color:#FFD700;
            font-weight:bold;
            font-size:16px;
        ">
        Cepat • Mudah • Transparan
        </p>


        </div>
        """,
        unsafe_allow_html=True
    )



    # ======================================================
    # ALUR PELAYANAN
    # ======================================================


    st.subheader(
        "🔄 Alur Pelayanan"
    )


    langkah = [

        (
            "1",
            "Pilih Layanan",
            "Pilih jenis permohonan sesuai kebutuhan"
        ),

        (
            "2",
            "Isi Data Pemohon",
            "Lengkapi informasi pemohon"
        ),

        (
            "3",
            "Upload Dokumen",
            "Unggah dokumen persyaratan"
        ),

        (
            "4",
            "Verifikasi",
            "Petugas KPU melakukan pemeriksaan"
        ),

        (
            "5",
            "Selesai",
            "Permohonan berhasil diproses"
        )

    ]


    cols = st.columns(5)


    for col, item in zip(cols, langkah):

        nomor, judul, ket = item


        with col:

            st.markdown(
                f"""
                <div style="
                    background:#ffffff;
                    border:2px solid #D4AF37;
                    border-radius:5px;
                    padding:5px;
                    text-align:center;
                    min-height:80px;
                ">


                <div style="
                    background:#7A0019;
                    color:white;
                    width:40px;
                    height:40px;
                    border-radius:50%;
                    margin:auto;
                    line-height:40px;
                    font-size:20px;
                    font-weight:bold;
                ">
                {nomor}
                </div>


                <h4 style="
                    color:#7A0019;
                    margin-top:15px;
                ">
                {judul}
                </h4>


                <p style="
                    font-size:13px;
                    color:#555;
                ">
                {ket}
                </p>


                </div>
                """,
                unsafe_allow_html=True
            )


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
yang tersedia.
"""
    )

    st.write("")


    # ======================================================
    # CARD LAYANAN
    # ======================================================


    layanan_cols = st.columns(3)



    # ======================================================
    # LAYANAN 1
    # ======================================================

    with layanan_cols[0]:

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                padding:25px;
                border-top:6px solid #7A0019;
                min-height:280px;
                box-shadow:0 4px 12px rgba(0,0,0,0.08);
            ">

            <h2 style="
                text-align:center;
            ">
            🏠
            </h2>


            <h3 style="
                text-align:center;
                color:#7A0019;
            ">
            Pindah Domisili
            </h3>


            <p style="
                text-align:center;
                color:#555;
            ">
            Pelayanan bagi masyarakat
            yang berpindah domisili
            atau tempat tinggal dalam
            wilayah Kota Bengkulu.
            </p>


            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


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



    # ======================================================
    # LAYANAN 2
    # ======================================================

    with layanan_cols[1]:

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                padding:25px;
                border-top:6px solid #D4AF37;
                min-height:280px;
                box-shadow:0 4px 12px rgba(0,0,0,0.08);
            ">


            <h2 style="
                text-align:center;
            ">
            🆕
            </h2>


            <h3 style="
                text-align:center;
                color:#7A0019;
            ">
            Pemilih Baru
            </h3>


            <p style="
                text-align:center;
                color:#555;
            ">
            Pelayanan bagi pemilih pemula,
            pemilih yang belum terdaftar
            dalam DPT, serta pensiunan
            TNI/POLRI.
            </p>


            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


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



    # ======================================================
    # LAYANAN 3
    # ======================================================

    with layanan_cols[2]:


        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                padding:25px;
                border-top:6px solid #7A0019;
                min-height:280px;
                box-shadow:0 4px 12px rgba(0,0,0,0.08);
            ">


            <h2 style="
                text-align:center;
            ">
            📄
            </h2>


            <h3 style="
                text-align:center;
                color:#7A0019;
            ">
            Pemilih TMS
            </h3>


            <p style="
                text-align:center;
                color:#555;
            ">
            Pelayanan untuk pemilih
            yang sudah tidak memenuhi
            syarat seperti meninggal dunia,
            TNI, atau POLRI.
            </p>


            </div>
            """,
            unsafe_allow_html=True
        )


        st.write("")


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


    st.markdown(
        """
        <div style="
            background:white;
            border-left:6px solid #D4AF37;
            border-radius:15px;
            padding:25px;
            box-shadow:0 4px 12px rgba(0,0,0,0.08);
        ">

        <h4 style="
            color:#7A0019;
        ">
        Dokumen yang perlu disiapkan:
        </h4>


        <ul style="
            line-height:2;
            font-size:16px;
        ">

        <li>✅ KTP Elektronik</li>

        <li>✅ Kartu Keluarga (KK)</li>

        <li>✅ Dokumen pendukung sesuai jenis layanan</li>

        </ul>


        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")



    # ======================================================
    # PERSYARATAN BERDASARKAN LAYANAN
    # ======================================================


    st.subheader(
        "📋 Persyaratan Berdasarkan Jenis Layanan"
    )



    with st.expander(
        "🏠 Pindah Domisili / Tempat Tinggal"
    ):

        st.markdown(
            """
    ### Persyaratan

    ✅ KTP Elektronik

    ✅ Kartu Keluarga

    ✅ Alamat domisili baru di Kota Bengkulu


    ### Keterangan

    Digunakan bagi masyarakat yang pindah
    domisili atau tempat tinggal dalam
    wilayah Kota Bengkulu.
    """
        )



    with st.expander(
        "🆕 Pemilih Baru / Belum Terdaftar Dalam DPT"
    ):

        st.markdown(
            """
    ### Persyaratan

    ✅ Kartu Keluarga

    ✅ KTP Elektronik (apabila sudah memiliki)


    ### Kategori

    - Pemilih Pemula
    - Belum terdaftar dalam DPT
    - Pensiunan TNI
    - Pensiunan POLRI
    """
        )



    with st.expander(
        "📄 Pemilih Tidak Memenuhi Syarat (TMS)"
    ):

        st.markdown(
            """
    ### Persyaratan

    ✅ KTP Elektronik

    ✅ Kartu Keluarga

    ✅ Dokumen pendukung sesuai kategori


    ### Kategori TMS

    - Meninggal Dunia
    - Menjadi Anggota TNI
    - Menjadi Anggota POLRI
    """
        )



    st.write("")



    # ======================================================
    # CEK STATUS PERMOHONAN
    # ======================================================

    st.subheader(
        "🔎 Cek Status Permohonan"
    )

    nomor = st.text_input(
        "Nomor Permohonan",
        placeholder="Contoh : SITAPEL-2026-000001"
    )

    if st.button(
        "🔍 Cek Status",
        type="primary",
        use_container_width=True
    ):

        if nomor.strip() == "":

            st.warning(
                "Masukkan Nomor Permohonan terlebih dahulu."
            )

        else:

            with st.spinner(
                "🔍 Sedang mencari data permohonan..."
            ):

                st.session_state.hasil_cek = find_by(
                    "Nomor Permohonan",
                    nomor.strip()
                )

    # ======================================================
    # HASIL CEK STATUS
    # ======================================================

    if "hasil_cek" in st.session_state:

        data = st.session_state.hasil_cek

        if data is None:

            st.error(
                "Nomor Permohonan tidak ditemukan."
            )

        else:

            status = data.get(
                "Status",
                "-"
            )

            warna_status = {
                "Menunggu Verifikasi": "🔵",
                "Sedang Diverifikasi": "🟡",
                "Perlu Perbaikan": "🟠",
                "Selesai": "🟢",
                "Ditolak": "🔴"
            }

            icon = warna_status.get(
                status,
                "⚪"
            )

            st.success(
                "Data permohonan ditemukan."
            )

            st.markdown(
                f"""
<div style="
background:#ffffff;
border:1px solid #dbeafe;
border-left:6px solid #2563eb;
border-radius:12px;
padding:20px;
box-shadow:0 2px 10px rgba(0,0,0,.08);
margin:15px 0;
">

<h4 style="margin-top:0;">
📋 Status Permohonan
</h4>

<h3 style="color:#2563eb;">
{icon} {status}
</h3>

<hr>

<b>Nomor Permohonan</b><br>
{data.get("Nomor Permohonan", "-")}

<br><br>

<b>Nama Pemohon</b><br>
{data.get("Nama Pemohon", "-")}

<br><br>

<b>Jenis Layanan</b><br>
{data.get("Jenis Layanan", "-")}

<br><br>

<b>Tanggal Pengajuan</b><br>
{data.get("Tanggal", "-")}

</div>
""",
                unsafe_allow_html=True
            )

            catatan = data.get(
                "Catatan Petugas",
                ""
            )

            st.markdown(
                "#### 📝 Catatan Petugas"
            )

            if catatan:

                st.info(
                    catatan
                )

            else:

                st.info(
                    "Belum ada catatan dari petugas verifikator."
                )

    st.write("")



    # ======================================================
    # FOOTER
    # ======================================================


    st.markdown(
        """
        <hr style="
        border:1px solid #D4AF37;
        ">
        """,
        unsafe_allow_html=True
    )



    st.markdown(
        """
        <div style="
            text-align:center;
            padding:25px;
        ">


        <h3 style="
            color:#7A0019;
            margin-bottom:5px;
        ">
        KOMISI PEMILIHAN UMUM
        KOTA BENGKULU
        </h3>


        <b style="
            color:#D4AF37;
        ">
        SITAPEL PDPB 2026
        </b>


        <p>
        Sistem Informasi Pelayanan Pemutakhiran Data Pemilih
        secara Berkelanjutan
        </p>


        <small>
        ©by.es 2026 KPU Kota Bengkulu
        </small>


        </div>
        """,
        unsafe_allow_html=True
    )
