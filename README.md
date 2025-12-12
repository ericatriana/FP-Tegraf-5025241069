# Longest Monotonically Increasing Subsequence (LMIS)

## Dokumentasi

Proyek ini dilengkapi dengan dokumentasi lengkap:
- **README.md** (file ini) - Dokumentasi utama dengan penjelasan algoritma lengkap
- **[QUICKSTART.md](QUICKSTART.md)** - Panduan cepat untuk memulai
- **[VISUALIZATION.md](VISUALIZATION.md)** - Penjelasan detail tentang visualisasi grafis
- **[SUMMARY.md](SUMMARY.md)** - Ringkasan lengkap implementasi

## Deskripsi Proyek

Proyek ini mengimplementasikan algoritma untuk menyelesaikan permasalahan **Longest Monotonically Increasing Subsequence (LMIS)**. LMIS adalah subsequence terpanjang dari sebuah urutan bilangan dimana setiap elemen selalu lebih besar dari elemen sebelumnya (monotonically increasing).

## Permasalahan

Diberikan sebuah urutan bilangan, temukan subsequence terpanjang dimana setiap elemen lebih besar dari elemen sebelumnya.

**Contoh:**
- Input: `[4, 1, 13, 7, 0, 2, 8, 11, 3]`
- Output: `[1, 2, 8, 11]` dengan panjang 4

Catatan: Subsequence tidak harus berurutan dalam array asli, tetapi urutan relatif harus dipertahankan.

## Pendekatan Solusi

Proyek ini mengimplementasikan dua pendekatan berbeda untuk menyelesaikan masalah LMIS:

### 1. Tree-Based Approach

Pendekatan ini membangun sebuah tree yang merepresentasikan semua kemungkinan subsequence yang monotonically increasing.

#### Cara Kerja:
1. **Root Node**: Node akar sebagai placeholder (tidak memiliki nilai)
2. **Building Tree**: Untuk setiap elemen dalam sequence:
   - Buat node baru jika nilai lebih besar dari node parent
   - Tambahkan sebagai child dari node parent
   - Rekursif lanjutkan proses untuk elemen berikutnya
3. **Finding Longest Path**: Lakukan Depth-First Search (DFS) untuk mencari path terpanjang dari root ke leaf

#### Kompleksitas:
- **Time Complexity**: O(2^n) dalam worst case (mengeksplor semua kemungkinan)
- **Space Complexity**: O(2^n) untuk menyimpan semua node
- **Kegunaan**: Baik untuk visualisasi dan pemahaman konsep, tetapi tidak efisien untuk sequence panjang

#### Struktur Tree:
```
ROOT
├── 4
│   ├── 13
│   ├── 7
│   │   ├── 8
│   │   │   └── 11
│   │   └── 11
├── 1
│   ├── 13
│   ├── 7
│   │   ├── 8
│   │   │   └── 11
│   │   └── 11
│   ├── 2
│   │   ├── 8
│   │   │   └── 11
│   │   ├── 11
│   │   └── 3
│   └── 8
│       └── 11
├── 0
│   ├── 2
│   │   ├── 8
│   │   │   └── 11
│   │   ├── 11
│   │   └── 3
│   └── 8
│       └── 11
...
```

### 2. Dynamic Programming Approach

Pendekatan yang lebih efisien menggunakan Dynamic Programming klasik.

#### Cara Kerja:
1. **Inisialisasi**: Buat array `dp[i]` yang menyimpan panjang LMIS yang berakhir di index `i`
2. **Parent Tracking**: Buat array `parent[i]` untuk melacak index elemen sebelumnya
3. **Iterasi**: Untuk setiap elemen `i`:
   ```
   for j from 0 to i-1:
       if sequence[j] < sequence[i]:
           if dp[j] + 1 > dp[i]:
               dp[i] = dp[j] + 1
               parent[i] = j
   ```
4. **Rekonstruksi**: Trace back dari index dengan nilai dp maksimum menggunakan array parent

#### Kompleksitas:
- **Time Complexity**: O(n^2)
- **Space Complexity**: O(n)
- **Kegunaan**: Efisien untuk sequence dengan ukuran besar

#### Contoh Proses DP:

Untuk sequence: `[4, 1, 13, 7, 0, 2, 8, 11, 3]`

