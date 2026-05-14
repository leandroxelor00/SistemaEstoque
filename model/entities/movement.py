from datetime import datetime as dt

class Movimentacao:

    def __init__(self,idMovimento:int,idProd:int,quantidade:int,idFunc:int,idFornecedor:int,tipo:str):
        self.__idMovimento = idMovimento
        self.__idProd = idProd
        self.__quantidade = quantidade
        self.__idFunc = idFunc
        self.__idFornecedor = idFornecedor
        self.__tipo = tipo

    @property
    def idMov(self):
        return self.__idMovimento

    @property
    def dataMov(self):
        return self.__dataMov

    # def entrarEstoque(self,idProd:int,quantidade:int):
    #     self.__idProd = idProd
    #     self.__quantidade = quantidade
    #
    # def saidaEstoque(self,idProd:int,quantidade:int,numeroSala:int):
    #     self.__idProd = idProd
    #     self.__quantidade = quantidade
    #     self.__numeroSala = numeroSala

    def movimento(self):
        return {
            "idMovimento": self.__idMovimento,
            "idProd": self.__idProd,
            "quantidade": self.__quantidade,
            "idFunc": self.__idFunc,
            "idFornecedor": self.__idFornecedor,
            "tipo": self.__tipo,
        }
