import heapq
from collections import deque

ocorrencias = []
ordem = []

fila_chegada = deque()
heap_prioridade = []
contador_heap = 0

class BST:
    def __init__(self, chave, ocorrencia):
        self.chave = chave
        self.ocorrencia = ocorrencia
        self.esquerda = None
        self.direita = None

class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, ocorrencia):
        if self.raiz is None:
            self.raiz = BST(chave, ocorrencia)
        else:
            self._inserir(self.raiz, chave, ocorrencia)

    def _inserir(self, no, chave, ocorrencia):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = BST(chave, ocorrencia)
            else:
                self.inserir(no.esquerda, chave, ocorrencia)
        elif chave > no.chave:
            if no.direita is None:
                no.direita = BST(chave, ocorrencia)
            else:
                self._inserir(no.direita, chave, ocorrencia)
        else:
            if isinstance(no.ocorrencia, list):
                no.ocorrencia.append(ocorrencia)
            else:
                no.ocorrencia = [no.ocorrencia, ocorrencia]

    def buscar(self, chave):
        return self.buscar(self.raiz, chave)
    
    def _buscar(self, no, chave):
        if no is None:
            return None
        if chave == no.chave:
            return no.ocorrencia
        elif chave < no.chave:
            return self._buscar(no.esquerda, chave)
        else:
            return self._buscar(no.direira, chave)
        
arvore_ids = ArvoreBST()

def extrair_codigo_id(id_ocorrencia):
    try:
        return int(id_ocorrencia.split("-")[-1])
    except (ValueError, IndexError):
        return 0

hash_nome = {}
hash_tipo = {}

def hash_inserir(dicionario, chave, ocorrencia):
    chave = chave.lower().strip()
    if chave not in dicionario:
        dicionario[chave] = []
    dicionario[chave].append(ocorrencia)

def gerar_id(nome):
    soma = 0

    for letra in nome:
        soma = soma + ord(letra)

    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)


def cadastrar_ocorrencia():
    global contador_heap
    print("\nCADASTRAR OCORRÊNCIA")

    nome = input("Nome do requisitante: ")
    id_ocorrencia = gerar_id(nome)

    tipo = input("Tipo da ocorrência: ")
    descricao = input("Descrição: ")
    prioridade = int(input("Prioridade de 1 a 5: "))
    status = "Aberto"

    ordem.append(id_ocorrencia)

    while (prioridade < 1 or prioridade > 5):
      print("\nPrioridade inválida\n")
      prioridade = int(input("Prioridade de 1 a 5: "))

    nova_ocorrencia = {
        "id": id_ocorrencia,
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "prioridade": prioridade,
        "ordem": len(ordem),
        "status": status
    }

    ocorrencias.append(nova_ocorrencia)

    fila_chegada.append(nova_ocorrencia)
    heapq.heappush(heap_prioridade, (-prioridade, contador_heap, nova_ocorrencia))
    contador_heap += 1

    arvore_ids.inserir(extrair_codigo_id(id_ocorrencia), nova_ocorrencia)

    hash_inserir(hash_nome, nome, nova_ocorrencia)
    hash_inserir(hash_tipo, nome, nova_ocorrencia)

    print("\n=== Ocorrência cadastrada! ====")
    print("ID:", id_ocorrencia)
    print("Nome:", nome)
    print("Tipo:", tipo)
    print("Descrição:", descricao)
    print("Prioridade:", prioridade)
    print("Ordem de chegada:", len(ordem))
    print("Status:", status)

def listar_ocorrencias():
    print("\nLISTA DE OCORRÊNCIAS")
    if not ocorrencias:
        print("Nenhuma ocorrência cadastrada.")
    else:
        for o in ocorrencias:
            print(f"ID: {o['id']} | Nome: {o['nome']} | Tipo: {o['tipo']} | Prioridade: {o['prioridade']}")


def buscar_ocorrencia_id():
    print("\nBUSCAR OCORRÊNCIA POR ID")
    id_busca = input("Digite o ID para buscar: ").strip()
    
    codigo = extrair_codigo_id(id_busca)
    resultado = arvore_ids.buscar(codigo)

    if resultado is None:
        print(f"Nenhuma ocorrencia encontrada com o ID: {id_busca}")
        return
    
    encontrada = False
    for o in ocorrencias:
        if o['id'] == id_busca:
            print("\nOcorrência encontrada:")
            print("ID:", o['id'])
            print("Nome:", o['nome'])
            print("Tipo:", o['tipo'])
            print("Descrição:", o['descricao'])
            print("Prioridade:", o['prioridade'])
            encontrada = True
            break
    if not encontrada:
        print(f"Nenhuma ocorrência encontrada com o ID: {id_busca}")

def atender_ordem_chegada():
    print("\n ATENDER POR ORDEM DE CHEGADA")

    while fila_chegada:
        ocorrencia = fila_chegada.popleft()
        if ocorrencia["status"] == "Aberto":
            ocorrencia["status"] == "Atendido"
            print("\nOcorrência atendida:")
            print("ID:", ocorrencia['id'])
            print("Nome:", ocorrencia['nome'])
            print("Tipo:", ocorrencia['tipo'])
            print("Descrição", ocorrencia['descricao'])
            print("Prioridade:", ocorrencia['prioridade'])
            return
        
    print("Não há ocorrencias em aberto para atender")

def atender_maior_prioridade():
    print("\nATENDER POR MAIOR PRIORIDADE")

    while heap_prioridade:
        prioridade_neg, _, ocorrencia = heap_prioridade(heap_prioridade)
        if ocorrencia["status"] == "Aberto":
           ocorrencia["status"] == "Atendido"
           print("\nOcorrência atendida:")
           print("ID:", ocorrencia['id'])
           print("Nome:", ocorrencia['nome'])
           print("Tipo:", ocorrencia['tipo'])
           print("Descrição:", ocorrencia['descricao'])
           print("Prioridade:", -prioridade_neg)
           return
        
    print("Não há ocorrencias em baerto para atender")

def buscar_nome_ou_tipo():
    print("\nBUSCAR OCORRÊNCIAS POR NOME OU TIPO")
    print("1 - Buscar por nome")
    print("2 - Buscar por tipo")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        chave = input("Digite o nome do requisitante: ").strip().lower()
        resultados = hash_nome.get(chave, [])
    elif escolha == "2":
        chave = input("Digite o tipo da ocorrência: ").strip().lower()
        resultados = hash_tipo.get(chave, [])
    else:
        print("Opção inválida.")
        return
    
    if not resultados:
        print("Nenhuma ocorrência encontrada")
        return
    
    print(f"\n{len(resultados)} ocorrência(s) encontrada(s):")
    for o in resultados:
        print(f"ID: {o['id']} | Nome: {o['nome']} | Tipo: {o['tipo']} | Prioridade: {o['prioridade']}")

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar ocorrência")
    print("2 - Listar ocorrências")
    print("3 - Buscar ocorrência por ID")
    print("4 - Atender pela ordem de chegada")
    print("5 - Atender pela maior prioridade")
    print("6 - Buscar ocorrências por nome ou tipo")
    print("7 -")
    print("8 -")
    print("9 -")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_ocorrencia()
    elif opcao == "2":
        listar_ocorrencias()
    elif opcao == "3":
        buscar_ocorrencia_id()
    elif opcao == "4":
        atender_ordem_chegada()
    elif opcao == "5":
        atender_maior_prioridade()
    elif opcao == "6":
        buscar_nome_ou_tipo
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")