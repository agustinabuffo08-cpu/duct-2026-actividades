# Analizador de frecuencias de palabras

`analizador.py` lee `texto_integradora.txt`, cuenta cuántas veces aparece cada palabra usando un diccionario (sin distinguir mayúsculas, sin signos de puntuación y sin palabras vacías como "el", "de" o "que"), muestra en pantalla las 10 más frecuentes y guarda un gráfico de barras con ellas en `grafico_frecuencias.png`. Si el archivo de texto no existe, muestra un mensaje de error en lugar de interrumpirse.

**Requisitos:** Python 3 y las bibliotecas `matplotlib` (para el gráfico) y `pytest` (para las pruebas), listadas en `requirements.txt`. Se instalan con:

    python -m pip install -r requirements.txt

**Cómo ejecutarlo:** desde la carpeta `Actividad_Integradora`, correr `python analizador.py`.

**Pruebas:** desde la misma carpeta, correr `python -m pytest`. `test_analizador.py` verifica un caso básico, un texto vacío, mayúsculas y minúsculas, signos de puntuación, palabras vacías y el caso de archivo inexistente.
