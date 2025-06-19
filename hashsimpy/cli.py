import argparse
from leitura import ler_arquivo
from preprocessamento import preprocessar
from shingling import gerar_shingles
from minHash import MinHash
from comparador import comparar_assinaturas


def main():
    parser = argparse.ArgumentParser(
        description="📦 HashSimPy - Verificador de Similaridade Textual usando MinHash"
    )

    parser.add_argument(
        "arquivo1",
        help="Caminho do primeiro arquivo de texto (.txt)"
    )
    parser.add_argument(
        "arquivo2",
        help="Caminho do segundo arquivo de texto (.txt)"
    )
    parser.add_argument(
        "--k",
        type=int,
        default=5,
        help="Tamanho dos shingles (padrão: 5)"
    )
    parser.add_argument(
        "--hashes",
        type=int,
        default=100,
        help="Número de funções hash simuladas para MinHash (padrão: 100)"
    )

    args = parser.parse_args()

    print("\n🚀 Iniciando comparação de documentos...\n")

    try:
        # Ler arquivos
        texto1 = ler_arquivo(args.arquivo1)
        texto2 = ler_arquivo(args.arquivo2)

        # Pré-processamento
        texto1 = preprocessar(texto1)
        texto2 = preprocessar(texto2)

        # Gerar shingles
        shingles1 = gerar_shingles(texto1, args.k)
        shingles2 = gerar_shingles(texto2, args.k)

        print("📄 Shingles gerados:")
        print(f" - Documento 1: {len(shingles1)} shingles")
        print(f" - Documento 2: {len(shingles2)} shingles\n")

        # Gerar assinaturas MinHash
        minhash = MinHash(num_hashes=args.hashes)
        assinatura1 = minhash.assinatura(shingles1)
        assinatura2 = minhash.assinatura(shingles2)

        # Comparar assinaturas
        similaridade = comparar_assinaturas(assinatura1, assinatura2)

        print("🔍 Resultado da comparação:")
        print(f" - Similaridade estimada: {similaridade * 100:.2f}%\n")

    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
