# ==========================================================
# SITAPEL v3
# services/drive.py
# Google Drive (Refresh Token)
# ==========================================================

import io

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

from auth.google_refresh import get_credentials


# ==========================================================
# GET DRIVE SERVICE
# ==========================================================

def get_drive_service():
    """
    Membuat Google Drive service menggunakan
    OAuth Refresh Token.
    """

    credentials = get_credentials()

    return build(
        "drive",
        "v3",
        credentials=credentials
    )


# ==========================================================
# BUAT FOLDER
# ==========================================================

def buat_folder(
    nama_folder,
    parent_id=None
):

    service = get_drive_service()

    # gunakan folder induk dari secrets jika tidak dikirim
    if parent_id is None:
        parent_id = st.secrets["GOOGLE_DRIVE_FOLDER_ID"]

    metadata = {
        "name": nama_folder,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id]
    }

    folder = service.files().create(
        body=metadata,
        fields="id, webViewLink"
    ).execute()

    return folder["id"], folder["webViewLink"]


# ==========================================================
# UPLOAD FILE
# ==========================================================

def upload_file(
    file,
    nama_file,
    folder_id
):

    service = get_drive_service()

    file.seek(0)

    media = MediaIoBaseUpload(
        io.BytesIO(file.read()),
        mimetype=file.type,
        resumable=True
    )

    metadata = {
        "name": nama_file,
        "parents": [folder_id]
    }

    uploaded = service.files().create(
        body=metadata,
        media_body=media,
        fields="id, webViewLink"
    ).execute()

    return uploaded["id"], uploaded["webViewLink"]


# ==========================================================
# SET PUBLIC
# ==========================================================

def set_public(file_id):

    service = get_drive_service()

    permission = {
        "type": "anyone",
        "role": "reader"
    }

    service.permissions().create(
        fileId=file_id,
        body=permission
    ).execute()