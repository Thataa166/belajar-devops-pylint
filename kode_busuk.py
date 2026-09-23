"""Modul contoh perbaikan kode_busuk mengikuti konvensi PEP 8."""


def hitung_penjumlahan_dua_nilai(nilai_pertama, nilai_kedua):
    """Menghitung penjumlahan dua nilai.

    Args:
        nilai_pertama: Nilai pertama yang dijumlahkan.
        nilai_kedua: Nilai kedua yang dijumlahkan.

    Returns:
        Hasil penjumlahan nilai_pertama dan nilai_kedua.
    """
    hasil = nilai_pertama + nilai_kedua
    print(hasil)
    return hasil


def main():
    """Fungsi utama program."""
    hitung_penjumlahan_dua_nilai(1, 2)


if __name__ == "__main__":
    main()
