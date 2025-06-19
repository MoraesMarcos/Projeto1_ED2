def gerar_shingles(texto, k=5):
    """
    Gera um conjunto de k-shingles (substrings de tamanho k) a partir do texto.

    Parâmetros:
        texto (str): Texto pré-processado
        k (int): Tamanho de cada shingle

    Retorna:
        set: Conjunto de shingles únicos
    """
    if not isinstance(texto, str):
        raise ValueError("O argumento 'texto' deve ser uma string.")
    if not isinstance(k, int) or k <= 0:
        raise ValueError("O tamanho do shingle 'k' deve ser um inteiro positivo.")
    if len(texto) < k:
        return set()

    return set(texto[i:i+k] for i in range(len(texto) - k + 1))