

class Estoque:

    def __init__(self,idEstoque:int,idProd:int,quantidade:int):
        self.__idEstoque = idEstoque
        self.__idProd = idProd
        self.__quantidade = quantidade

    @property
    def idProd(self):
        return self.__idProd

    @property
    def idEstoque(self):
        return self.__idEstoque

    @property
    def quantidade(self):
        return self.__quantidade

    def addProd(self,quantidade:int):
        self.__quantidade += quantidade

    def removerProd(self,quantidade:int):
        self.__quantidade -= quantidade

    def estoque(self):
        return {
            "idEstoque": self.__idEstoque,
            "idProd": self.__idProd,
            "quantidade": self.__quantidade,
        }

    @staticmethod
    def dictToObject(data):
        return Estoque(
            data["idEstoque"],
            data["idProd"],
            data["quantidade"]
        )