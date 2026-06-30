# Sistema de Gerenciamento de Ocorrências Acadêmicas

Projeto desenvolvido para a disciplina de **Algoritmos e Estruturas de Dados II (AED II)**.

O objetivo é demonstrar a aplicação integrada das estruturas de dados estudadas em aula para o gerenciamento de ocorrências acadêmicas.

---


## Como executar o projeto

### Pré-requisitos

- Python 3 instalado.

### Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### Entrar na pasta

```bash
cd nome-do-projeto
```

### Executar

```bash
python main.py
```

---

## Funcionalidades

O sistema possui um menu interativo executado no terminal.

### Funcionalidades implementadas

- Cadastro de ocorrências
- Listagem de ocorrências
- Atendimento por ordem de chegada
- Atendimento por prioridade
- Busca por ID
- Busca por nome
- Busca por tipo
- Histórico de ações

---

## Dados de uma ocorrência

Cada ocorrência possui:

- ID
- Nome do solicitante
- Tipo
- Descrição
- Prioridade (1 a 5)
- Ordem de chegada
- Status

---

# Fluxo do cadastro

Ao cadastrar uma nova ocorrência, o sistema realiza automaticamente:

1. Adiciona a ocorrência na lista geral.
2. Insere a ocorrência na fila de atendimento.
3. Insere a ocorrência na árvore BST.
4. Insere a ocorrência na heap de prioridade.
5. Insere a ocorrência na hash table.
6. Registra a ação na pilha de histórico.

---

# Estrutura do menu

```text
1 - Cadastrar ocorrência
2 - Listar ocorrências
3 - Buscar ocorrência por ID
4 - Atender pela ordem de chegada
5 - Atender pela maior prioridade
6 - Buscar ocorrências por nome ou tipo
7 - Ver histórico
0 - Sair
```

---



# Perguntas obrigatórias

## Onde foi utilizada a fila?


---

## Onde foi utilizada a pilha?
    A pilha foi usada no histórico, realizando o LIFO(Last In, First Out) para empilhar o chamado e usando o .append para empilhar e .pop para desempilhar simulando um CTRL Z.


---

## Onde foi utilizada a árvore?


---

## Onde foi utilizada a heap?


---

## Onde foi utilizada a hash table?


---

## Qual algoritmo de ordenação foi implementado?


---

## Qual estrutura foi mais adequada para busca rápida?


---

## Qual estrutura foi mais adequada para atendimento por prioridade?


---

## Qual foi a maior dificuldade do grupo?

**Resposta do grupo.**

---

# Integrantes

- Christian Pieper
- Guilherme Pinheiro
- Luis Dos Santos
- Otavio Vieira
- Pablo Knapp
