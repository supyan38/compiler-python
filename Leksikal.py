import re

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

def classify_token(token):
    # Gunakan tokenisasi berbasis regex
    token_matches = tokenize(token)
    return token_matches[0][1] if token_matches else 'Unknown'

def main():
    file_name = input("Masukkan nama file yang berisi token (path nya): ")
    try:
        with open(file_name, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return

    classified_tokens = tokenize(code)
    token_counts = {}

    for _, classification in classified_tokens:
        if classification in token_counts:
            token_counts[classification] += 1
        else:
            token_counts[classification] = 1

    print("\nHasil Klasifikasi Token:")
    for token, classification in classified_tokens:
        print(f"{token} -> {classification}")

    print("\nJumlah Setiap Jenis Token:")
    for classification, count in token_counts.items():
        print(f"{classification}: {count}")

if __name__ == "__main__":
    main()
    

# path kode sumber (sesuaikan lah)
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens all.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_leksikal.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_sintaksis.txt
# C:\Users\LNV\Documents\1. Kuliah\semester 5\Teknik Kompilasi\Lexer\tokens_semantik.txt
