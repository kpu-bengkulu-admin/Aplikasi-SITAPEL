# ==========================================================
# SITAPEL v4
#
# File        : services/submit.py
# Status      : FINAL
# Version     : 4.0.0
#
# Python      : 3.14+
# Streamlit   : 1.58+
#
# Description :
# Submit Service
#
# Mengelola seluruh proses permohonan:
#
# - Generate Nomor
# - Upload Lampiran
# - Simpan ke Google Sheets
#
# ==========================================================


from providers.drive import (
    create_folder,
    upload_to_folder,
    delete_folder,
)

from __future__ import annotations

from datetime import datetime

from providers.drive import (
    upload_file,
)

from providers.sheets import (
    append_row,
)

from services.nomor import (
    generate_nomor,
)

# ==========================================================
# STATUS
# ==========================================================

STATUS_DIPROSES = "Diproses"

# ==========================================================
# FILE
# ==========================================================

FILE_KTP = "KTP"

FILE_KK = "KK"

FILE_PENDUKUNG = "Dokumen Pendukung"

# ==========================================================
# DATE
# ==========================================================

def now_string() -> str:
    """
    Format tanggal penyimpanan.

    Contoh:

    08-07-2026 13:45:22
    """

    return datetime.now().strftime(

        "%d-%m-%Y %H:%M:%S"

    )

# ==========================================================
# UPLOAD ATTACHMENT
# ==========================================================

def upload_attachment(
    *,
    file,
    nomor: str,
    prefix: str,
) -> dict:
    """
    Upload satu lampiran ke Google Drive.

    Return
    ------
    {
        "id": "...",
        "name": "...",
        "webViewLink": "...",
        "webContentLink": "..."
    }
    """

    if file is None:

        return {}

    filename = getattr(file, "name", "file")

    extension = ""

    if "." in filename:

        extension = "." + filename.split(".")[-1].lower()

    drive_filename = (

        f"{nomor}"

        f"_{prefix}"

        f"{extension}"

    )

    return upload_file(

        file=file,

        filename=drive_filename,

    )


# ==========================================================
# KTP
# ==========================================================

def upload_ktp(
    nomor: str,
    file,
) -> dict:
    """
    Upload file KTP.
    """

    return upload_attachment(

        nomor=nomor,

        file=file,

        prefix="KTP",

    )


# ==========================================================
# KK
# ==========================================================

def upload_kk(
    nomor: str,
    file,
) -> dict:
    """
    Upload file KK.
    """

    return upload_attachment(

        nomor=nomor,

        file=file,

        prefix="KK",

    )


# ==========================================================
# DOKUMEN PENDUKUNG
# ==========================================================

def upload_pendukung(
    nomor: str,
    file,
) -> dict:
    """
    Upload dokumen pendukung.
    """

    return upload_attachment(

        nomor=nomor,

        file=file,

        prefix="PENDUKUNG",

    )


# ==========================================================
# MULTI UPLOAD
# ==========================================================

def upload_documents(
    *,
    nomor: str,
    ktp,
    kk,
    pendukung=None,
) -> dict:
    """
    Upload seluruh lampiran.

    Return
    ------
    {
        "ktp": {...},
        "kk": {...},
        "pendukung": {...}
    }
    """

    return {

        "ktp": upload_ktp(

            nomor,

            ktp,

        ),

        "kk": upload_kk(

            nomor,

            kk,

        ),

        "pendukung": upload_pendukung(

            nomor,

            pendukung,

        )

        if pendukung

        else {},

    }

# ==========================================================
# DATE
# ==========================================================

def current_date() -> str:
    """
    Tanggal hari ini.
    """

    return datetime.now().strftime(

        "%d-%m-%Y"

    )


def current_time() -> str:
    """
    Jam saat ini.
    """

    return datetime.now().strftime(

        "%H:%M:%S"

    )


def current_year() -> str:
    """
    Tahun.
    """

    return datetime.now().strftime(

        "%Y"

    )


def current_month() -> str:
    """
    Nama bulan Indonesia.
    """

    bulan = [

        "Januari",

        "Februari",

        "Maret",

        "April",

        "Mei",

        "Juni",

        "Juli",

        "Agustus",

        "September",

        "Oktober",

        "November",

        "Desember",

    ]

    return bulan[

        datetime.now().month - 1

    ]


# ==========================================================
# BUILD ROW
# ==========================================================

