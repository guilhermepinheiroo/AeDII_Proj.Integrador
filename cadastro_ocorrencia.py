import datetime

cadastro_ocorrencias = []

def cadastrar_ocorrencia(nome, tipo, status, prioridade, descricao, data_hora):

    ocorrencia = {
        "id_ocorrencia": len(cadastro_ocorrencias) + 1,
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "data_hora": datetime.now(),
        "prioridade": prioridade,
        "status": status

    }

    cadastro_ocorrencias.append(ocorrencia)

def listar_ocorrencias():