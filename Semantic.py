def check_semantics(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        exec_globals = {}
        exec(code, exec_globals)

        # aturan semantik (tambahkan aturan sesuai kebutuhan):
        # 1. aturan a harus integer
        if 'a' in exec_globals:
            if not isinstance(exec_globals['a'], int):
                print("Kesalahan Semantik: 'a' harus berupa integer!")
            else:
                print("'a' valid secara semantik!")
        else:
            print("Kesalahan Semantik: Variabel 'a' tidak ditemukan!")
        
        # 2. aturan b harus float
        if 'b' in exec_globals:
            if not isinstance(exec_globals['b'], float):
                print("Kesalahan Semantik: 'b' harus berupa float!")
            else:
                print("'b' valid secara semantik!")
        else:
            print("Kesalahan Semantik: Variabel 'b' tidak ditemukan!")
            
        """
        # Tambahan aturan
        if 'c' in exec_globals:
             if exec_globals['c'] != exec_globals['a'] + exec_globals['b']:
                print("Kesalahan Semantik: 'c' harus hasil penjumlahan 'a' dan 'b'!")
             else:
                print("'c' valid secara semantik!")
        else:
            print("Kesalahan Semantik: Variabel 'c' tidak ditemukan!")
        """
             
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan. Pastikan path file benar.")
    except Exception as e:
        print(f"Kesalahan saat memeriksa semantik file '{file_path}': {e}")

if __name__ == "__main__":
    file_path = input("Masukkan path ke file Python yang ingin diperiksa: ")
    check_semantics(file_path)

# path kode sumber (sesuaikan lah)
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens all.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_leksikal.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_sintaksis.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_semantik.txt