# BINARY SEARCH TREE + BINARY TRAVERSAL
### Project UAS Algoritma Pemrograman

---

## 📋 Informasi Project

**Kelompok:** EsTehHangat

**Anggota:**
1. Viero Alfiandhy Havist(202410370110423)
2. Akmal Dzaky Mahardika(202410370110157)
3. Mohammad Ziaulhaq Alhasbuki(202410370110319)

**Mata Kuliah:** Algoritma Pemrograman

---

## 🎯 Tujuan Project

Mengimplementasikan dua algoritma dari empat pilihan yang diberikan:
1. ✅ **Binary Search Tree (BST)**
2. ✅ **Binary Traversal (PreOrder, InOrder, PostOrder)**

---

## 🚀 Cara Menjalankan Program

#### **1. bst_traversal.py**

**Persyaratan:**
- Python 3.x (standard library only)

**Cara menjalankan:**
```bash
python bst_traversal.py
```
---

## 📖 Penjelasan Algoritma

### 1️⃣ Binary Search Tree (BST)

**Definisi:**
Binary Search Tree adalah struktur data tree dimana setiap node memiliki maksimal 2 anak (left dan right) dengan aturan:
- Semua node di **subtree kiri** < node parent
- Semua node di **subtree kanan** > node parent

**Operasi yang Diimplementasikan:**

#### Insert (Penyisipan)
```
Complexity: O(log n) average, O(n) worst case
```
- Dimulai dari root
- Jika data < node.data → masuk ke kiri
- Jika data > node.data → masuk ke kanan
- Ulangi sampai menemukan posisi kosong

**Contoh:**
```
Insert: 50, 30, 70, 20, 40

        50
       /  \
      30   70
     /  \
    20  40
```

#### Search (Pencarian)
```
Complexity: O(log n) average, O(n) worst case
```
- Bandingkan data dengan node saat ini
- Jika sama → data ditemukan
- Jika lebih kecil → cari di kiri
- Jika lebih besar → cari di kanan

#### Delete (Penghapusan)
```
Complexity: O(log n) average, O(n) worst case
```
Ada 3 kasus:
1. **Leaf node** (tidak punya anak) → langsung hapus
2. **1 anak** → ganti dengan anaknya
3. **2 anak** → ganti dengan successor (nilai terkecil di subtree kanan)

---

### 2️⃣ Binary Traversal

**Definisi:**
Cara sistematis untuk mengunjungi semua node dalam binary tree.

#### PreOrder Traversal
```
Urutan: Root → Left → Right
Complexity: O(n)
```
**Kegunaan:** 
- Copy tree
- Prefix expression
- Membuat backup tree

**Contoh:**
```
Tree:      50
          /  \
         30   70
        /  \
       20  40

PreOrder: 50 → 30 → 20 → 40 → 70
```

#### InOrder Traversal
```
Urutan: Left → Root → Right
Complexity: O(n)
```
**Kegunaan:**
- Mendapatkan data terurut dari BST
- Infix expression

**Contoh:**
```
InOrder: 20 → 30 → 40 → 50 → 70
(Terurut dari kecil ke besar!)
```

#### PostOrder Traversal
```
Urutan: Left → Right → Root
Complexity: O(n)
```
**Kegunaan:**
- Delete tree
- Postfix expression
- Menghitung ukuran tree

**Contoh:**
```
PostOrder: 20 → 40 → 30 → 70 → 50
```

---

## 💡 Fitur Program

### 📋 Menu Utama:
1. **Insert data** - Menambahkan angka ke BST
2. **Delete data** - Menghapus angka dari BST
3. **Search data** - Mencari apakah angka ada di BST
4. **Tampilkan tree** - Visualisasi struktur tree (ASCII art)
5. **PreOrder Traversal** - Tampilkan hasil PreOrder
6. **InOrder Traversal** - Tampilkan hasil InOrder (terurut!)
7. **PostOrder Traversal** - Tampilkan hasil PostOrder
8. **Tampilkan semua Traversal** - Tampilkan ketiga traversal sekaligus
9. **Info tree** - Informasi detail tree (root, size, height, min, max)
0. **Exit** - Keluar dari program

### ✨ Fitur Unggulan:
- ✅ **Interactive input** - User dapat memasukkan data sendiri
- ✅ **Input validation** - Error handling yang baik
- ✅ **Auto properties** - Validasi BST, balanced check, dll 
- ✅ **Clear output** - Penjelasan setiap traversal
- ✅ **User-friendly** - Interface mudah dipahami

---

## 📊 Contoh Penggunaan

### Contoh 1: Membuat BST dan Visualisasi
```
Input data: 50 30 70 20 40 60 80

Tree yang terbentuk (binarytree version):
        ____50____
       /          \
    __30__      __70__
   /      \    /      \
  20      40  60      80

PreOrder:  50 → 30 → 20 → 40 → 70 → 60 → 80
InOrder:   20 → 30 → 40 → 50 → 60 → 70 → 80  (TERURUT!)
PostOrder: 20 → 40 → 30 → 60 → 80 → 70 → 50

Info Tree:
- Root: 50
- Jumlah node: 7
- Tinggi tree: 3
- Min value: 20
- Max value: 80
- Is BST: True ✓
- Is balanced: True ✓
```

### Contoh 2: Delete Node dengan 2 Anak
```
Tree awal: 50 30 70 20 40 60 80
Operasi: Delete 30

Tree setelah delete:
        ____50____
       /          \
    __40__      __70__
   /          /      \
  20        60      80

Penjelasan: 
Node 30 punya 2 anak (20 dan 40)
→ Cari successor = 40 (nilai terkecil di kanan)
→ Node 30 diganti dengan 40
→ Node 40 yang lama dihapus
```

### Contoh 3: InOrder = Sorted!
```
Input acak: 45 23 67 12 34 56 78 90

InOrder Result: 12 → 23 → 34 → 45 → 56 → 67 → 78 → 90

✨ Bukti bahwa BST bekerja dengan benar!
   InOrder traversal SELALU menghasilkan urutan terurut pada BST.
```

---

## 🔍 Analisis Kompleksitas

| Operasi | Average Case | Worst Case |
|---------|--------------|------------|
| Insert  | O(log n)     | O(n)       |
| Delete  | O(log n)     | O(n)       |
| Search  | O(log n)     | O(n)       |
| PreOrder| O(n)         | O(n)       |
| InOrder | O(n)         | O(n)       |
| PostOrder| O(n)        | O(n)       |

**Catatan:** Worst case terjadi ketika tree menjadi skewed (seperti linked list)

---

## 📝 Kesimpulan

Program ini berhasil mengimplementasikan:

1. ✅ **Binary Search Tree** dengan operasi Insert, Delete, dan Search
2. ✅ **Binary Traversal** (PreOrder, InOrder, PostOrder)
3. ✅ Interface interaktif dengan input dari user
4. ✅ Visualisasi tree untuk pemahaman yang lebih baik
5. ✅ Error handling dan validasi input

### 🎯 Pembelajaran:
- Memahami konsep dan implementasi BST
- Memahami perbedaan ketiga jenis traversal
- Implementasi algoritma rekursif
- Membuat program interaktif yang user-friendly
- **Research library** untuk visualisasi optimal
