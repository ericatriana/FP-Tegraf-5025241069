# Dokumentasi Visualisasi LMIS

Dokumen ini menjelaskan secara detail tentang tiga jenis visualisasi yang dihasilkan oleh program LMIS.

## 1. Tree Visualization (tree_visualization.png)

### Deskripsi
Visualisasi ini menampilkan tree lengkap yang merepresentasikan semua kemungkinan subsequence yang monotonically increasing dari input sequence.

### Elemen Visual

#### Node Colors
- **Emas (Gold)**: Node ROOT sebagai placeholder awal
- **Merah (Red)**: Node yang merupakan bagian dari Longest Monotonically Increasing Subsequence
- **Biru (Sky Blue)**: Node lain yang dieksplorasi tetapi bukan bagian dari LMIS

#### Struktur
- Tree dibuat secara top-down dari ROOT
- Setiap level merepresentasikan panjang subsequence
- Edge (panah) menunjukkan hubungan parent-child

### Cara Membaca
1. Mulai dari node ROOT di atas
2. Ikuti path dari ROOT ke node merah untuk melihat LMIS
3. Setiap node merah adalah elemen dari LMIS hasil
4. Node biru menunjukkan kemungkinan subsequence lain yang dieksplorasi

### Contoh Interpretasi
Untuk input `[4, 1, 13, 7, 0, 2, 8, 11, 3]`:
- Node merah menunjukkan path: 4 → 7 → 8 → 11
- Ini adalah salah satu LMIS dengan panjang 4
- Node biru lainnya menunjukkan path alternatif yang lebih pendek

### Kegunaan
- Memahami bagaimana algoritma tree-based mengeksplorasi semua kemungkinan
- Melihat visualisasi concrete dari search space
- Membantu debugging untuk sequence yang lebih kecil
- Educational tool untuk memahami konsep subsequence

## 2. DP Process Visualization (dp_process.png)

### Deskripsi
Visualisasi ini menampilkan dua grafik yang menjelaskan proses Dynamic Programming dalam mencari LMIS.

### Grafik Atas: Input Sequence dengan DP Values

#### Elemen Visual
- **Bar Chart**: Menampilkan nilai setiap elemen dalam sequence
- **Label pada Bar**:
  - Nilai atas: Nilai element asli
  - Nilai bawah: Nilai dp[i] (panjang LMIS yang berakhir di index i)
- **Warna Bar**:
  - Merah: Elemen yang merupakan bagian dari LMIS hasil
  - Biru: Elemen yang bukan bagian dari LMIS hasil

#### Cara Membaca
- Lihat label dp pada setiap bar untuk memahami panjang LMIS yang berakhir di index tersebut
- Bar merah menunjukkan elemen yang dipilih sebagai bagian dari LMIS final
- Nilai dp yang lebih tinggi menunjukkan bahwa elemen tersebut adalah bagian dari subsequence yang lebih panjang

### Grafik Bawah: DP Array dengan Parent Connections

#### Elemen Visual
- **Bar Chart**: Menampilkan nilai array dp[i]
- **Panah Merah**: Menunjukkan hubungan parent dalam LMIS
  - Panah dari index j ke index i berarti elemen di j adalah predecessor dari elemen di i dalam LMIS
- **Warna Bar**: Sama seperti grafik atas (merah untuk LMIS, biru untuk lainnya)

#### Cara Membaca
1. Cari bar dengan nilai tertinggi (ini adalah panjang LMIS)
2. Ikuti panah merah dari kanan ke kiri untuk trace back LMIS
3. Setiap panah menunjukkan "elemen ini diikuti oleh elemen berikutnya dalam LMIS"

### Contoh Interpretasi
Untuk sequence `[4, 1, 13, 7, 0, 2, 8, 11, 3]`:

**Grafik Atas:**
```
Index:  0  1   2  3  4  5  6   7  8
Value:  4  1  13  7  0  2  8  11  3
dp[i]:  1  1   2  2  1  2  3   4  3
```

**Grafik Bawah:**
- Bar tertinggi di index 7 dengan dp[7] = 4
- Panah menunjukkan: 0 → 3 → 6 → 7
- Artinya LMIS adalah: 4 → 7 → 8 → 11

### Kegunaan
- Memahami bagaimana nilai dp dihitung untuk setiap index
- Melihat proses trace back untuk mendapatkan LMIS
- Memvalidasi correctness dari algoritma DP
- Visualisasi untuk debugging dan educational purposes

## 3. Comparison Visualization (comparison.png)

### Deskripsi
Visualisasi side-by-side yang membandingkan input sequence original dengan LMIS hasil.

### Grafik Kiri: Original Sequence

