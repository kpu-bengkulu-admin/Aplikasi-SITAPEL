# ==========================================================
# SITAPEL v4
#
# File        : providers/drive.py
# Status      : FINAL
# Version     : 4.0.0
#
# Python      : 3.14+
# Streamlit   : 1.58+
#
# Google Drive Provider
#
# ==========================================================

from __future__ import annotations

from io import BytesIO

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

from auth.credentials import get_google_credentials

from config import DRIVE


# ==========================================================
# SERVICE
# ==========================================================

def get_drive_service():
    """
    Membuat Google Drive Service.
    """

    return build(

        "drive",

        "v3",

        credentials=get_google_credentials(),

        cache_discovery=False,

    )


# ==========================================================
# ROOT FOLDER
# ==========================================================

def get_root_folder() -> str:
    """
    Folder utama SITAPEL.
    """

    return DRIVE.folder_id

# ==========================================================
# CREATE FOLDER
# ==========================================================

def create_folder(
    folder_name: str,
) -> dict:
    """
    Membuat folder baru
    di dalam folder utama SITAPEL.
    """

    service = get_drive_service()

    metadata = {

        "name": folder_name,

        "mimeType": "application/vnd.google-apps.folder",

        "parents": [

            get_root_folder()

        ],

    }

    folder = (

        service.files()

        .create(

            body=metadata,

            fields="id,name,webViewLink",

            supportsAllDrives=True,

        )

        .execute()

    )

    return folder

# ==========================================================
# UPLOAD TO FOLDER
# ==========================================================

def upload_to_folder(
    *,
    file,
    folder_id: str,
    filename: str,
) -> dict:
    """
    Upload file ke dalam folder Google Drive.

    Parameters
    ----------
    file
        Hasil dari st.file_uploader()

    folder_id
        ID Folder Google Drive

    filename
        Nama file tanpa ekstensi
    """

    service = get_drive_service()

    original_name = getattr(

        file,

        "name",

        "file",

    )

    extension = ""

    if "." in original_name:

        extension = "." + original_name.split(".")[-1].lower()

    drive_filename = (

        filename +

        extension

    )

    file.seek(0)

    media = MediaIoBaseUpload(

        BytesIO(

            file.read()

        ),

        mimetype=file.type,

        resumable=True,

    )

    metadata = {

        "name": drive_filename,

        "parents": [

            folder_id,

        ],

    }

    uploaded = (

        service.files()

        .create(

            body=metadata,

            media_body=media,

            fields=(

                "id,"

                "name,"

                "mimeType,"

                "webViewLink,"

                "webContentLink"

            ),

            supportsAllDrives=True,

        )

        .execute()

    )

    return uploaded


# ==========================================================
# UPLOAD FILE
# ==========================================================

def upload_file(
    *,
    file,
    filename: str,
    folder_id: str | None = None,
) -> dict:
    """
    Wrapper upload file.

    Jika folder_id tidak diberikan,
    maka file diupload ke folder utama.
    """

    if folder_id is None:

        folder_id = get_root_folder()

    return upload_to_folder(

        file=file,

        folder_id=folder_id,

        filename=filename,

    )

# ==========================================================
# DELETE FOLDER
# ==========================================================

def delete_folder(
    folder_id: str,
) -> bool:
    """
    Menghapus folder beserta seluruh isinya
    ke Trash Google Drive.

    Digunakan untuk rollback apabila proses
    submit gagal.
    """

    service = get_drive_service()

    service.files().delete(

        fileId=folder_id,

        supportsAllDrives=True,

    ).execute()

    return True


# ==========================================================
# GET FOLDER LINK
# ==========================================================

def folder_link(
    folder_id: str,
) -> str:
    """
    Menghasilkan URL folder Google Drive.
    """

    return (

        "https://drive.google.com/drive/folders/"

        f"{folder_id}"

    )


# ==========================================================
# GET FILE LINK
# ==========================================================

def file_link(
    file_id: str,
) -> str:
    """
    Menghasilkan URL file Google Drive.
    """

    return (

        "https://drive.google.com/file/d/"

        f"{file_id}"

        "/view"

    )


# ==========================================================
# GET FILE METADATA
# ==========================================================

def get_file(
    file_id: str,
) -> dict:
    """
    Mengambil metadata file.
    """

    service = get_drive_service()

    return (

        service.files()

        .get(

            fileId=file_id,

            fields=(

                "id,"

                "name,"

                "mimeType,"

                "size,"

                "createdTime,"

                "modifiedTime,"

                "webViewLink"

            ),

            supportsAllDrives=True,

        )

        .execute()

    )


# ==========================================================
# LIST FILES
# ==========================================================

def list_files(
    folder_id: str,
) -> list:
    """
    Mengambil seluruh file dalam folder.
    """

    service = get_drive_service()

    result = (

        service.files()

        .list(

            q=f"'{folder_id}' in parents and trashed=false",

            fields="files(id,name,mimeType,webViewLink)",

            supportsAllDrives=True,

            includeItemsFromAllDrives=True,

        )

        .execute()

    )

    return result.get(

        "files",

        [],

    )

# ==========================================================
# UPLOAD PERMOHONAN SITAPEL
# ==========================================================

def upload_folder_permohonan(
    nomor_permohonan: str,
    ktp,
    kk,
    pendukung=None,
) -> str:
    """
    Membuat folder berdasarkan nomor permohonan,
    mengunggah seluruh dokumen, kemudian
    mengembalikan URL folder Google Drive.
    """

    # Membuat folder permohonan
    folder = create_folder(nomor_permohonan)

    folder_id = folder["id"]

    # Upload KTP
    upload_to_folder(
        file=ktp,
        folder_id=folder_id,
        filename="KTP-el",
    )

    # Upload KK
    upload_to_folder(
        file=kk,
        folder_id=folder_id,
        filename="Kartu Keluarga",
    )

    # Upload Dokumen Pendukung (jika ada)
    if pendukung is not None:

        upload_to_folder(
            file=pendukung,
            folder_id=folder_id,
            filename="Dokumen Pendukung",
        )

    return folder_link(folder_id)


# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "get_drive_service",

    "get_root_folder",

    "create_folder",

    "upload_to_folder",

    "upload_file",

    "upload_folder_permohonan",

    "delete_folder",

    "folder_link",

    "file_link",

    "get_file",

    "list_files",

]