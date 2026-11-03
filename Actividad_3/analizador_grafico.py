import os
import string

import matplotlib.pyplot as plt

# Lista de stopwords de la Secuencia B (ejercicio_2.py), ampliada con otras
# palabras vacias frecuentes del español
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
    "sin", "sobre", "entre", "hasta", "desde", "él", "ella",
}

# Formas de una misma palabra que se cuentan juntas: {forma: palabra normalizada}
NORMALIZAR = {
    "libros": "libro",
    "hexágonos": "hexágono",
    "hombres": "hombre",
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
    for signo in string.punctuation + "¿¡«»“”‘’—–…":
        texto = texto.replace(signo, "")
    return texto.split()


def analizar_y_graficar(ruta, top_n=10):
    """
    Lee un archivo de texto, cuenta la frecuencia de cada palabra
    (sin stopwords y con plurales normalizados) y genera un grafico de barras horizontales con
    las top_n palabras mas frecuentes.

    Parametros:
        ruta (str): ruta al archivo de texto a analizar
        top_n (int): cantidad de palabras a graficar

    Retorna:
        None (genera y guarda el grafico)
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    palabras_texto = tokenizar(texto)

    frecuencias = {}
    for palabra in palabras_texto:
        palabra = NORMALIZAR.get(palabra, palabra)
        if palabra not in STOP_WORDS:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]

    # Comprension de listas: separa las tuplas (palabra, frecuencia) en dos listas
    palabras = [par[0] for par in top10]
    valores = [par[1] for par in top10]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes (sin stopwords)")
    plt.xlabel("Frecuencia")
    plt.tight_layout()

    # El grafico se guarda en la misma carpeta que el archivo de texto
    carpeta = os.path.dirname(os.path.abspath(ruta))
    plt.savefig(os.path.join(carpeta, "grafico_frecuencias.png"), dpi=150, bbox_inches="tight")
    plt.show()


def main():
    # texto.txt se busca en la misma carpeta que este script
    carpeta_script = os.path.dirname(os.path.abspath(__file__))
    analizar_y_graficar(os.path.join(carpeta_script, "texto.txt"))


if __name__ == "__main__":
    main()
