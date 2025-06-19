from hashsimpy.leitura import ler_arquivo
from hashsimpy.preprocessamento import preprocessar
from hashsimpy.shingling import gerar_shingles

def main():
    caminho = "exemplo.txt"
    try:
        texto = ler_arquivo(caminho)
        texto_limpo = preprocessar(texto)
        shingles = gerar_shingles(texto_limpo, k=5)

        print("📄 Texto pré-processado:")
        print(texto_limpo)

        print("\n🧩 Shingles gerados:")
        for s in sorted(shingles):
            print(f"- {s}")

        print(f"\n🔢 Total de shingles: {len(shingles)}")

    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")

if __name__ == "__main__":
    main()