

class Fornecedor:

    def __init__(self,idFornecedor:int,nome:str):
        self.__idFornecedor = idFornecedor
        self.__nome = nome


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idFornecedor(self):
        return self.__idFornecedor

    def __eq__(self, other):
        return self.__idFornecedor==other.idFornecedor

    def fornecedor(self):
        return {
            "idFornecedor": self.__idFornecedor,
            "nome": self.__nome,
        }

    @staticmethod
    def dictToObject(data):
        return Fornecedor(
            data["idFornecedor"],
            data["nome"]
        )