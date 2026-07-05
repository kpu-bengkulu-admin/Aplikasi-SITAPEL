# ==========================================================
# SITAPEL v3
# services/submit.py
# Submit Permohonan
# ==========================================================

import streamlit as st

from services.drive import (
    buat_folder,
    upload_file
)

from services.nomor import (
    generate_nomor_permohonan
)

from services.sheets import (
    simpan_ke_sheets
)


# ==========================================================
# MAPPING DOKUMEN
# ==========================================================

UPLOAD_MAPPING = {

    "Pindah Domisili": [

        ("kk_file", "KK"),

        ("ktp_file", "KTP"),

        ("dokumen_file", "Dokumen_Pendukung")

    ],

    "TMS": [

        ("dokumen_file", "Dokumen")

    ],

    "Pemilih Baru": [

        ("kk_file", "KK"),

        ("ktp_file", "KTP"),

        ("dokumen_file", "Dokumen_Pendukung")

    ]

}


# ==========================================================
# UPLOAD DOKUMEN
# ==========================================================

def upload_semua_dokumen(folder_id):

    layanan = st.session_state.layanan

    mapping = UPLOAD_MAPPING.get(
        layanan,
        []
    )

    hasil = {}

    for key, prefix in mapping:

        file = st.session_state.get(key)

        if file is None:
            continue

        file.seek(0)

        nama_file = f"{prefix}_{file.name}"

        file_id, file_link = upload_file(
            file=file,
            nama_file=nama_file,
            folder_id=folder_id
        )

        hasil[key] = {

            "id": file_id,

            "link": file_link

        }

    return hasil


# ==========================================================
# SUBMIT PERMOHONAN
# ==========================================================

def submit_permohonan():

    # ======================================================
    # NOMOR PERMOHONAN
    # ======================================================

    nomor = generate_nomor_permohonan()

    # ======================================================
    # FOLDER DRIVE
    # ======================================================

    folder_id, folder_link = buat_folder(
        nama_folder=nomor
    )

    # ======================================================
    # UPLOAD DOKUMEN
    # ======================================================

    try:

        hasil_upload = upload_semua_dokumen(folder_id)

    except Exception as e:

        raise Exception(
            f"Gagal mengupload dokumen ke Google Drive.\n\n{e}"
        )

    # ======================================================
    # DATA SHEETS
    # ======================================================


    try:

        simpan_ke_sheets(
            nomor_permohonan=nomor,
            folder_link=folder_link
        )

    except Exception as e:

        raise Exception(
            f"Gagal menyimpan data ke Google Sheets.\n\n{e}"
        )


    # ======================================================
    # SESSION
    # ======================================================

    st.session_state["nomor_permohonan"] = nomor

    st.session_state["folder_id"] = folder_id

    return {

        "nomor_permohonan": nomor,

        "folder_link": folder_link

    }