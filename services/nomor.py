# ==========================================================
# SITAPEL v4
#
# File        : services/nomor.py
# Status      : FINAL
# Version     : 4.0.0
#
# Python      : 3.14+
# Streamlit   : 1.58+
#
# Description :
# Generator Nomor Permohonan
#
# ==========================================================

from __future__ import annotations

import re
from datetime import datetime

from providers.sheets import (
    get_column,
)

# ==========================================================
# CONSTANT
# ==========================================================

PREFIX = "SITAPEL"

COLUMN_NAME = "Nomor Permohonan"

NUMBER_WIDTH = 6

PATTERN = re.compile(
    r"^SITAPEL-(\d{4})-(\d{6})$"
)


# ==========================================================
# YEAR
# ==========================================================

def current_year() -> str:
    """
    Mengembalikan tahun saat ini.
    """

    return datetime.now().strftime("%Y")


# ==========================================================
# LAST SEQUENCE
# ==========================================================

def get_last_sequence() -> int:
    """
    Mengambil nomor urut terbesar
    pada tahun berjalan.
    """

    year = current_year()

    numbers = get_column(COLUMN_NAME)

    last = 0

    for nomor in numbers:

        if not nomor:

            continue

        nomor = nomor.strip()

        match = PATTERN.match(nomor)

        if match is None:

            continue

        nomor_year = match.group(1)

        sequence = int(match.group(2))

        if nomor_year != year:

            continue

        if sequence > last:

            last = sequence

    return last


# ==========================================================
# NEXT SEQUENCE
# ==========================================================

def next_sequence() -> int:
    """
    Nomor urut berikutnya.
    """

    return get_last_sequence() + 1


# ==========================================================
# FORMAT
# ==========================================================

def format_nomor(sequence: int) -> str:
    """
    Format nomor permohonan.

    Contoh:

    SITAPEL-2026-000001
    """

    return (

        f"{PREFIX}"

        f"-{current_year()}"

        f"-{sequence:0{NUMBER_WIDTH}d}"

    )


# ==========================================================
# GENERATOR
# ==========================================================

def generate_nomor() -> str:
    """
    Menghasilkan nomor permohonan baru.
    """

    return format_nomor(

        next_sequence()

    )


# ==========================================================
# EXPORT
# ==========================================================

__all__ = [

    "generate_nomor",

]