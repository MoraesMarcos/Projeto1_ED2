def gerar_shingles(texto, k=5):
    return set(texto[i:i+k] for i in range(len(texto) - k + 1))
