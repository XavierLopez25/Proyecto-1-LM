import csv

def find_unique_symbols(csv_file_path):
    unique_symbols = set()
    
    # Abrir el archivo CSV
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # Leer cada línea
        for row in reader:
            # Iterar sobre cada campo en la fila
            for field in row:
                # Añadir cada carácter al conjunto de símbolos únicos
                unique_symbols.update(field)
    
    return unique_symbols

# Ruta al archivo CSV
csv_path = 'BL-Flickr-Images-Book.csv'
# Llamar a la función y obtener los símbolos
symbols = find_unique_symbols(csv_path)
print("\n\nUnique symbols in CSV:", symbols,"\n\n")


def categorize_and_sort_characters(characters):
    # Define las categorías usando intervalos de Unicode
    categories = {
        'Latin Lowercase': set(),
        'Latin Uppercase': set(),
        'Cyrillic Lowercase': set(),
        'Cyrillic Uppercase': set(),
        'Greek Lowercase': set(),
        'Greek Uppercase': set(),
        'Digits': set(),
        'Other Characters': set()
    }
    
    # Clasificar cada carácter en el conjunto apropiado
    for char in characters:
        if 'a' <= char <= 'z':
            categories['Latin Lowercase'].add(char)
        elif 'A' <= char <= 'Z':
            categories['Latin Uppercase'].add(char)
        elif 'α' <= char <= 'ω':
            categories['Greek Lowercase'].add(char)
        elif 'Α' <= char <= 'Ω':
            categories['Greek Uppercase'].add(char)
        elif 'а' <= char <= 'я':
            categories['Cyrillic Lowercase'].add(char)
        elif 'А' <= char <= 'Я':
            categories['Cyrillic Uppercase'].add(char)
        elif '0' <= char <= '9':
            categories['Digits'].add(char)
        else:
            categories['Other Characters'].add(char)
    
    # Ordenar cada conjunto y devolver los resultados
    sorted_categories = {k: ''.join(sorted(v)) for k, v in categories.items()}
    return sorted_categories

# Conjunto de caracteres únicos
unique_characters = {'̇', 'Ю', 'é', '̔', 'І', 'ј', 'ה', '′', 'v', 'л', 'o', '[', 'K', 'f', '̊', '̣', 'О', 'þ', 'a', 's', 'ת', 'м', 'W', 'º', '?', 'n', ',', 'σ', 'и', 'Л', 'ω', 'ћ', '“', 'z', 'C', 'ς', 'с', 'С', 'е', 'ѵ', 'З', 'Ф', 'x', 'S', 'χ', 'β', 'ψ', 'ý', '}', 'ł', 'T', 'ρ', '\uf004', '"', 'к', 'р', 'l', 'п', 'ͅ', 'Φ', 'ó', 'p', '&', 'И', 'х', 'ц', 'R', '3', 'В', 'w', 'Β', '*', 'ד', '7', '̋', 'Π', 'Ξ', 'а', 'y', 'è', '̂', '”', 'Ч', '0', 'і', 'O', 'm', 'Ζ', 'я', 'Т', 'ĭ', '(', 'б', 'æ', 'č', '̀', 'ι', ')', 'Τ', 'й', '̄', 'Ш', 'H', '’', ' ', 'k', '.', '̃', 'Y', 'Μ', ':', 'ш', '2', 'Е', 'У', 'I', "'", 'у', 'λ', 'ö', 'П', 'Н', 'ʹ', ';', 'τ', 'š', '̧', 'φ', 'ø', 'ק', '̨', '9', 'з', 'ב', '̌', 'Б', '4', 'Я', 'ѳ', 'ı', 'ξ', 'ъ', '-', ']', 'ч', 'κ', 'М', 'G', 'e', 'Г', '5', 'ⁿ', 'í', 'γ', 'Ι', 'D', 'P', '6', '́', 'ם', 'ь', '̢', 'd', 'r', 'א', 'н', 'L', '1', '„', 'Œ', 'Э', 'ї', 'ü', 'j', 'г', 'Æ', 'ú', 'Q', 'δ', 'Θ', 'ѣ', 'э', 'M', 'Х', 'θ', 'F', 'X', 'A', 'b', 'u', 'К', 'N', 'B', 'ʿ', 'А', 'υ', 'Ж', 'œ', 'Λ', '°', 'η', 'ж', '\uf010', 'Σ', 'Ѳ', 'V', 'Р', 'Ø', 'i', 'ל', '£', 'ć', '|', 'ο', 'Γ', 'ë', 'Ц', 'т', 'Κ', '̈', 'פ', 'c', 'J', 'ν', '·', 'ф', 'Ε', '!', 'π', 'Α', 'g', 'в', '̓', 'ε', 'д', 'Đ', 'ю', 'Ο', 'ð', 'q', 'Δ', 'Ν', '̆', 'Ł', 't', 'Z', 'h', 'E', 'ы', '8', 'α', 'Д', '/', 'щ', 'μ', 'о', 'U'}

# Categorizar y ordenar los caracteres
sorted_characters = categorize_and_sort_characters(unique_characters)

# Mostrar los resultados ordenados
for category, chars in sorted_characters.items():
    print(f"{category}: {chars}")

print("")
