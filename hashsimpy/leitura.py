import os

def ler_arquivo(caminho):
    """
    Lê o conteúdo de um arquivo de texto.

    Parâmetros:
        caminho (str): Caminho para o arquivo .txt

    Retorna:
        str: Conteúdo do arquivo como uma única string

    Lança:
        FileNotFoundError: Se o arquivo não existir
        IOError: Se ocorrer erro de leitura
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo '{caminho}' não encontrado.")
    
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        raise IOError(f"Erro ao ler o arquivo: {e}")
