# 📦 HashTablePy

A Tabela Hash é uma estrutura de dados que permite a associação eficiente entre chaves e valores, usando uma função de hash para mapear a chave a um índice dentro de um array. Essa estrutura é amplamente usada em dicionários, caches, indexadores de bancos de dados, etc.

## 🔍 Descrição

Este projeto implementa uma estrutura de dados conhecida como **Tabela Hash** (ou **Mapa Hash**), permitindo inserir, buscar e remover pares chave-valor de forma eficiente.

## 🧠 Conceitos Abordados

Função de Hash: converte uma chave (ex: string) em um número inteiro. Exemplo: hash(key) % tamanho.

Array Base (buckets): armazena os valores com base nos índices gerados pela função de hash.

Tratamento de Colisões: quando múltiplas chaves geram o mesmo índice, usa-se o Encadeamento Separado — uma lista em cada posição do array para armazenar múltiplos elementos.

Operações Essenciais:

put(chave, valor): insere um novo par ou atualiza um existente.

get(chave): busca o valor associado à chave.

delete(chave): remove um par chave-valor.
