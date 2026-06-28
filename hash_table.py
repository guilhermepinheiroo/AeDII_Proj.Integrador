class HashTable:
    def __init__(self, size = 7) -> None:
        self.size = size
        self.tabela = [ [] for _ in range(size)]
        self.historico = []  # Pilha LIFO (Last In, First Out) para os comandos de Desfazer

    def funcao_hash(self, chave: str | int | float) -> int:
        lista_caracteres = []

        if isinstance(chave, str):
            lista_caracteres = list(chave)
        elif isinstance(chave, (int, float)):
            lista_caracteres = list(str(chave))

        tamanho_lista = len(lista_caracteres)
        imagem_hash = 0
        for posicao, caractere in enumerate(lista_caracteres):
          potencia = 256 ** ( tamanho_lista - posicao - 1 )
          imagem_hash += ord(caractere) * potencia

        primo = 2 ** 13 - 1
        imagem_hash = imagem_hash % primo

        return imagem_hash % self.size

    def inserir(self, chave: str, valor: dict, registrar_historico: bool = True) -> None:
        indice = self.funcao_hash(chave)
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                if registrar_historico:
                    # Guarda a ação inversa: atualizar de volta pro valor que existia (v)
                    self.historico.append(("atualizar", chave, v))
                self.tabela[indice][i] = (chave, valor)
                return
        
        if registrar_historico:
            # Guarda a ação inversa: apagar a chave que acabou de ser criada
            self.historico.append(("inserir", chave, None))
            
        self.tabela[indice].append((chave, valor))

    def buscar(self, chave: str) -> dict | None:
        indice = self.funcao_hash(chave)
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        return None  

    def deletar(self, chave: str, registrar_historico: bool = True) -> bool:
        indice = self.funcao_hash(chave)
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                if registrar_historico:
                    # Guarda a ação inversa: reinserir o valor que foi deletado (v)
                    self.historico.append(("deletar", chave, v))
                del self.tabela[indice][i]
                return True
        return False

    def desfazer(self) -> bool:
        if not self.historico:
            return False  # Nada no histórico para ser desfeito
            
        acao, chave, valor = self.historico.pop() # Pega sempre a ÚLTIMA ação realizada
        
        if acao == "inserir":
            # Se for tentar desfazer uma criação, nós deletamos a chave
            self.deletar(chave, registrar_historico=False)
        elif acao == "atualizar":
            # Se tentarmos desfazer uma atualização, devolvemos pra estado anterior
            self.inserir(chave, valor, registrar_historico=False)
        elif acao == "deletar":
            # Se tentarmos desfazer um delete, nós reinserimos o que foi apagado
            self.inserir(chave, valor, registrar_historico=False)
            
        return True
