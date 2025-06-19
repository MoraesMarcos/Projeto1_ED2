import re
from unidecode import unidecode

def preprocessar(texto):
    """
    Limpa e padroniza o texto, removendo acentos e caracteres não alfabéticos.

    Parâmetros:
        texto (str): Texto original

    Retorna:
        str: Texto em minúsculas, sem acentos, pontuação ou números
    """
    if not isinstance(texto, str):
        raise ValueError("O argumento 'texto' deve ser uma string.")

    # Converte para minúsculas e remove acentos
    texto = unidecode(texto.lower())

    # Remove tudo que não for letra ou espaço
    texto = re.sub(r'[^a-z\s]', '', texto)

    # Remove espaços duplicados e espaços nas bordas
    texto = re.sub(r'\s+', ' ', texto).strip()

    return texto
