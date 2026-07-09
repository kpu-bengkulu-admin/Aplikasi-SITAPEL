# ==========================================================
# SITAPEL v4
# data/wilayah.py
# Wilayah Administrasi Kota Bengkulu
# ==========================================================

WILAYAH = {

    "Gading Cempaka": [
        "Cempaka Permai",
        "Jalan Gedang",
        "Lingkar Barat",
        "Padang Harapan",
        "Sidomulyo"
    ],

    "Kampung Melayu": [
        "Kandang",
        "Kandang Mas",
        "Padang serai",
        "Muara Dua",
        "Sumber Jaya"
        "Teluk Sepang"
    ],

    "Muara Bangkahulu": [
        "Bentiring",
        "Bentiring Permai",
        "Beringin Raya",
        "Kandang Limun",
        "Pematang Gubernur",
        "Rawa Makmur",
        "Rawa Makmur Permai"
    ],

    "Ratu Agung": [
        "Kebun Kenanga",
        "Kebun Tebeng",
        "Kebun Beler",
        "Nusa Indah",
        "Sawah Lebar",
        "Sawah Lebar Baru",
        "Tanah Patah"
        "Lempuing"
    ],

    "Ratu Samban": [
        "Anggut Atas",
        "Anggut Bawah",
        "Anggut Dalam",
        "Belakang Pondok",
        "Kebun Dahri",
        "Kebun Geran",
        "Padang Jati",
        "Penurunan"
        "Pengantungan",
    ],

    "Selebar": [
        "Betungan",
        "Bumi Ayu",
        "Pagar Dewa",
        "Sumur Dewa",
        "Pekan Sabtu",
        "Sukarami"
    ],

    "Singaran Pati": [
        "Dusun Besar",
        "Jembatan Kecil",
        "Lingkar Timur",
        "Panorama",
        "Padang Nangka",
        "Timur Indah"
    ],

    "Sungai Serut": [
        "Kampung Kelawi",
        "Semarang",
        "Surabaya",
        "Sukamerindu",
        "Tanjung Jaya",
        "Tanjung Agung"
        "Pasar Bengkulu"
    ],

    "Teluk Segara": [
        "Bajak",
        "Berkas",
        "Jitra",
        "Kebun Roos",
        "Kebun keling",
        "Kampung Bali",
        "Malabero",
        "Pasar Baru",
        "Pasar Melintang",
        "Pintu Batu",
        "Pondok Besi",
        "Sumur Meleleh",
        "Tengah Padang"
    ]

}

# ==========================================================
# HELPER
# ==========================================================

def daftar_kecamatan():
    """
    Menghasilkan daftar kecamatan
    dalam urutan alfabet.
    """
    return sorted(WILAYAH.keys())


def daftar_kelurahan(kecamatan):
    """
    Menghasilkan daftar kelurahan
    berdasarkan kecamatan.
    """
    if not kecamatan:
        return []

    return WILAYAH.get(kecamatan, [])