def build_row(
    *,
    id: int,
    nomor: str,
    folder_link: str,
    form_data: dict,
) -> list:
    """
    Menyusun satu baris data
    sesuai struktur Google Sheet.
    """

    return [

        id,

        nomor,

        current_date(),

        current_time(),

        current_year(),

        current_month(),

        STATUS_DIPROSES,

        form_data.get(

            "jenis_layanan",

            "",

        ),

        form_data.get(

            "nama_pemohon",

            "",

        ),

        form_data.get(

            "whatsapp",

            "",

        ),

        form_data.get(

            "email",

            "",

        ),

        form_data.get(

            "nama_diajukan",

            "",

        ),

        form_data.get(

            "anggota_keluarga",

            "",

        ),

        form_data.get(

            "kecamatan",

            "",

        ),

        form_data.get(

            "kelurahan",

            "",

        ),

        form_data.get(

            "alamat_baru",

            "",

        ),

        form_data.get(

            "kategori_tms",

            "",

        ),

        form_data.get(

            "sudah_memiliki_ktpel",

            "",

        ),

        form_data.get(

            "keterangan_pemohon",

            "",

        ),

        "",

        "",

        "",

        folder_link,

    ]

# ==========================================================
# SUBMIT
# ==========================================================

def submit_permohonan(
    *,
    form_data: dict,
    file_ktp,
    file_kk,
    file_pendukung=None,
) -> dict:
    """
    Submit permohonan baru.
    """

    from providers.sheets import get_next_id

    folder = None

    try:

        # ==================================================
        # ID
        # ==================================================

        id_permohonan = get_next_id()

        # ==================================================
        # NOMOR
        # ==================================================

        nomor = generate_nomor()

        # ==================================================
        # CREATE FOLDER
        # ==================================================

        folder = create_folder(

            nomor,

        )

        folder_id = folder["id"]

        folder_link = folder["webViewLink"]

        # ==================================================
        # KTP
        # ==================================================

        if file_ktp:

            upload_to_folder(

                file=file_ktp,

                folder_id=folder_id,

                filename="KTP",

            )

        # ==================================================
        # KK
        # ==================================================

        if file_kk:

            upload_to_folder(

                file=file_kk,

                folder_id=folder_id,

                filename="KK",

            )

        # ==================================================
        # PENDUKUNG
        # ==================================================

        if file_pendukung:

            upload_to_folder(

                file=file_pendukung,

                folder_id=folder_id,

                filename="Pendukung",

            )

        # ==================================================
        # BUILD ROW
        # ==================================================

        row = build_row(

            id=id_permohonan,

            nomor=nomor,

            folder_link=folder_link,

            form_data=form_data,

        )

        # ==================================================
        # SAVE SHEET
        # ==================================================

        append_row(

            row,

        )

        return {

            "success": True,

            "nomor": nomor,

            "status": STATUS_DIPROSES,

            "folder": folder_link,

        }

    except Exception:

        if folder is not None:

            try:

                delete_folder(

                    folder["id"]

                )

            except Exception:

                pass

        raise

# ==========================================================
# VALIDATION
# ==========================================================

REQUIRED_FIELDS = [

    "jenis_layanan",

    "nama_pemohon",

    "whatsapp",

    "nama_diajukan",

    "kecamatan",

    "kelurahan",

]


def validate_form(
    form_data: dict,
) -> None:
    """
    Validasi data sebelum diproses.
    """

    for field in REQUIRED_FIELDS:

        value = form_data.get(field)

        if value is None:

            raise ValueError(

                f"Field '{field}' wajib diisi."

            )

        if isinstance(value, str):

            if not value.strip():

                raise ValueError(

                    f"Field '{field}' wajib diisi."

                )


# ==========================================================
# SUBMIT WRAPPER
# ==========================================================

def process_submission(
    *,
    form_data: dict,
    file_ktp,
    file_kk,
    file_pendukung=None,
) -> dict:
    """
    Entry point utama aplikasi.

    Digunakan oleh pages/permohonan.py
    """

    validate_form(

        form_data,

    )

    return submit_permohonan(

        form_data=form_data,

        file_ktp=file_ktp,

        file_kk=file_kk,

        file_pendukung=file_pendukung,

    )


# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "process_submission",

    "submit_permohonan",

    "validate_form",

    "build_row",

    "upload_attachment",

    "upload_documents",

]

