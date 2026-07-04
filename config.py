# ==========================================================
# SITAPEL v3.0
# config.py
# ==========================================================

from pathlib import Path

# ==========================================================
# INFORMASI APLIKASI
# ==========================================================

APP_NAME = "SITAPEL"
APP_VERSION = "3.0"
APP_AUTHOR = "KPU"

# ==========================================================
# BASE DIRECTORY
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

# ==========================================================
# GOOGLE SERVICE ACCOUNT
# ==========================================================

SERVICE_ACCOUNT_FILE = BASE_DIR / "service_account.json"

# Alias untuk services
GOOGLE_SERVICE_ACCOUNT = str(SERVICE_ACCOUNT_FILE)

# ==========================================================
# GOOGLE SHEETS
# ==========================================================

SPREADSHEET_ID = "18h8koqclETHuwSgcXO53f3C938-F41y4YUWCY4rVv94"

WORKSHEET_NAME = "Sheet1"

# ==========================================================
# GOOGLE DRIVE
# ==========================================================

PARENT_FOLDER_ID = "1Fg0J7ffU88Aw5KWTf3kPr2Vwzgt_jEEh"

# Alias untuk services
DRIVE_PARENT_FOLDER = PARENT_FOLDER_ID

# ==========================================================
# GOOGLE API SCOPES
# ==========================================================

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]

# ==========================================================
# STATUS PERMOHONAN
# ==========================================================

STATUS_MENUNGGU = "MENUNGGU"
STATUS_DIPROSES = "DIPROSES"
STATUS_SELESAI = "SELESAI"
STATUS_DITOLAK = "DITOLAK"

STATUS_LIST = [
    STATUS_MENUNGGU,
    STATUS_DIPROSES,
    STATUS_SELESAI,
    STATUS_DITOLAK,
]

# ==========================================================
# BATAS UKURAN FILE
# ==========================================================

MAX_FILE_SIZE_MB = 5

MAX_FILE_SIZE = MAX_FILE_SIZE_MB * 1024 * 1024

# ==========================================================
# FORMAT FILE YANG DIIZINKAN
# ==========================================================

ALLOWED_FILE_TYPES = [
    "application/pdf",
    "image/jpeg",
    "image/png",
]

# ==========================================================
# NAMA FILE DI GOOGLE DRIVE
# ==========================================================

FILE_KK = "KK.pdf"
FILE_KTP = "KTP.pdf"
FILE_PENDUKUNG = "DOKUMEN_PENDUKUNG.pdf"

# ==========================================================
# NOMOR PERMOHONAN
# ==========================================================

PREFIX_PERMOHONAN = "PDM"

# ==========================================================
# ESTIMASI LAYANAN
# ==========================================================

ESTIMASI_VERIFIKASI = "1 Hari Kerja"

# ==========================================================
# LINK GOOGLE DRIVE
# ==========================================================

DRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/{}"

# ==========================================================
# SESSION STATE DEFAULT
# ==========================================================

DEFAULT_SESSION = {

    "page": "dashboard",

    "step": 1,

    "nomor_permohonan": "",

    "layanan": "",

    "nama_pemohon": "",

    "email": "",

    "whatsapp": "",

    "nama_diajukan": "",

    "alamat_tujuan": "",

    "alasan": "",

    "alasan_lainnya": "",

    "kk_file": None,

    "ktp_file": None,

    "dokumen_pendukung": None,

    "persetujuan": False,
}