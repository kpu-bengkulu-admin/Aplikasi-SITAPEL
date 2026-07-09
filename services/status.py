# ==========================================================
# SITAPEL v4
#
# File        : services/status.py
# Status      : FINAL
# Version     : 4.0.0
#
# Python      : 3.14+
# Streamlit   : 1.58+
#
# Description :
# Layanan Status Permohonan
#
# ==========================================================

from __future__ import annotations

from providers.sheets import (
    find_by,
    find_row_number,
    record_exists,
)

# ==========================================================
# COLUMN
# ==========================================================

COLUMN_NOMOR = "Nomor Permohonan"

COLUMN_STATUS = "Status"

COLUMN_TANGGAL = "Tanggal"

COLUMN_NAMA = "Nama"

COLUMN_NIK = "NIK"

COLUMN_KETERANGAN = "Keterangan"

# ==========================================================
# EXISTS
# ==========================================================

def permohonan_exists(
    nomor: str,
) -> bool:
    """
    Mengecek apakah nomor permohonan tersedia.
    """

    return record_exists(

        COLUMN_NOMOR,

        nomor,

    )


# ==========================================================
# GET
# ==========================================================

def get_permohonan(
    nomor: str,
) -> dict | None:
    """
    Mengambil satu data permohonan.
    """

    return find_by(

        COLUMN_NOMOR,

        nomor,

    )


# ==========================================================
# ROW
# ==========================================================

def get_row_number(
    nomor: str,
) -> int | None:
    """
    Mengambil nomor baris pada spreadsheet.
    """

    return find_row_number(

        COLUMN_NOMOR,

        nomor,

    )

# ==========================================================
# STATUS
# ==========================================================

def get_status(
    nomor: str,
) -> str | None:
    """
    Mengambil status permohonan.
    """

    data = get_permohonan(nomor)

    if data is None:

        return None

    return data.get(

        COLUMN_STATUS,

        "",

    )


# ==========================================================
# KETERANGAN
# ==========================================================

def get_keterangan(
    nomor: str,
) -> str:
    """
    Mengambil keterangan permohonan.
    """

    data = get_permohonan(nomor)

    if data is None:

        return ""

    return data.get(

        COLUMN_KETERANGAN,

        "",

    )


# ==========================================================
# NAMA
# ==========================================================

def get_nama(
    nomor: str,
) -> str:
    """
    Mengambil nama pemohon.
    """

    data = get_permohonan(nomor)

    if data is None:

        return ""

    return data.get(

        COLUMN_NAMA,

        "",

    )


# ==========================================================
# NIK
# ==========================================================

def get_nik(
    nomor: str,
) -> str:
    """
    Mengambil NIK pemohon.
    """

    data = get_permohonan(nomor)

    if data is None:

        return ""

    return data.get(

        COLUMN_NIK,

        "",

    )


# ==========================================================
# TANGGAL
# ==========================================================

def get_tanggal(
    nomor: str,
) -> str:
    """
    Mengambil tanggal permohonan.
    """

    data = get_permohonan(nomor)

    if data is None:

        return ""

    return data.get(

        COLUMN_TANGGAL,

        "",

    )


# ==========================================================
# STATUS CHECK
# ==========================================================

def is_diproses(
    nomor: str,
) -> bool:
    """
    Status masih diproses.
    """

    status = get_status(nomor)

    if status is None:

        return False

    return status.strip().lower() == "diproses"


def is_disetujui(
    nomor: str,
) -> bool:
    """
    Status disetujui.
    """

    status = get_status(nomor)

    if status is None:

        return False

    return status.strip().lower() == "disetujui"


def is_ditolak(
    nomor: str,
) -> bool:
    """
    Status ditolak.
    """

    status = get_status(nomor)

    if status is None:

        return False

    return status.strip().lower() == "ditolak"


def is_selesai(
    nomor: str,
) -> bool:
    """
    Status selesai.
    """

    status = get_status(nomor)

    if status is None:

        return False

    return status.strip().lower() == "selesai"


# ==========================================================
# RESULT
# ==========================================================

def get_status_result(
    nomor: str,
) -> dict | None:
    """
    Mengembalikan ringkasan status permohonan
    untuk halaman Cek Status.
    """

    data = get_permohonan(nomor)

    if data is None:

        return None

    return {

        "nomor": nomor,

        "tanggal": data.get(

            COLUMN_TANGGAL,

            "",

        ),

        "nama": data.get(

            COLUMN_NAMA,

            "",

        ),

        "nik": data.get(

            COLUMN_NIK,

            "",

        ),

        "status": data.get(

            COLUMN_STATUS,

            "",

        ),

        "keterangan": data.get(

            COLUMN_KETERANGAN,

            "",

        ),

    }

# ==========================================================
# UPDATE STATUS
# ==========================================================

from providers.sheets import (
    read_header,
    update_row,
)


def update_status(
    nomor: str,
    *,
    status: str,
    keterangan: str = "",
) -> bool:
    """
    Memperbarui status permohonan.
    """

    row_number = get_row_number(nomor)

    if row_number is None:

        return False

    data = get_permohonan(nomor)

    if data is None:

        return False

    data[COLUMN_STATUS] = status

    data[COLUMN_KETERANGAN] = keterangan

    header = read_header()

    values = [

        data.get(col, "")

        for col in header

    ]

    return update_row(

        row_number,

        values,

    )


# ==========================================================
# APPROVE
# ==========================================================

def approve_permohonan(
    nomor: str,
    *,
    keterangan: str = "",
) -> bool:
    """
    Mengubah status menjadi Disetujui.
    """

    return update_status(

        nomor,

        status="Disetujui",

        keterangan=keterangan,

    )


# ==========================================================
# REJECT
# ==========================================================

def reject_permohonan(
    nomor: str,
    *,
    keterangan: str,
) -> bool:
    """
    Mengubah status menjadi Ditolak.
    """

    return update_status(

        nomor,

        status="Ditolak",

        keterangan=keterangan,

    )


# ==========================================================
# FINISH
# ==========================================================

def finish_permohonan(
    nomor: str,
    *,
    keterangan: str = "",
) -> bool:
    """
    Mengubah status menjadi Selesai.
    """

    return update_status(

        nomor,

        status="Selesai",

        keterangan=keterangan,

    )


# ==========================================================
# PROCESS
# ==========================================================

def process_permohonan(
    nomor: str,
    *,
    keterangan: str = "",
) -> bool:
    """
    Mengubah status menjadi Diproses.
    """

    return update_status(

        nomor,

        status="Diproses",

        keterangan=keterangan,

    )


# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "permohonan_exists",

    "get_permohonan",

    "get_row_number",

    "get_status",

    "get_status_result",

    "get_keterangan",

    "get_nama",

    "get_nik",

    "get_tanggal",

    "is_diproses",

    "is_disetujui",

    "is_ditolak",

    "is_selesai",

    "update_status",

    "approve_permohonan",

    "reject_permohonan",

    "finish_permohonan",

    "process_permohonan",

]