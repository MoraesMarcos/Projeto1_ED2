# 📦 HashTablePy

A Tabela Hash é uma estrutura de dados que permite a associação eficiente entre chaves e valores, usando uma função de hash para mapear a chave a um índice dentro de um array. Essa estrutura é amplamente usada em dicionários, caches, indexadores de bancos de dados, etc.

## 🔍 Descrição

Este projeto implementa uma estrutura de dados conhecida como **Tabela Hash** (ou **Mapa Hash**), permitindo inserir, buscar e remover pares chave-valor de forma eficiente.

## 🧠 Conceitos Abordados

Função de Hash: converte uma chave (ex: string) em um número inteiro. Exemplo: hash(key) % tamanho.

Array Base (buckets): armazena os valores com base nos índices gerados pela função de hash.

Tratamento de Colisões: quando múltiplas chaves geram o mesmo índice, usa-se o Encadeamento Separado — uma lista em cada posição do array para armazenar múltiplos elementos.

Operações Essenciais:

- put(chave, valor): insere um novo par ou atualiza um existente.

- get(chave): busca o valor associado à chave.

- delete(chave): remove um par chave-valor.

## 🧱 Diagrama de Classe


      HashTable       

+----------------------+

 - bucketes: list                         
 - size: int                              
+----------------------+

 + _hash(key): int                       
 + put(key, value):                       
 + get(key):                              
 + delete(key):                           
 + __str__(): str                        

## 📋 Plano de Tarefas

| Tarefa                                 | Responsável    | Status          |
| -------------------------------------- | -------------- | --------------- |
| Estudar os conceitos de tabela hash    | Equipe         | ✅ Concluído    |
| Criar repositório no GitHub            | Aluno - Marcos | ✅ Concluído    |
| Estruturar o projeto (pasta, arquivos) | Aluno          | 🔄 Em andamento |
| Implementar método `_hash()`           | Aluno - Marcos | 🔄 Em andamento |
| Implementar `put(chave, valor)`        | Aluno          | 🔄 Em andamento |
| Implementar `get(chave)`               | Aluno          | 🔄 Em andamento |
| Implementar `delete(chave)`            | Aluno          | 🔄 Em andamento |
| Escrever README.md                     | Aluno - Marcos | ✅ Concluído    |
| Criar `main.py` com testes simples     | Aluno - Marcos | 🔄 Em andamento |
| Documentar planejamento da semana 1    | Aluno - Marcos | 🔄 Em andamento |

