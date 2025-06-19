from hashsimpy.leitura import ler_arquivo
from hashsimpy.preprocessamento import preprocessar
from hashsimpy.shingling import gerar_shingles


def main():
    caminho = "exemplo.txt"
    texto = ler_arquivo(caminho)
    texto_limpo = preprocessar(texto)
    shingles = gerar_shingles(texto_limpo, k=5)

    print("Texto pré-processado:")
    print(texto_limpo)
    print("\nShingles gerados:")
    print(shingles)
    print(f"\nTotal de shingles: {len(shingles)}")

if __name__ == "__main__":
    main()
