ocorrencias = []
ordem = []

def gerar_id(nome):
    soma = 0

    for letra in nome:
        soma = soma + ord(letra)

    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)


def cadastrar_ocorrencia():
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
    print("\nBUSCAR OCORRÊNCIA")
    id_busca = input("Digite o ID para buscar: ")
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


while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar ocorrência")
    print("2 - Listar ocorrências")
    print("3 - Buscar ocorrência por ID")
    print("4 -")
    print("5 -")
    print("6 -")
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
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")