# ==========================================================
# SITAPEL v4
#
# File        : providers/sheets.py
# Status      : FINAL
# Version     : 4.0.0
#
# Python      : 3.14+
# Streamlit   : 1.58+
#
# Google Sheets Provider
#
# ==========================================================

from __future__ import annotations

from datetime import datetime

from typing import Any

from googleapiclient.discovery import build

from auth.credentials import get_google_credentials

from config import SHEETS


# ==========================================================
# SERVICE
# ==========================================================

def get_sheets_service():
    """
    Membuat Google Sheets Service.
    """

    return build(

        "sheets",

        "v4",

        credentials=get_google_credentials(),

        cache_discovery=False,

    )


# ==========================================================
# SPREADSHEET
# ==========================================================

def spreadsheet_id() -> str:
    """
    Mengembalikan Spreadsheet ID.
    """

    return SHEETS.spreadsheet_id


def worksheet_name() -> str:
    """
    Mengembalikan nama worksheet.
    """

    return SHEETS.sheet_name

# ==========================================================
# READ HEADER
# ==========================================================

def read_header() -> list[str]:
    """
    Mengambil header worksheet.
    """

    service = get_sheets_service()

    result = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=spreadsheet_id(),
            range=f"{worksheet_name()}!A1:ZZ1",
        )
        .execute()
    )

    values = result.get("values", [])

    if not values:
        return []

    return values[0]


# ==========================================================
# READ ROWS
# ==========================================================

def read_rows() -> list[list]:
    """
    Mengambil seluruh data tanpa header.
    """

    service = get_sheets_service()

    result = (

        service.spreadsheets()

        .values()

        .get(

            spreadsheetId=spreadsheet_id(),

            range=worksheet_name(),

        )

        .execute()

    )

    values = result.get(

        "values",

        [],

    )

    if len(values) <= 1:

        return []

    return values[1:]


# ==========================================================
# READ DICT
# ==========================================================

def read_dict() -> list[dict[str, Any]]:
    """
    Mengubah seluruh data menjadi list dictionary.
    """

    header = read_header()

    rows = read_rows()

    data = []

    for row in rows:

        while len(row) < len(header):

            row.append("")

        data.append(

            dict(

                zip(

                    header,

                    row,

                )

            )

        )

    return data

# ==========================================================
# APPEND ROW
# ==========================================================

def append_row(
    values: list,
) -> bool:
    """
    Menambahkan satu baris data
    ke bagian akhir worksheet.
    """

    service = get_sheets_service()

    service.spreadsheets().values().append(

        spreadsheetId=spreadsheet_id(),

        range=worksheet_name(),

        valueInputOption="USER_ENTERED",

        insertDataOption="INSERT_ROWS",

        body={

            "values": [

                values

            ]

        },

    ).execute()

    return True


# ==========================================================
# UPDATE ROW
# ==========================================================

def update_row(
    row_number: int,
    values: list,
) -> bool:
    """
    Memperbarui satu baris data.

    row_number mengikuti nomor
    baris asli pada Google Sheet.
    """

    service = get_sheets_service()

    last_column = chr(

        64 + len(values)

    )

    target_range = (

        f"{worksheet_name()}!"

        f"A{row_number}:"

        f"{last_column}{row_number}"

    )

    service.spreadsheets().values().update(

        spreadsheetId=spreadsheet_id(),

        range=target_range,

        valueInputOption="USER_ENTERED",

        body={

            "values": [

                values

            ]

        },

    ).execute()

    return True

# ==========================================================
# UPDATE STATUS PERMOHONAN
# ==========================================================

def update_status_permohonan(
    nomor_permohonan: str,
    status: str,
    catatan_admin: str = "",
    link_surat: str = ""
) -> bool:
    """
    Memperbarui status permohonan
    berdasarkan Nomor Permohonan.
    """

    row_number = find_row_number(
        "Nomor Permohonan",
        nomor_permohonan
    )

    if row_number is None:

        return False

    record = find_by(
        "Nomor Permohonan",
        nomor_permohonan
    )

    if record is None:

        return False

    values = [

        record.get("ID", ""),
        record.get("Nomor Permohonan", ""),
        record.get("Tanggal", ""),
        record.get("Jam", ""),
        record.get("Tahun", ""),
        record.get("Bulan", ""),

        # Status baru
        status,

        record.get("Jenis Layanan", ""),
        record.get("Nama Pemohon", ""),
        record.get("WhatsApp", ""),
        record.get("Email", ""),
        record.get("Nama Diajukan", ""),
        record.get("Anggota Keluarga", ""),
        record.get("Kecamatan", ""),
        record.get("Kelurahan", ""),
        record.get("Alamat Baru", ""),
        record.get("Kategori TMS", ""),
        record.get("Sudah Memiliki KTP-el", ""),
        record.get("Keterangan Pemohon", ""),

        # Kolom Admin
        catatan_admin,
        datetime.now().strftime("%d-%m-%Y %H:%M"),
        link_surat,

        record.get("Link Folder Drive", "")

    ]

    return update_row(
        row_number,
        values
    )