#### Elemen Visual
- **Line Plot dengan Marker**: Menampilkan semua elemen dalam sequence original
- **Warna**: Biru (Sky Blue)
- **Label**: Nilai setiap elemen ditampilkan di atas titik

#### Informasi
- Menunjukkan seluruh input sequence
- X-axis: Index dalam array original
- Y-axis: Nilai elemen
- Memperlihatkan variasi dan pola dalam input

### Grafik Kanan: LMIS Result

#### Elemen Visual
- **Line Plot dengan Marker**: Menampilkan elemen-elemen LMIS
- **Warna**: Merah
- **Marker lebih besar**: Untuk emphasize hasil
- **Label**: Nilai setiap elemen LMIS

#### Informasi
- Menunjukkan hanya elemen yang merupakan bagian dari LMIS
- X-axis: Position dalam LMIS (bukan index original)
- Y-axis: Nilai elemen
- Line selalu naik (karena monotonically increasing)

### Cara Membaca
1. **Bandingkan panjang**:
   - Grafik kiri menunjukkan length n (original)
   - Grafik kanan menunjukkan length k (LMIS)
   - k ≤ n selalu

2. **Bandingkan pola**:
   - Grafik kiri mungkin naik-turun (non-monotonic)
   - Grafik kanan selalu naik (strictly increasing)

3. **Trace elemen**:
   - Setiap elemen di grafik kanan ada di grafik kiri
   - Urutan relatif dipertahankan (subsequence property)

### Contoh Interpretasi
Untuk input `[4, 1, 13, 7, 0, 2, 8, 11, 3]`:

**Grafik Kiri (Original):**
- 9 elemen dengan pola naik-turun
- Min: 0, Max: 13
- Non-monotonic pattern

**Grafik Kanan (LMIS):**
- 4 elemen: [4, 7, 8, 11]
- Selalu naik: 4 < 7 < 8 < 11
- Subsequence dari input original
- Tidak ada subsequence monotonic yang lebih panjang

### Kegunaan
- Quick visual comparison antara input dan output
- Validasi bahwa LMIS benar-benar monotonically increasing
- Memahami berapa banyak elemen yang "dibuang" untuk mendapatkan LMIS
- Presentasi hasil yang clear dan professional

## Tips Menggunakan Visualisasi

### Untuk Debugging
1. Gunakan **tree_visualization.png** untuk melihat apakah semua path dieksplorasi
2. Gunakan **dp_process.png** untuk validasi nilai dp di setiap step
3. Gunakan **comparison.png** untuk cek output final

### Untuk Presentasi
1. Mulai dengan **comparison.png** untuk menunjukkan input vs output
2. Lanjut dengan **dp_process.png** untuk explain algoritma
3. Gunakan **tree_visualization.png** untuk deep dive (optional)

### Untuk Pembelajaran
1. Pelajari **tree_visualization.png** untuk memahami search space
2. Pelajari **dp_process.png** untuk memahami dynamic programming
3. Gunakan **comparison.png** untuk verify understanding

## Analisis Visual Complexity

### Tree Visualization
- **Best Case**: Sequence descending - tree minimal, hanya n nodes
- **Worst Case**: Sequence ascending - tree eksplosif, O(2^n) nodes
- **Recommended**: Sequence dengan n ≤ 10 untuk visualisasi yang jelas

### DP Process
- **Scalability**: Baik hingga n ~ 50 untuk readability
- **Clarity**: Terbaik untuk n ≤ 20
- **Information Density**: Tinggi, packed with insights

### Comparison
- **Scalability**: Sangat baik, bisa untuk n > 100
- **Clarity**: Tetap jelas untuk sequence panjang
- **Best Use**: Any sequence size

## Customization Tips

### Mengubah Warna
Edit file `lmis.py`, cari section warna:
```python
node_colors.append('#FF6B6B')  # Ganti kode warna hex
node_colors.append('#87CEEB')  # Ganti kode warna hex
```

### Mengubah Ukuran Figure
Edit parameter figsize:
```python
plt.figure(figsize=(16, 10))  # (width, height) dalam inches
```

### Mengubah DPI (Resolution)
Edit parameter saat save:
```python
plt.savefig(save_path, dpi=300, bbox_inches='tight')  # Increase untuk quality lebih tinggi
```

### Menambahkan Annotation
Tambahkan di dalam fungsi visualisasi:
```python
plt.text(x, y, "Your text", fontsize=12, color='red')
```

## Kesimpulan

Ketiga visualisasi ini saling melengkapi:
- **Tree Visualization**: Shows the "how" - bagaimana algoritma bekerja
- **DP Process**: Shows the "why" - kenapa hasil ini optimal
- **Comparison**: Shows the "what" - apa hasil akhirnya

Gunakan sesuai kebutuhan untuk maximize understanding dan communication.
