### 📦 HashSimPy  
Ferramenta de linha de comando (CLI) para verificação de similaridade textual entre documentos, utilizando a técnica de **MinHashing** e estruturas de dados eficientes em Python. Ideal para tarefas como detecção de plágio, agrupamento de textos semelhantes e identificação de duplicatas.

### 🔍 Descrição  
Este projeto implementa um verificador de similaridade textual baseado em MinHash, permitindo comparar documentos de forma rápida e com menor custo computacional que o cálculo exato do índice de Jaccard.

### 🧠 Conceitos Abordados  

- **Pré-processamento de texto**: limpeza, padronização e remoção de ruído textual usando expressões regulares.
- **Shingling**: divisão do texto em *k*-shingles, substrings de tamanho fixo.
- **MinHashing**: algoritmo para geração de assinaturas compactas dos documentos usando múltiplas funções hash simuladas.
- **Índice de Similaridade**: estimativa baseada em quantos hashes coincidem entre dois documentos.

### 🔧 Operações Essenciais

- `ler_arquivo(path)`: leitura do arquivo `.txt`.
- `preprocessar(texto)`: limpa e prepara o texto.
- `gerar_shingles(texto, k)`: transforma o texto em conjunto de *shingles*.
- `assinatura(shingles)`: gera a assinatura MinHash.
- `comparar_assinaturas(sig1, sig2)`: retorna a similaridade estimada.

### 🧱 Arquitetura de Módulos

| Módulo           | Função Principal                                  |
|------------------|---------------------------------------------------|
| `leitura.py`     | Lê arquivos de texto                              |
| `preprocessamento.py` | Limpa e padroniza o texto                     |
| `shingling.py`   | Gera os *shingles* a partir do texto              |
| `minhash.py`     | Cria assinaturas MinHash                          |
| `comparador.py`  | Compara assinaturas para estimar similaridade     |
| `cli.py`         | Interface de linha de comando com argparse        |

### 📋 Plano de Tarefas

| Tarefa                                      | Responsável         | Status         |
|--------------------------------------------|----------------------|----------------|
| Estudar os conceitos (Hash, Shingle, etc)  | Equipe               | ✅ Concluído   |
| Criar repositório e estrutura de pastas    | Aluno - [Marcos](https://github.com/MoraesMarcos)       | ✅ Concluído   |
| Implementar leitura de arquivos            | Aluno -[Marcos](https://github.com/MoraesMarcos)        | ✅ Concluído   |
| Implementar pré-processamento              | Aluno - [Marcos](https://github.com/MoraesMarcos)       | ✅ Concluído   |
| Implementar geração de shingles            | Aluno - [Marcos](https://github.com/MoraesMarcos)       | ✅ Concluído   |
| Implementar MinHash                        | Aluno - [Douglas](https://github.com/douglasteyh)       | ✅ Concluído   |
| Implementar função de comparação           | Aluno - [Douglas](https://github.com/douglasteyh)       | ✅ Concluído   |
| Desenvolver interface CLI                  | Aluno - [Douglas](https://github.com/douglasteyh)       | ✅ Concluído   |
| Testar com casos reais e ajustar CLI       | Aluno - Nome       | 🔄 Em andamento |
| Criar README completo                      | Aluno - [Marcos](https://github.com/MoraesMarcos)       | ✅ Concluído   |
| Criar slides da apresentação               | Aluno - [Marcos](https://github.com/MoraesMarcos)       | 🔄 Em andamento |