# ==========================================================
# DELETE ROW
# ==========================================================

def delete_row(
    row_number: int,
) -> bool:
    """
    Menghapus satu baris
    menggunakan Google Sheets API.
    """

    service = get_sheets_service()

    spreadsheet = (

        service.spreadsheets()

        .get(

            spreadsheetId=spreadsheet_id(),

        )

        .execute()

    )

    sheet_id = spreadsheet["sheets"][0]["properties"]["sheetId"]

    body = {

        "requests": [

            {

                "deleteDimension": {

                    "range": {

                        "sheetId": sheet_id,

                        "dimension": "ROWS",

                        "startIndex": row_number - 1,

                        "endIndex": row_number,

                    }

                }

            }

        ]

    }

    service.spreadsheets().batchUpdate(

        spreadsheetId=spreadsheet_id(),

        body=body,

    ).execute()

    return True

# ==========================================================
# COLUMN LETTER
# ==========================================================

def column_letter(column_number: int) -> str:
    """
    Mengubah nomor kolom menjadi
    format Excel.

    Contoh:

    1  -> A
    26 -> Z
    27 -> AA
    """

    result = ""

    while column_number > 0:

        column_number, remainder = divmod(

            column_number - 1,

            26,

        )

        result = chr(

            65 + remainder

        ) + result

    return result


# ==========================================================
# GET COLUMN
# ==========================================================

def get_column(
    column_name: str,
) -> list[str]:
    """
    Mengambil seluruh isi
    satu kolom berdasarkan header.
    """

    header = read_header()

    if column_name not in header:

        raise ValueError(

            f"Kolom '{column_name}' tidak ditemukan."

        )

    index = header.index(

        column_name

    )

    rows = read_rows()

    values = []

    for row in rows:

        if len(row) > index:

            values.append(

                row[index]

            )

        else:

            values.append("")

    return values


# ==========================================================
# FIND BY
# ==========================================================

def find_by(
    column_name: str,
    value: str,
) -> dict | None:
    """
    Mencari satu record berdasarkan
    nama kolom.
    """

    records = read_dict()

    for record in records:

        if str(

            record.get(

                column_name,

                "",

            )

        ).strip() == str(value).strip():

            return record

    return None


# ==========================================================
# FIND ROW NUMBER
# ==========================================================

def find_row_number(
    column_name: str,
    value: str,
) -> int | None:
    """
    Mengembalikan nomor baris
    Google Sheet.
    """

    records = read_dict()

    for index, record in enumerate(

        records,

        start=2,

    ):

        if str(

            record.get(

                column_name,

                "",

            )

        ).strip() == str(value).strip():

            return index

    return None


# ==========================================================
# RECORD EXISTS
# ==========================================================

def record_exists(
    column_name: str,
    value: str,
) -> bool:
    """
    Mengecek apakah data tersedia.
    """

    return (

        find_by(

            column_name,

            value,

        )

        is not None

    )


# ==========================================================
# GET NEXT ID
# ==========================================================

def get_next_id() -> int:
    """
    Menghasilkan ID berikutnya.

    Berdasarkan kolom ID.
    """

    ids = get_column(

        "ID"

    )

    numbers = []

    for item in ids:

        try:

            numbers.append(

                int(item)

            )

        except Exception:

            pass

    if not numbers:

        return 1

    return max(

        numbers

    ) + 1

# ==========================================================
# GENERATE NOMOR PERMOHONAN
# ==========================================================

def generate_nomor_permohonan() -> str:
    """
    Format:
    SITAPEL-2026-000001
    """

    nomor = get_next_id()

    tahun = datetime.now().year

    return f"SITAPEL-{tahun}-{nomor:06d}"


# ==========================================================
# SIMPAN PERMOHONAN
# ==========================================================

def simpan_permohonan(data: dict) -> bool:
    """
    Menyimpan satu permohonan ke Google Sheet.
    """

    values = [

        data["ID"],
        data["Nomor Permohonan"],
        data["Tanggal"],
        data["Jam"],
        data["Tahun"],
        data["Bulan"],
        data["Status"],
        data["Jenis Layanan"],
        data["Nama Pemohon"],
        data["WhatsApp"],
        data["Email"],
        data["Nama Diajukan"],
        data["Anggota Keluarga"],
        data["Kecamatan"],
        data["Kelurahan"],
        data["Alamat Baru"],
        data["Kategori TMS"],
        data["Sudah Memiliki KTP-el"],
        data["Keterangan Pemohon"],
        data["Catatan Admin"],
        data["Tanggal Verifikasi"],
        data["Link Surat"],
        data["Link Folder Drive"]

    ]

    return append_row(values)


# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "get_sheets_service",

    "spreadsheet_id",

    "worksheet_name",

    "read_header",

    "read_rows",

    "read_dict",

    "append_row",

    "update_row",

    "delete_row",

    "column_letter",

    "get_column",

    "find_by",

    "find_row_number",

    "record_exists",

    "get_next_id",

    "generate_nomor_permohonan",

    "simpan_permohonan",

]