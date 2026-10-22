import string

STOP_WORDS = {
    "el", "la", "los", "las", "de", "del", "y", "a", "en", "un", "una",
    "que", "es", "por", "con", "no", "se", "su", "al", "lo", "como",
}

def tokenizar(texto):
    """
    Convierte el texto a minusculas, quita los signos de puntuacion
    y lo separa en una lista de palabras (tokens).

    Parametros:
        texto (str): texto crudo a procesar

Retorna:
        list[str]: lista de tokens limpios
    """
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    return texto.split()


def main():
    with open("texto.txt", "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    tokens = tokenizar(texto)

    # Secuencia A: frecuencias de todas las palabras
    frecuencias_todas = {}
    for token in tokens:
        # TODO: completar la linea que agrega "token" al diccionario
        # "frecuencias_todas", sumando 1 cada vez que se repite
        frecuencias = Counter(palabras).most_common(10)
with open("frecuencias.csv", "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["palabra", "frecuencia"])
    for palabra, freq in frecuencias:
        escritor.writerow([palabra, freq])

    # Secuencia B: frecuencias sin palabras vacias (stopwords)
    frecuencias_sin_stopwords = {}
    for token in tokens:
        if token not in STOP_WORDS:
            # TODO: completar la linea que agrega "token" al diccionario
            # "frecuencias_sin_stopwords", sumando 1 cada vez que se repite
            frecuencias = Counter(palabras).most_common(10)
with open("frecuencias.csv", "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["palabra", "frecuencia"])
    for palabra, freq in frecuencias:
        escritor.writerow([palabra, freq])

    print("=== Secuencia A: todas las palabras ===")
    top_a = sorted(frecuencias_todas.items(), key=lambda x: x[1], reverse=True)[:10]
    for palabra, frecuencia in top_a:
        print(f"  {palabra}: {frecuencia}")

    print("\n=== Secuencia B: sin palabras vacias ===")

    top_b = sorted(frecuencias_sin_stopwords.items(), key=lambda x: x[1], reverse=True)[:10]
    for palabra, frecuencia in top_b:
        print(f"  {palabra}: {frecuencia}")

if __name__ == "__main__":
    main()