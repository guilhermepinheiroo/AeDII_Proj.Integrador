class HashTable:
    def __init__(self, size = 10) -> None:
        self.size = size
        self.tabela = [ [] for _ in range(size)]

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
