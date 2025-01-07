import os
import re
import ast

# Daftar keyword, operator, dan delimiter yang akan digunakan untuk klasifikasi
keywords = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
    'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
}
operators = {
    '\\+', '-', '\\*', '/', '//', '%', '\\*\\*', '=', '==', '!=', '<', '<=', '>', '>=',
    '&', '\\|', '\\^', '~', '<<', '>>', 'and', 'or', 'not', 'is', 'in', 'not in', 'is not'
}
delimiters = {
    '\\(', '\\)', '\\[', '\\]', '\\{', '\\}', ',', ':', '\\.', ';', '@', '=', '->', '\\+=', '-=',
    '\\*=', '/=', '//=', '%=', '\\*\\*=', '&=', '\\|=', '\\^=', '>>=', '<<='
}

def tokenize(code):
    # Gabungkan semua token yang memungkinkan
    token_pattern = (
        f"(?P<Keyword>{'|'.join(keywords)})|"
        f"(?P<Operator>{'|'.join(operators)})|"
        f"(?P<Delimiter>{'|'.join(delimiters)})|"
        f"(?P<FloatLiteral>[0-9]+\\.[0-9]+)|"  
        f"(?P<IntegerLiteral>[0-9]+)|"
        f"(?P<StringLiteral>\".*?\"|\'.*?\')|"
        f"(?P<Identifier>[a-zA-Z_][a-zA-Z0-9_]*)"
    )
    regex = re.compile(token_pattern)
    return [(match.group(), match.lastgroup) for match in regex.finditer(code)]

def check_syntax(file_path):
    try:
        # Membaca isi file
        with open(file_path, 'r') as file:
            code = file.read()
        
        # Memeriksa sintaksis dengan pustaka ast
        ast.parse(code)
        print(f"File '{file_path}' valid secara sintaksis!")
        return True
    except SyntaxError as e:
        print(f"Kesalahan Sintaksis di '{file_path}':\n{e}")
        return False
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan. Pastikan nama file benar.")
        return False
    except Exception as e:
        print(f"Terjadi kesalahan saat memeriksa file '{file_path}': {e}")
        return False

def check_semantics(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        exec_globals = {}
        exec(code, exec_globals)

        # aturan semantik (tambahkan aturan sesuai kebutuhan):
        valid = True

        # 1. aturan a harus integer
        if 'a' in exec_globals:
            if not isinstance(exec_globals['a'], int):
                print("Kesalahan Semantik: 'a' harus berupa integer!")
                valid = False
            else:
                print("'a' valid secara semantik!")
        else:
            print("Kesalahan Semantik: Variabel 'a' tidak ditemukan!")
            valid = False
        
        # 2. aturan b harus float
        if 'b' in exec_globals:
            if not isinstance(exec_globals['b'], float):
                print("Kesalahan Semantik: 'b' harus berupa float!")
                valid = False
            else:
                print("'b' valid secara semantik!")
        else:
            print("Kesalahan Semantik: Variabel 'b' tidak ditemukan!")
            valid = False
        
        return valid
        
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan. Pastikan path file benar.")
        return False
    except Exception as e:
        print(f"Kesalahan saat memeriksa semantik file '{file_path}': {e}")
        return False

def generate_machine_code(tokens):
    machine_code = []
    for token, classification in tokens:
        if classification == "Keyword":
            if token in {"int", "float"}:
                machine_code.append(f"DECLARE {token.upper()}")
            elif token == "if":
                machine_code.append("JUMP_IF_FALSE")
            elif token == "else":
                machine_code.append("JUMP")
        elif classification == "Identifier":
            machine_code.append(f"LOAD {token}")
        elif classification == "Operator":
            if token == "+":
                machine_code.append("ADD")
            elif token == "-":
                machine_code.append("SUB")
            elif token == "*":
                machine_code.append("MUL")
            elif token == "/":
                machine_code.append("DIV")
        elif classification == "Integer Literal":
            machine_code.append(f"PUSH_INT {token}")
        elif classification == "Float Literal":
            machine_code.append(f"PUSH_FLOAT {token}")
        elif classification == "Delimiter" and token == ";":
            machine_code.append("END_STATEMENT")

    return machine_code

def generate_output(file_path, tokens, machine_code):
    output_file = file_path.replace('.txt', '_output.txt')
    try:
        with open(output_file, 'w') as file:
            file.write("=== Hasil Kompilasi ===\n")
            file.write("\n[1] Hasil Analisis Leksikal:\n")
            for token, classification in tokens:
                file.write(f"{token} -> {classification}\n")

            file.write("\n[2] Sintaksis: Valid\n")
            file.write("\n[3] Semantik: Valid\n")

            file.write("\n[4] Kode Mesin:\n")
            for line in machine_code:
                file.write(line + "\n")
        print(f"\nOutput berhasil disimpan ke: {output_file}")
    except Exception as e:
        print(f"Kesalahan saat menyimpan file output: {e}")

def main():
    print("=== Kompilator Sederhana ===")

    # Step 1: Input file sumber kode
    file_path = input("Masukkan path ke file sumber kode: ")
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' tidak ditemukan. Pastikan path benar.")
        return

    # Step 2: Analisis Leksikal
    print("\n[1] Analisis Leksikal")
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        classified_tokens = tokenize(code)

        print("Hasil Klasifikasi Token:")
        for token, classification in classified_tokens:
            print(f"{token} -> {classification}")
    except Exception as e:
        print(f"Kesalahan pada analisis leksikal: {e}")
        return

    # Step 3: Analisis Sintaksis
    print("\n[2] Analisis Sintaksis")
    if not check_syntax(file_path):
        return

    # Step 4: Analisis Semantik
    print("\n[3] Analisis Semantik")
    if not check_semantics(file_path):
        return

    # Step 5: Generate Machine Code
    print("\n[4] Generasi Bahasa Mesin")
    machine_code = generate_machine_code(classified_tokens)
    print("\nKode Mesin:")
    for line in machine_code:
        print(line)

    # Step 6: Generate Output File
    generate_output(file_path, classified_tokens, machine_code)

    print("\nProses kompilasi selesai tanpa error!")

if __name__ == "__main__":
    main()
    
# path kode sumber (sesuaikan lah)
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens all.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_leksikal.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_sintaksis.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_semantik.txt