| Index | Value | dp[i] | parent[i] | Penjelasan |
|-------|-------|-------|-----------|------------|
| 0     | 4     | 1     | -1        | Elemen pertama |
| 1     | 1     | 1     | -1        | 1 < 4, tidak ada predecessor |
| 2     | 13    | 2     | 0         | 13 > 4, dp[0] + 1 = 2 |
| 3     | 7     | 2     | 0         | 7 > 4, dp[0] + 1 = 2 |
| 4     | 0     | 1     | -1        | 0 < semua, tidak ada predecessor |
| 5     | 2     | 2     | 1         | 2 > 1, dp[1] + 1 = 2 |
| 6     | 8     | 3     | 5         | 8 > 2, dp[5] + 1 = 3 |
| 7     | 11    | 4     | 6         | 11 > 8, dp[6] + 1 = 4 |
| 8     | 3     | 3     | 5         | 3 > 2, dp[5] + 1 = 3 |

Hasil: Maximum dp = 4 at index 7
Trace back: 7 → 6 → 5 → 1 → sequence [1, 2, 8, 11]

## Struktur Kode

### Class `Node`
Representasi node untuk tree visualization.

**Atribut:**
- `value`: Nilai yang disimpan dalam node
- `parent`: Reference ke parent node
- `children`: List dari child nodes
- `level`: Kedalaman node dalam tree

**Method:**
- `add_child(child_node)`: Menambahkan child node

### Class `LMISolver`
Solver utama untuk menyelesaikan permasalahan LMIS.

**Atribut:**
- `sequence`: Input sequence
- `n`: Panjang sequence
- `tree_root`: Root node dari tree
- `all_nodes`: List semua node dalam tree

**Method:**
- `build_tree()`: Membangun tree dari semua kemungkinan subsequence
- `_build_tree_recursive(parent_node, start_idx, last_value)`: Helper rekursif untuk build tree
- `find_longest_path()`: Mencari path terpanjang dalam tree menggunakan DFS
- `solve_dp()`: Solusi menggunakan Dynamic Programming
- `print_tree(max_depth)`: Mencetak visualisasi tree
- `get_statistics()`: Mendapatkan statistik dari tree
- `visualize_tree(highlight_path, save_path)`: Membuat visualisasi grafis tree dengan matplotlib
- `visualize_dp_process(save_path)`: Membuat visualisasi proses Dynamic Programming
- `visualize_comparison(save_path)`: Membuat visualisasi perbandingan input dan output

## Cara Penggunaan

### Instalasi

**Requirements:**
- Python 3.6 atau lebih tinggi
- matplotlib (untuk visualisasi grafis)
- networkx (untuk visualisasi tree)

**Instalasi Dependencies:**

```bash
pip install -r requirements.txt
```

Atau install manual:
```bash
pip install matplotlib networkx
```

### Menjalankan Program

```bash
python lmis.py
```

Program akan otomatis membuat folder `visualizations/` dan menghasilkan 3 file visualisasi di dalamnya:
- `visualizations/tree_visualization.png` - Visualisasi tree lengkap dengan highlight path terpanjang
- `visualizations/dp_process.png` - Visualisasi proses Dynamic Programming
- `visualizations/comparison.png` - Perbandingan sequence original dengan LMIS hasil

### Menggunakan sebagai Module

```python
from lmis import LMISolver

# Inisialisasi dengan sequence
sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
solver = LMISolver(sequence)

# Metode 1: Tree-based
solver.build_tree()
longest_seq, length = solver.find_longest_path()
print(f"LMIS: {longest_seq}, Length: {length}")

# Metode 2: Dynamic Programming (lebih efisien)
longest_seq, length = solver.solve_dp()
print(f"LMIS: {longest_seq}, Length: {length}")

# Visualisasi tree (untuk sequence pendek)
solver.print_tree()

# Statistik
stats = solver.get_statistics()
print(f"Total nodes: {stats['total_nodes']}")

# Visualisasi grafis (akan disimpan di folder visualizations/)
import os
os.makedirs('visualizations', exist_ok=True)
solver.visualize_tree(highlight_path=longest_seq, save_path='visualizations/tree_viz.png')
solver.visualize_dp_process(save_path='visualizations/dp_viz.png')
solver.visualize_comparison(save_path='visualizations/comparison_viz.png')
```

## Contoh Output

