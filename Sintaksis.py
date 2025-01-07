import ast
def check_syntax(file_path):
    try:
        # Membaca isi file
        with open(file_path, 'r') as file:
            code = file.read()
        
        # Memeriksa sintaksis dengan pustaka ast
        ast.parse(code)
        print(f"File '{file_path}' valid secara sintaksis!")
    except SyntaxError as e:
        print(f"Kesalahan Sintaksis di '{file_path}':\n{e}")
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan. Pastikan nama file benar.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memeriksa file '{file_path}': {e}")

if __name__ == "__main__":
    file_path = input("Masukkan nama file token: ")
    check_syntax(file_path)
    

# path kode sumber (sesuaikan lah)
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens all.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_leksikal.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_sintaksis.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_semantik.txt