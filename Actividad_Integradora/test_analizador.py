from analizador import contar_frecuencias, leer_archivo


def test_frecuencias_basico():
    resultado = contar_frecuencias("sol luna sol")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1


def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}


def test_frecuencias_mayusculas():
    # "Sol", "sol" y "SOL" se cuentan como la misma palabra
    resultado = contar_frecuencias("Sol sol SOL")
    assert resultado == {"sol": 3}


def test_frecuencias_puntuacion():
    # Los signos pegados a una palabra no la convierten en otra distinta
    resultado = contar_frecuencias("¡Sol, luna; sol!")
    assert resultado == {"sol": 2, "luna": 1}


def test_frecuencias_sin_stopwords():
    # Las palabras vacias ("el", "y", "la") no se cuentan
    resultado = contar_frecuencias("el sol y la luna")
    assert resultado == {"sol": 1, "luna": 1}


def test_archivo_inexistente():
    # Si el archivo no existe, leer_archivo no se rompe: devuelve None
    resultado = leer_archivo("archivo_que_no_existe.txt")
    assert resultado is None
