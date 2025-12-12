# Quick Start Guide - LMIS Project

Panduan cepat untuk memulai menggunakan program Longest Monotonically Increasing Subsequence (LMIS).

## Instalasi Cepat

```bash
# 1. Clone atau download repository
git clone <repository-url>
cd FP-Tegraf

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan program
python lmis.py
```

## File Output

Setelah menjalankan `lmis.py`, Anda akan mendapatkan 3 file visualisasi:
- `tree_visualization.png` - Tree lengkap dengan highlight LMIS
- `dp_process.png` - Proses Dynamic Programming
- `comparison.png` - Perbandingan input vs output

## Membuat Visualisasi Kustom

```bash
# Jalankan script dengan contoh built-in
python visualize_custom.py

# Atau edit visualize_custom.py dan tambahkan sequence Anda:
# my_sequence = [5, 2, 8, 6, 3, 6, 9, 7]
# visualize_custom_sequence(my_sequence, prefix='my_custom')
```

## Contoh Penggunaan sebagai Module

```python
from lmis import LMISolver

# Buat solver dengan sequence Anda
sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
solver = LMISolver(sequence)

# Method 1: Tree-based (untuk visualisasi dan pembelajaran)
solver.build_tree()
result, length = solver.find_longest_path()
print(f"LMIS: {result}, Length: {length}")

# Method 2: Dynamic Programming (lebih efisien)
result, length = solver.solve_dp()
print(f"LMIS: {result}, Length: {length}")

# Buat visualisasi
solver.visualize_tree(highlight_path=result, save_path='my_tree.png')
solver.visualize_dp_process(save_path='my_dp.png')
solver.visualize_comparison(save_path='my_comparison.png')
```

## Dokumentasi Lengkap

- **README.md** - Dokumentasi utama dengan penjelasan algoritma lengkap
- **VISUALIZATION.md** - Detail penjelasan setiap jenis visualisasi
- **requirements.txt** - Daftar dependencies yang diperlukan

## Tips

1. Untuk sequence pendek (n ≤ 10): Gunakan tree visualization untuk pemahaman mendalam
2. Untuk sequence panjang (n > 15): Fokus pada DP method dan comparison visualization
3. Gunakan visualize_custom.py untuk eksperimen dengan berbagai sequence

## Troubleshooting

**Import Error:**
```bash
pip install matplotlib networkx
```

**Program Lambat:**
- Gunakan solve_dp() untuk sequence > 15 elemen
- Batasi tree visualization hanya untuk sequence kecil

**Visualisasi Tidak Jelas:**
- Edit ukuran figure di lmis.py (parameter figsize)
- Increase DPI untuk resolution lebih tinggi (parameter dpi)

## Hasil yang Diharapkan

Untuk input: `[4, 1, 13, 7, 0, 2, 8, 11, 3]`
- **Output**: `[4, 7, 8, 11]` atau `[1, 2, 8, 11]`
- **Length**: 4
- **Tree nodes**: 48 nodes explored

## Kontribusi

Proyek ini dibuat untuk tugas praktikum Teori Graf.

## Lisensi

Educational purposes.
