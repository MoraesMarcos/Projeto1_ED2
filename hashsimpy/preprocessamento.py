import re

def preprocessar(texto):
    """
    Limpa e padroniza o texto, removendo caracteres não alfabéticos.

    Parâmetros:
        texto (str): Texto original

    Retorna:
        str: Texto em minúsculas, sem números ou pontuação
    """
    if not isinstance(texto, str):
        raise ValueError("O argumento 'texto' deve ser uma string.")

    texto = texto.lower()
    texto = re.sub(r'[^a-z\s]', '', texto)  # Mantém apenas letras e espaços
    texto = re.sub(r'\s+', ' ', texto).strip()  # Remove espaços duplicados
    return texto
