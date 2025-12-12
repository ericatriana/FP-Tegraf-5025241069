# Folder Visualisasi

Folder ini berisi semua file visualisasi PNG yang dihasilkan oleh program LMIS.

## Struktur File

### Visualisasi Utama
File-file ini dihasilkan saat menjalankan `lmis.py`:

- **tree_visualization.png** - Visualisasi tree lengkap dengan highlight LMIS path
- **dp_process.png** - Visualisasi proses Dynamic Programming
- **comparison.png** - Perbandingan input sequence vs LMIS output

### Visualisasi Contoh (dari visualize_custom.py)

#### Praktikum Example
Sequence: `[4, 1, 13, 7, 0, 2, 8, 11, 3]`
- **praktikum_tree.png** - Tree visualization
- **praktikum_dp.png** - DP process
- **praktikum_comparison.png** - Comparison

#### Multiple Possibilities Example
Sequence: `[10, 9, 2, 5, 3, 7, 101, 18]`
- **multiple_tree.png** - Tree visualization
- **multiple_dp.png** - DP process
- **multiple_comparison.png** - Comparison

#### Sorted Sequence Example
Sequence: `[1, 2, 3, 4, 5, 6, 7]`
- **sorted_tree.png** - Tree visualization (127 nodes!)
- **sorted_dp.png** - DP process
- **sorted_comparison.png** - Comparison (input = output)

#### Duplicates Example
Sequence: `[1, 3, 2, 3, 4, 2, 5]`
- **duplicates_tree.png** - Tree visualization
- **duplicates_dp.png** - DP process
- **duplicates_comparison.png** - Comparison

## Cara Membaca Visualisasi

### Tree Visualization
- **Node Emas**: ROOT node
- **Node Merah**: Elemen yang merupakan bagian dari LMIS
- **Node Biru**: Node lain yang dieksplorasi

### DP Process
- **Grafik Atas**: Input sequence dengan nilai DP
- **Grafik Bawah**: DP array dengan parent connections (panah merah)
- **Warna Merah**: Bagian dari LMIS
- **Warna Biru**: Bukan bagian dari LMIS

### Comparison
- **Grafik Kiri**: Input sequence original
- **Grafik Kanan**: LMIS hasil (selalu monotonically increasing)

## Regenerasi File

Untuk regenerate semua visualisasi:

```bash
# Visualisasi utama
python lmis.py

# Visualisasi contoh
python visualize_custom.py
```

## Spesifikasi Teknis

- **Format**: PNG
- **Resolution**: 300 DPI (high quality)
- **Size**: Bervariasi tergantung kompleksitas (typically 500KB - 2MB per file)
- **Color Scheme**:
  - Gold (#FFD700) untuk ROOT
  - Red (#FF6B6B) untuk LMIS elements
  - Sky Blue (#87CEEB) untuk other elements

## Catatan

File-file dalam folder ini dapat di-commit ke repository atau di-ignore tergantung preferensi.
Edit file `.gitignore` di root directory untuk mengatur behavior ini.

Untuk detail lengkap tentang cara membaca dan interpretasi visualisasi, lihat [VISUALIZATION.md](../VISUALIZATION.md).
