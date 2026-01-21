"""
BINARY SEARCH TREE + BINARY TRAVERSAL
Project UAS Algoritma Pemrograman (BINARYTREE VERSION)

Implementasi:
1. Binary Search Tree (Insert, Delete, Search)
2. Binary Traversal (PreOrder, InOrder, PostOrder)

Features:
- BEST tree visualization using binarytree library
- Beautiful ASCII art output
- Interactive menu
- Professional presentation

Kelompok: [Nama Kelompok Anda]
Anggota:
1. [Nama 1]
2. [Nama 2]
3. [Nama 3]
4. [Nama 4]
"""

try:
    from binarytree import Node as BinaryNode, build
    BINARYTREE_AVAILABLE = True
except ImportError:
    BINARYTREE_AVAILABLE = False
    print("⚠️  Library 'binarytree' belum terinstall.")
    print("📦 Install dengan: pip install binarytree")
    print("🔄 Menggunakan visualisasi default...\n")


class Node:
    """Class untuk merepresentasikan node dalam BST (internal structure)"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class untuk Binary Search Tree beserta operasi-operasinya"""
    
    def __init__(self):
        self.root = None
    
    # ========== OPERASI BST ==========
    
    def insert(self, data):
        """Memasukkan data baru ke dalam BST"""
        if self.root is None:
            self.root = Node(data)
            print(f"✓ Data {data} berhasil ditambahkan sebagai root")
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper function untuk insert secara rekursif"""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                print(f"✓ Data {data} berhasil ditambahkan")
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                print(f"✓ Data {data} berhasil ditambahkan")
            else:
                self._insert_recursive(node.right, data)
        else:
            print(f"✗ Data {data} sudah ada dalam tree")
    
    def search(self, data):
        """Mencari data dalam BST"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Helper function untuk search secara rekursif"""
        if node is None:
            return False
        
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data):
        """Menghapus data dari BST"""
        if self.root is None:
            print("✗ Tree kosong, tidak ada yang bisa dihapus")
            return
        
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        """Helper function untuk delete secara rekursif"""
        if node is None:
            print(f"✗ Data {data} tidak ditemukan")
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node ditemukan
            if node.left is None and node.right is None:
                print(f"✓ Data {data} berhasil dihapus (leaf node)")
                return None
            elif node.left is None:
                print(f"✓ Data {data} berhasil dihapus (1 anak kanan)")
                return node.right
            elif node.right is None:
                print(f"✓ Data {data} berhasil dihapus (1 anak kiri)")
                return node.left
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._delete_recursive(node.right, successor.data)
                print(f"✓ Data {data} berhasil dihapus (2 anak, diganti dengan {successor.data})")
        
        return node
    
    def _find_min(self, node):
        """Mencari node dengan nilai minimum"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    # ========== BINARY TRAVERSAL ==========
    
    def preorder(self):
        """PreOrder Traversal: Root → Left → Right"""
        print("\n" + "="*70)
        print("🔹 PREORDER TRAVERSAL")
        print("="*70)
        print("Urutan: Root → Left → Right")
        result = []
        self._preorder_recursive(self.root, result)
        if result:
            print("Hasil: " + " → ".join(map(str, result)))
        else:
            print("Tree kosong")
        print("="*70)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def inorder(self):
        """InOrder Traversal: Left → Root → Right"""
        print("\n" + "="*70)
        print("🔹 INORDER TRAVERSAL")
        print("="*70)
        print("Urutan: Left → Root → Right")
        result = []
        self._inorder_recursive(self.root, result)
        if result:
            print("Hasil: " + " → ".join(map(str, result)))
            print("Dalam BST, InOrder menghasilkan urutan terurut (ascending)")
        else:
            print("Tree kosong")
        print("="*70)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def postorder(self):
        """PostOrder Traversal: Left → Right → Root"""
        print("\n" + "="*70)
        print("🔹 POSTORDER TRAVERSAL")
        print("="*70)
        print("Urutan: Left → Right → Root")
        result = []
        self._postorder_recursive(self.root, result)
        if result:
            print("Hasil: " + " → ".join(map(str, result)))
        else:
            print("Tree kosong")
        print("="*70)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    # ========== VISUALISASI DENGAN BINARYTREE ==========
    
    def display_tree(self):
        if self.root is None:
            print("\n❌ Tree kosong")
            return
        
        print("\n" + "="*70)
        print("🌳 BINARY SEARCH TREE VISUALIZATION")
        print("="*70)
        
        if BINARYTREE_AVAILABLE:
            # Convert our BST to binarytree format
            bt_root = self._convert_to_binarytree(self.root)
            print(bt_root)
            
            # Print tree properties
            print(f"\n📊 Properties:")
            print(f"   Height: {bt_root.height}")
            print(f"   Size: {bt_root.size}")
            print(f"   Leaf count: {bt_root.leaf_count}")
            print(f"   Is balanced: {bt_root.is_balanced}")
            print(f"   Is BST: {bt_root.is_bst}")
        else:
            # Fallback to default visualization
            self._display_default()
        
        print("="*70)
    
    def _convert_to_binarytree(self, node):
        """Convert our Node to binarytree Node"""
        if node is None:
            return None
        
        bt_node = BinaryNode(node.data)
        bt_node.left = self._convert_to_binarytree(node.left)
        bt_node.right = self._convert_to_binarytree(node.right)
        return bt_node
    
    def _display_default(self):
        """Fallback visualization"""
        self._display_helper(self.root, "", True)
    
    def _display_helper(self, node, prefix, is_tail):
        if node is not None:
            print(prefix + ("└── " if is_tail else "├── ") + f"[{node.data}]")
            children = []
            if node.left is not None:
                children.append(node.left)
            if node.right is not None:
                children.append(node.right)
            
            for i, child in enumerate(children):
                is_last = (i == len(children) - 1)
                extension = "    " if is_tail else "│   "
                
                if child == node.left and node.right is not None:
                    self._display_helper(child, prefix + extension, False)
                else:
                    self._display_helper(child, prefix + extension, True)
    

    
    def get_info(self):
        """Menampilkan informasi tree"""
        if self.root is None:
            print("\n❌ Tree kosong")
            return
        
        print("\n" + "="*70)
        print("ℹ️  INFORMASI TREE")
        print("="*70)
        print(f"🔹 Root        : {self.root.data}")
        print(f"🔹 Jumlah node : {self._count_nodes(self.root)}")
        print(f"🔹 Tinggi tree : {self._height(self.root)}")
        print(f"🔹 Min value   : {self._find_min(self.root).data}")
        print(f"🔹 Max value   : {self._find_max(self.root).data}")
        
        if BINARYTREE_AVAILABLE:
            bt_root = self._convert_to_binarytree(self.root)
            print(f"🔹 Is balanced : {bt_root.is_balanced}")
            print(f"🔹 Is perfect  : {bt_root.is_perfect}")
            print(f"🔹 Is strict   : {bt_root.is_strict}")
        
        print("="*70)
    
    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)
    
    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current


# ========== MENU PROGRAM ==========

def print_header():
    print("\n" + "="*70)
    print("  🌳 BINARY SEARCH TREE & BINARY TRAVERSAL 🌳")
    print("  📚 Project UAS Algoritma Pemrograman")
    print("="*70)


def print_menu():
    print("\n" + "─"*70)
    print("📋 MENU UTAMA:")
    print("─"*70)
    print("  1️⃣  Insert data")
    print("  2️⃣  Delete data")
    print("  3️⃣  Search data")
    print("  4️⃣  Tampilkan tree")
    print("  5️⃣  PreOrder Traversal")
    print("  6️⃣  InOrder Traversal")
    print("  7️⃣  PostOrder Traversal")
    print("  8️⃣  Tampilkan semua Traversal")
    print("  9️⃣  Info tree")
    print("  0️⃣  Exit")
    print("─"*70)


def main():
    bst = BinarySearchTree()
    
    print_header()
    print("   Menggunakan library 'binarytree' untuk ASCII art sempurna!\n")
    
    if not BINARYTREE_AVAILABLE:
        print("💡 TIP: Install binarytree untuk visualisasi maksimal!")
        print("   Jalankan: pip install binarytree\n")
    
    print("🔹 Apakah Anda ingin mengisi data awal? (y/n): ", end="")
    choice = input().lower()
    
    if choice == 'y':
        print("\n📝 Masukkan angka-angka (pisahkan dengan spasi):")
        print("   Contoh: 50 30 70 20 40 60 80")
        print("   Input: ", end="")
        data_input = input()
        
        try:
            numbers = [int(x) for x in data_input.split()]
            print()
            for num in numbers:
                bst.insert(num)
            bst.display_tree()
        except ValueError:
            print("✗ Input tidak valid, tree dimulai kosong")
    
    while True:
        print_menu()
        pilihan = input("👉 Pilih menu (0-9): ")
        
        if pilihan == '1':
            try:
                data = int(input("\n📥 Masukkan angka yang ingin ditambahkan: "))
                bst.insert(data)
            except ValueError:
                print("✗ Input harus berupa angka!")
        
        elif pilihan == '2':
            try:
                data = int(input("\n🗑️  Masukkan angka yang ingin dihapus: "))
                bst.delete(data)
            except ValueError:
                print("✗ Input harus berupa angka!")
        
        elif pilihan == '3':
            try:
                data = int(input("\n🔍 Masukkan angka yang ingin dicari: "))
                if bst.search(data):
                    print(f"✅ Data {data} ditemukan dalam tree")
                else:
                    print(f"❌ Data {data} tidak ditemukan dalam tree")
            except ValueError:
                print("✗ Input harus berupa angka!")
        
        elif pilihan == '4':
            bst.display_tree()
        
        elif pilihan == '5':
            bst.preorder()
        
        elif pilihan == '6':
            bst.inorder()
        
        elif pilihan == '7':
            bst.postorder()
        
        elif pilihan == '8':
            print("\n" + "🔄"*35)
            bst.preorder()
            bst.inorder()
            bst.postorder()
            print("🔄"*35)
        
        elif pilihan == '9':
            bst.get_info()
        
        elif pilihan == '0':
            print("\n" + "="*70)
            print("  👋 Terima kasih telah menggunakan program ini!")
            print("  🎓 Semoga membantu pemahaman Anda tentang BST!")
            print("="*70 + "\n")
            break
        
        else:
            print("\n❌ Pilihan tidak valid! Silakan pilih 0-9")


if __name__ == "__main__":
    main()