```
======================================================================
LONGEST MONOTONICALLY INCREASING SUBSEQUENCE (LMIS)
======================================================================

Input Sequence: [4, 1, 13, 7, 0, 2, 8, 11, 3]
Length: 9

----------------------------------------------------------------------
METODE 1: TREE-BASED APPROACH
----------------------------------------------------------------------

Longest Monotonically Increasing Subsequence:
Sequence: [1, 2, 8, 11]
Length: 4

Tree Statistics:
- Total nodes explored: 47
- Maximum depth: 4

----------------------------------------------------------------------
METODE 2: DYNAMIC PROGRAMMING APPROACH
----------------------------------------------------------------------

Longest Monotonically Increasing Subsequence:
Sequence: [1, 2, 8, 11]
Length: 4

----------------------------------------------------------------------
VERIFICATION
----------------------------------------------------------------------
Both methods agree: Length = 4
Sequences are equivalent (same elements)

======================================================================
GENERATING VISUALIZATIONS
======================================================================

1. Creating tree visualization...
Tree visualization saved to: visualizations/tree_visualization.png

2. Creating DP process visualization...
DP process visualization saved to: visualizations/dp_process.png

3. Creating comparison visualization...
Comparison visualization saved to: visualizations/comparison.png

All visualizations have been generated successfully!
Files created in 'visualizations/' folder
```

## Visualisasi Grafis

Program ini menghasilkan tiga jenis visualisasi untuk membantu pemahaman:

### 1. Tree Visualization (`tree_visualization.png`)
Menampilkan tree lengkap dari semua kemungkinan subsequence:
- **Node Emas (Gold)**: Root node
- **Node Merah**: Path terpanjang (LMIS)
- **Node Biru**: Node lainnya yang dieksplorasi

Visualisasi ini membantu memahami bagaimana algoritma mengeksplorasi semua kemungkinan subsequence yang monotonically increasing.

### 2. DP Process Visualization (`dp_process.png`)
Menampilkan dua grafik:
- **Grafik Atas**: Input sequence dengan nilai DP pada setiap elemen
- **Grafik Bawah**: Array DP dengan panah menunjukkan parent connections

Warna merah menandakan elemen yang merupakan bagian dari LMIS hasil. Panah merah menunjukkan urutan elemen dalam LMIS.

### 3. Comparison Visualization (`comparison.png`)
Menampilkan perbandingan side-by-side:
- **Kiri**: Sequence original lengkap
- **Kanan**: LMIS yang ditemukan

Memudahkan untuk melihat hubungan antara input dan output.

**Catatan**: Untuk penjelasan detail tentang setiap visualisasi, cara membacanya, dan interpretasi, silakan lihat file [VISUALIZATION.md](VISUALIZATION.md).

## Test Cases

Program ini sudah diuji dengan berbagai test case:

### Test Case 1: `[10, 9, 2, 5, 3, 7, 101, 18]`
- **LMIS**: `[2, 3, 7, 18]`
- **Length**: 4

### Test Case 2: `[0, 1, 0, 3, 2, 3]`
- **LMIS**: `[0, 1, 2, 3]`
- **Length**: 4

### Test Case 3: `[7, 7, 7, 7, 7]`
- **LMIS**: `[7]`
- **Length**: 1
- **Note**: Semua elemen sama, tidak ada yang strictly increasing

### Test Case 4: `[1, 2, 3, 4, 5]`
- **LMIS**: `[1, 2, 3, 4, 5]`
- **Length**: 5
- **Note**: Seluruh sequence sudah monotonically increasing

### Test Case 5: `[5, 4, 3, 2, 1]`
- **LMIS**: `[5]` (atau elemen tunggal lainnya)
- **Length**: 1
- **Note**: Sequence menurun, tidak ada subsequence increasing

## Perbandingan Metode

| Aspek | Tree-Based | Dynamic Programming |
|-------|------------|---------------------|
| Time Complexity | O(2^n) | O(n^2) |
| Space Complexity | O(2^n) | O(n) |
| Visualisasi | Excellent | Tidak ada |
| Efisiensi | Buruk untuk n > 15 | Baik hingga n ~ 10000 |
| Pemahaman Konsep | Sangat baik | Memerlukan pemahaman DP |
| Praktikalitas | Learning tool | Production ready |

## Optimisasi Lanjutan

Untuk sequence yang sangat panjang (n > 10000), dapat digunakan algoritma yang lebih optimal:

### Binary Search Approach (O(n log n))

Menggunakan patience sorting dengan binary search:

```python
def solve_optimal(sequence):
    from bisect import bisect_left

    tails = []  # tails[i] = smallest tail of LIS dengan length i+1

    for num in sequence:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)
```

**Complexity**: O(n log n)

## Aplikasi Real-World

