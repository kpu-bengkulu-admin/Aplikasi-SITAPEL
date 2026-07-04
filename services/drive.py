# ==========================================================
# SITAPEL v3
# services/drive.py
# Google Drive (OAuth - Streamlit Cloud Ready)
# ==========================================================

import io
import streamlit as st

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload


# ==========================================================
# GET DRIVE SERVICE
# ==========================================================

def get_drive_service():

    credentials = st.session_state.get("google_credentials")

    if not credentials:
        raise Exception("User belum login Google")

    return build(
        "drive",
        "v3",
        credentials=credentials
    )


# ==========================================================
# BUAT FOLDER
# ==========================================================

def buat_folder(nama_folder, parent_id=None):

    service = get_drive_service()

    metadata = {
        "name": nama_folder,
        "mimeType": "application/vnd.google-apps.folder"
    }

    if parent_id:
        metadata["parents"] = [parent_id]

    folder = service.files().create(
        body=metadata,
        fields="id, webViewLink"
    ).execute()

    return folder["id"], folder["webViewLink"]


# ==========================================================
# UPLOAD FILE
# ==========================================================

def upload_file(file, nama_file, folder_id):

    service = get_drive_service()

    file_stream = io.BytesIO(file.read())

    media = MediaIoBaseUpload(
        file_stream,
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
# SET PERMISSION (PUBLIC READ OPTIONAL)
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