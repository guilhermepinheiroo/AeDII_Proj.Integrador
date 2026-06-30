# PROJETO INTEGRADOR AEDII <br><br> Sistema de Gerenciamento de Ocorrências Acadêmicas

Projeto desenvolvido para a disciplina de **Algoritmos e Estruturas de Dados II (AEDII)**.

O objetivo é demonstrar a aplicação integrada das estruturas de dados estudadas em aula para o gerenciamento de ocorrências acadêmicas.

---


## Como executar o projeto

### Pré-requisitos

- Python 3 instalado.

### Clonar o repositório

```bash
git clone https://github.com/guilhermepinheiroo/AeDII_Proj.Integrador.git
```

### Entrar na pasta

```bash
cd AeDII_Proj.Integrador
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
Foi utilizada na variável `fila_chegada` em `main.py` para gerenciar o atendimento de ocorrências pela ordem de chegada, utilizando o princípio (FIFO - *First In, First Out*) na função `atender_ordem_chegada`.

---

## Onde foi utilizada a pilha?
Na variável `historico` em `main.py` para manter o histórico de ocorrências e permitir desfazer a última ação registrada na função `desfazer_ultima_acao`, utilizando o princípio (LIFO - *Last In, First Out*).

---

## Onde foi utilizada a árvore?
Foi utilizada uma árvore binária de busca nas classes `BST` e `ArvoreBST` em `main.py` (`arvore_ids`), servindo para indexar e buscar as ocorrências a partir do código numérico extraído do ID.

---

## Onde foi utilizada a heap?
Foi utilizada na variável `heap_prioridade` em `main.py` (usando o módulo nativo `heapq`), para gerenciar as ocorrências e realizar o atendimento com base no nível de prioridade (utilizando prioridade negativa para simular uma Max-Heap e um contador de desempate) na função `atender_maior_prioridade`.

---

## Onde foi utilizada a hash table?
Foi utilizada nos dicionários nativos `hash_nome` e `hash_tipo` em `main.py` para indexação e busca de ocorrências por nome ou tipo. Além disso, uma tabela hash própria com resolução de colisões por encadeamento foi modelada no arquivo `hash_table.py`.

---

## Qual algoritmo de ordenação foi implementado?
A ordenação é gerenciada e mantida de forma dinâmica pela estrutura de **Heap** (ordenação de prioridade) e pela **Árvore BST** (ordenação de IDs).

---

## Qual estrutura foi mais adequada para busca rápida?
A **Hash Table** pois permite buscas por correspondência exata em tempo médio constante $O(1)$.

---

## Qual estrutura foi mais adequada para atendimento por prioridade?
A **Heap** pois permite a recuperar o elemento de maior prioridade em tempo $O(\log n)$ a cada inserção ou remoção.

---

## Qual foi a maior dificuldade do grupo?

A nossa maior dificuldade foi sincronizar o estado das ocorrências de forma consistente entre todas as estruturas de dados. Como um mesmo registro é compartilhado entre todas elas, garantir que ações como o atendimento por ordem de chegada ou por prioridade e a funcionalidade de desfazer ocorressem em tempo real sem gerar inconsistências ou conflitos de dados foi o maior desafio do projeto.

---

# Integrantes

- Christian Pieper - [@PieperChristian](https://github.com/PieperChristian)
- Guilherme Pinheiro - [@guilhermepinheiroo](https://github.com/guilhermepinheiroo)
- Luis Matheus - [@luiszr21](https://github.com/luiszr21)
- Otavio Vieira - [@otaviovieiraa](https://github.com/otaviovieiraa)
- Pablo Knapp - [@pabloknapp](https://github.com/pabloknapp)
