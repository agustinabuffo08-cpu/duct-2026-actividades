from analizador import contar_frecuencias


def test_frecuencias_basico():
    resultado = contar_frecuencias("sol luna sol")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1


def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}


def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("Sol sol SOL")
    # TODO: completa la asercion que verifica que las tres variantes de
    # "sol" (con distintas mayusculas) se cuentan como la MISMA palabra,
    # gracias al .lower() de la funcion. El resultado deberia tener
    # "sol": 3
    assert resultado == {"sol": 3}


def test_frecuencias_espacios_de_mas():
    # Caso de borde: espacios al principio, al final y repetidos entre
    # palabras, tabulaciones y saltos de linea. Como .split() sin
    # argumentos corta por cualquier cantidad de espacios en blanco,
    # no deberian aparecer palabras vacias ("") en el resultado.
    resultado = contar_frecuencias("   sol    luna \t sol\n\nluna  sol   ")
    assert resultado == {"sol": 3, "luna": 2}
    assert "" not in resultado
