# Projeto1_ED2

📌 Tabela Hash (Hash Table):
Uma estrutura que associa chaves a valores através de uma função de hash que transforma a chave em um índice. Ideal para operações rápidas de inserção, busca e remoção.

📌 Função de Hash:
Transforma uma chave (como uma string ou número) em um índice de array. Usaremos a função embutida hash() do Python, aplicada com módulo (% tamanho) para garantir que o índice esteja dentro do tamanho do array.

📌 Colisões:
Quando duas chaves diferentes geram o mesmo índice. Estratégias para tratar:

Encadeamento Separado (Separate Chaining): Cada posição do array aponta para uma lista com os pares chave-valor que colidiram nesse índice.

📌 Fator de Carga:
Define a razão entre o número de elementos e o tamanho do array. Um alto fator de carga aumenta colisões, exigindo possível redimensionamento.

