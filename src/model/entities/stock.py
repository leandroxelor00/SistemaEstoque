

class Estoque:

    def __init__(self,idProd:int,quantidade:int):
        self.__idProd = idProd
        self.__quantidade = quantidade

    @property
    def idProd(self):
        return self.__idProd

    @property
    def quantidade(self):
        return self.__quantidade

    def addProd(self,quantidade:int):
        self.__quantidade += quantidade

    def removerProd(self,quantidade:int):
        self.__quantidade -= quantidade

    def estoque(self):
        return {
            "idProd": self.__idProd,
            "quantidade": self.__quantidade,
        }