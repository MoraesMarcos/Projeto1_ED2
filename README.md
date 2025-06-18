📦 HashSimPy  
Ferramenta de linha de comando (CLI) para verificação de similaridade textual entre documentos, utilizando a técnica de **MinHashing** e estruturas de dados eficientes em Python. Ideal para tarefas como detecção de plágio, agrupamento de textos semelhantes e identificação de duplicatas.

🔍 Descrição  
Este projeto implementa um verificador de similaridade textual baseado em MinHash, permitindo comparar documentos de forma rápida e com menor custo computacional que o cálculo exato do índice de Jaccard.

🧠 Conceitos Abordados  

- **Pré-processamento de texto**: limpeza, padronização e remoção de ruído textual usando expressões regulares.
- **Shingling**: divisão do texto em *k*-shingles, substrings de tamanho fixo.
- **MinHashing**: algoritmo para geração de assinaturas compactas dos documentos usando múltiplas funções hash simuladas.
- **Índice de Similaridade**: estimativa baseada em quantos hashes coincidem entre dois documentos.

🔧 Operações Essenciais

- `ler_arquivo(path)`: leitura do arquivo `.txt`.
- `preprocessar(texto)`: limpa e prepara o texto.
- `gerar_shingles(texto, k)`: transforma o texto em conjunto de *shingles*.
- `assinatura(shingles)`: gera a assinatura MinHash.
- `comparar_assinaturas(sig1, sig2)`: retorna a similaridade estimada.

🧱 Arquitetura de Módulos

| Módulo           | Função Principal                                  |
|------------------|---------------------------------------------------|
| `leitura.py`     | Lê arquivos de texto                              |
| `preprocessamento.py` | Limpa e padroniza o texto                     |
| `shingling.py`   | Gera os *shingles* a partir do texto              |
| `minhash.py`     | Cria assinaturas MinHash                          |
| `comparador.py`  | Compara assinaturas para estimar similaridade     |
| `cli.py`         | Interface de linha de comando com argparse        |

📋 Plano de Tarefas

| Tarefa                                      | Responsável         | Status         |
|--------------------------------------------|----------------------|----------------|
| Estudar os conceitos (Hash, Shingle, etc)  | Equipe               | ✅ Concluído   |
| Criar repositório e estrutura de pastas    | Aluno - Marcos       | ✅ Concluído   |
| Implementar leitura de arquivos            | Aluno - Marcos       | 🔄 Em andamento   |
| Implementar pré-processamento              | Aluno - Marcos       | 🔄 Em andamento   |
| Implementar geração de shingles            | Aluno - Marcos       | 🔄 Em andamento   |
| Implementar MinHash                        | Aluno - Marcos       | 🔄 Em andamento   |
| Implementar função de comparação           | Aluno - Marcos       | 🔄 Em andamento   |
| Desenvolver interface CLI                  | Aluno - Marcos       | 🔄 Em andamento   |
| Testar com casos reais e ajustar CLI       | Aluno - Marcos       | 🔄 Em andamento |
| Criar README completo                      | Aluno - Marcos       | ✅ Concluído   |
| Criar slides da apresentação               | Aluno - Marcos       | 🔄 Em andamento |

📎 Exemplo de uso

```bash
python cli.py doc1.txt doc2.txt --k 5 --n 100
