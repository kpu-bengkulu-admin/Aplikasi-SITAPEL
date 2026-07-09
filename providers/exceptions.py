# ==========================================================
# SITAPEL v4
#
# File        : providers/exceptions.py
# Status      : FINAL
# Version     : 4.0.0
#
# Python      : 3.14+
# Streamlit   : 1.58+
#
# Description :
# Centralized custom exceptions.
#
# ==========================================================

from __future__ import annotations


# ==========================================================
# BASE
# ==========================================================

class SITAPELError(Exception):
    """
    Base exception untuk seluruh aplikasi SITAPEL.
    """
    pass


# ==========================================================
# CONFIG
# ==========================================================

class ConfigurationError(SITAPELError):
    """
    Kesalahan konfigurasi aplikasi.
    """
    pass


# ==========================================================
# CRYPTO
# ==========================================================

class CryptoError(SITAPELError):
    """
    Kesalahan proses enkripsi/dekripsi.
    """
    pass


# ==========================================================
# STORAGE
# ==========================================================

class StorageError(SITAPELError):
    """
    Base exception untuk penyimpanan data.
    """
    pass


class StorageReadError(StorageError):
    """
    Gagal membaca data.
    """
    pass


class StorageWriteError(StorageError):
    """
    Gagal menyimpan data.
    """
    pass


class StorageUpdateError(StorageError):
    """
    Gagal memperbarui data.
    """
    pass


class StorageDeleteError(StorageError):
    """
    Gagal menghapus data.
    """
    pass


# ==========================================================
# OAUTH
# ==========================================================

class OAuthError(SITAPELError):
    """
    Base exception OAuth.
    """
    pass


class OAuthLoginError(OAuthError):
    """
    Login OAuth gagal.
    """
    pass


class OAuthTokenError(OAuthError):
    """
    Token OAuth tidak valid.
    """
    pass


class OAuthRefreshError(OAuthError):
    """
    Refresh Access Token gagal.
    """
    pass


class OAuthTokenNotFound(OAuthError):
    """
    Refresh Token belum tersedia.
    """
    pass


# ==========================================================
# GOOGLE DRIVE
# ==========================================================

class DriveError(SITAPELError):
    """
    Base exception Google Drive.
    """
    pass


class DriveUploadError(DriveError):
    """
    Upload file ke Google Drive gagal.
    """
    pass


class DriveFolderError(DriveError):
    """
    Folder Google Drive tidak ditemukan.
    """
    pass


# ==========================================================
# GOOGLE SHEETS
# ==========================================================

class SheetsError(SITAPELError):
    """
    Base exception Google Sheets.
    """
    pass


class SheetsReadError(SheetsError):
    """
    Membaca Google Sheets gagal.
    """
    pass


class SheetsWriteError(SheetsError):
    """
    Menulis Google Sheets gagal.
    """
    pass


# ==========================================================
# VALIDATION
# ==========================================================

class ValidationError(SITAPELError):
    """
    Validasi data gagal.
    """
    pass


# ==========================================================
# SUBMISSION
# ==========================================================

class SubmissionError(SITAPELError):
    """
    Proses pengajuan gagal.
    """
    pass


# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "SITAPELError",

    "ConfigurationError",

    "CryptoError",

    "StorageError",
    "StorageReadError",
    "StorageWriteError",
    "StorageUpdateError",
    "StorageDeleteError",

    "OAuthError",
    "OAuthLoginError",
    "OAuthTokenError",
    "OAuthRefreshError",
    "OAuthTokenNotFound",

    "DriveError",
    "DriveUploadError",
    "DriveFolderError",

    "SheetsError",
    "SheetsReadError",
    "SheetsWriteError",

    "ValidationError",

    "SubmissionError",

]