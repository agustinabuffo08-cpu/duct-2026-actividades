import os
import string

import matplotlib.pyplot as plt

# Palabras vacias (stopwords) que no se cuentan, como en la Secuencia B
# de la Clase 2, ampliadas con otras palabras vacias frecuentes del español
STOP_WORDS = {
    "el", "la", "los", "las", "de", "del", "y", "a", "en", "un", "una",
    "que", "es", "por", "con", "no", "se", "su", "al", "lo", "como",
    "o", "u", "e", "ni", "pero", "sino", "si", "para", "sus", "le", "les",
    "me", "mi", "mis", "te", "tu", "tus", "yo", "nos", "he", "ha", "han",
    "hay", "fue", "era", "son", "ser", "sea", "esta", "este", "esto",
    "estos", "estas", "esa", "ese", "eso", "esos", "esas", "aquel",
    "cada", "todo", "todos", "toda", "todas", "otro", "otros", "otra",
    "otras", "uno", "unos", "unas", "dos", "algún", "alguno", "alguna",
    "más", "muy", "ya", "también", "casi", "porque", "cuando", "donde",
    "sin", "sobre", "entre", "hasta", "desde", "él", "ella", "qué",
}


def leer_archivo(ruta):
    """
    Lee un archivo de texto y devuelve su contenido.

    Parametros:
        ruta (str): ruta al archivo de texto

    Retorna:
        str: el contenido del archivo, o None si el archivo no existe
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo '{ruta}'.")
        return None


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
    for signo in string.punctuation + "¿¡«»“”‘’—–…":
        texto = texto.replace(signo, "")
    return texto.split()


def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto, sin contar las
    palabras vacias (STOP_WORDS).

    Parametros:
        texto (str): el texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    frecuencias = {}
    for palabra in tokenizar(texto):
        if palabra not in STOP_WORDS:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def graficar_top(frecuencias, ruta_grafico, top_n=10):
    """
    Genera un grafico de barras horizontales con las top_n palabras
    mas frecuentes y lo guarda como imagen.

    Parametros:
        frecuencias (dict): pares {palabra: frecuencia}
        ruta_grafico (str): ruta del archivo .png a guardar
        top_n (int): cantidad de palabras a graficar

    Retorna:
        None (genera y guarda el grafico)
    """
    top = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]

    # Comprension de listas: separa las tuplas (palabra, frecuencia) en dos listas
    palabras = [par[0] for par in top]
    valores = [par[1] for par in top]

    plt.figure(figsize=(10, 6))
    # Se invierten las listas para que la palabra mas frecuente quede arriba
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(ruta_grafico, dpi=150, bbox_inches="tight")
    plt.show()


def main():
    # Los archivos se buscan y se guardan en la misma carpeta que este script
    carpeta = os.path.dirname(os.path.abspath(__file__))
    texto = leer_archivo(os.path.join(carpeta, "texto_integradora.txt"))
    if texto is None:
        return

    frecuencias = contar_frecuencias(texto)

    print(f"Cantidad de palabras contadas: {sum(frecuencias.values())}")
    print(f"Cantidad de palabras distintas: {len(frecuencias)}")
    print("\nLas 10 palabras mas frecuentes:")
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
    for palabra, frecuencia in top10:
        print(f"  {palabra}: {frecuencia}")

    ruta_grafico = os.path.join(carpeta, "grafico_frecuencias.png")
    graficar_top(frecuencias, ruta_grafico)
    print(f"\nGrafico guardado en: {ruta_grafico}")


if __name__ == "__main__":
    main()
