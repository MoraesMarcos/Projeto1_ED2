import re

def preprocessar(texto):
    texto = texto.lower()
    texto = re.sub(r'[^a-z\s]', '', texto)
    return texto