1. **Version Control**: Mencari sequence commit yang compatible
2. **Stock Trading**: Mencari periode kenaikan harga terpanjang
3. **Bioinformatics**: Sequence alignment dalam DNA/protein
4. **Data Analysis**: Trend analysis dalam time series data
5. **Network Routing**: Optimal path dengan increasing bandwidth

## Dokumentasi Teknis

### Definisi Formal

**Monotonically Increasing**: Sebuah sequence `a1, a2, ..., ak` disebut monotonically increasing jika:
```
a1 < a2 < a3 < ... < ak
```

**Subsequence**: Sequence yang diturunkan dari sequence lain dengan menghapus beberapa elemen tanpa mengubah urutan elemen yang tersisa.

### Teorema

**Optimal Substructure Property**:
Jika `LIS[i]` adalah panjang longest increasing subsequence yang berakhir di index `i`, maka:
```
LIS[i] = max(LIS[j] + 1) untuk semua j < i dimana sequence[j] < sequence[i]
```

### Proof of Correctness

**Dynamic Programming Approach:**

1. **Base Case**: `dp[0] = 1` (setiap elemen tunggal adalah LMIS dengan panjang 1)
2. **Inductive Step**: Untuk `dp[i]`, kita mempertimbangkan semua `j < i` dimana `sequence[j] < sequence[i]`
3. **Optimality**: Dengan mengambil `max(dp[j] + 1)`, kita memastikan `dp[i]` adalah optimal

## File-File dalam Proyek

### File Utama
1. **lmis.py** - Program utama dengan implementasi algoritma dan visualisasi
2. **visualize_custom.py** - Script untuk membuat visualisasi dengan sequence kustom
3. **README.md** - Dokumentasi lengkap proyek
4. **VISUALIZATION.md** - Dokumentasi detail tentang visualisasi grafis

### Folder dan File Output
- **visualizations/** - Folder berisi semua file visualisasi PNG

Program akan menghasilkan file-file visualisasi berikut di dalam folder `visualizations/`:

1. **tree_visualization.png** - Visualisasi tree dengan highlight LMIS
2. **dp_process.png** - Visualisasi proses Dynamic Programming
3. **comparison.png** - Perbandingan input vs output

### Menggunakan visualize_custom.py

Untuk membuat visualisasi dengan sequence Anda sendiri:

```bash
python visualize_custom.py
```

Atau edit file tersebut dan tambahkan sequence kustom:

```python
my_sequence = [5, 2, 8, 6, 3, 6, 9, 7]
visualize_custom_sequence(my_sequence, prefix='my_custom')
```

Program akan menghasilkan di folder `visualizations/`:
- `visualizations/my_custom_tree.png`
- `visualizations/my_custom_dp.png`
- `visualizations/my_custom_comparison.png`

## Troubleshooting

### Program Terlalu Lambat
- **Masalah**: Tree-based approach untuk sequence panjang
- **Solusi**: Gunakan `solve_dp()` untuk sequence > 15 elemen

### Memory Error
- **Masalah**: Tree-based approach menghabiskan memory
- **Solusi**: Batasi penggunaan tree hanya untuk visualisasi sequence kecil

### Hasil Berbeda antara Metode
- **Normal**: Bisa ada multiple LMIS dengan panjang sama
- **Verifikasi**: Cek apakah panjangnya sama (yang penting adalah panjangnya)

### Import Error matplotlib/networkx
- **Masalah**: Library visualisasi tidak terinstall
- **Solusi**: Jalankan `pip install matplotlib networkx`

## Kontribusi

Proyek ini dibuat sebagai tugas praktikum untuk mata kuliah Teori Graf.

## Lisensi

Proyek ini dibuat untuk keperluan edukasi.

## Referensi

1. Cormen, T. H., et al. (2009). "Introduction to Algorithms" (3rd ed.). MIT Press.
2. Dynamic Programming - Longest Increasing Subsequence
3. GeeksforGeeks - Longest Monotonically Increasing Subsequence
4. LeetCode Problem 300 - Longest Increasing Subsequence

## Kesimpulan

Implementasi ini mendemonstrasikan dua pendekatan berbeda untuk menyelesaikan permasalahan LMIS:

1. **Tree-based approach** memberikan visualisasi yang sangat baik untuk memahami bagaimana semua kemungkinan subsequence dieksplorasi, tetapi tidak efisien untuk input besar.

2. **Dynamic Programming approach** memberikan solusi yang efisien dan praktis untuk digunakan dalam aplikasi real-world.

Kedua metode menghasilkan hasil yang sama dan saling memvalidasi correctness dari implementasi.
