import os

def ler_arquivo(caminho):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo {caminho} não encontrado.")
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()
