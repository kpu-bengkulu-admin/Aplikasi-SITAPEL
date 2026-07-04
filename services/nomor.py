# ==========================================================
# SITAPEL v3
# services/nomor.py
# Generator Nomor Permohonan
# ==========================================================

from datetime import datetime


# ==========================================================
# GENERATE NOMOR PERMOHONAN
# ==========================================================

def generate_nomor_permohonan():

    tanggal = datetime.now().strftime("%Y%m%d")

    nomor_urut = get_nomor_urut_hari_ini()

    return f"PDPB-{tanggal}-{nomor_urut:04d}"


# ==========================================================
# NOMOR URUT HARI INI
# ==========================================================

def get_nomor_urut_hari_ini():

    """
    Sementara mengembalikan 1.

    Pada Step 5.6 fungsi ini akan membaca
    Google Sheets sehingga nomor menjadi:

    0001
    0002
    0003
    dst.
    """

    return 1