"""Modul contoh perbaikan kode mengikuti konvensi PEP 8."""


def hitung_penjumlahan(nilai_a, nilai_b):
    """Menghitung penjumlahan dua nilai.

    Args:
        nilai_a: Nilai pertama.
        nilai_b: Nilai kedua.

    Returns:
        Hasil penjumlahan nilai_a dan nilai_b.
    """
    return nilai_a + nilai_b


def main():
    """Fungsi utama program."""
    hasil = hitung_penjumlahan(1, 2)
    print(f"Hasil penjumlahan: {hasil}")


if __name__ == "__main__":
    main()
