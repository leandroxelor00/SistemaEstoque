from datetime import datetime as dt

class Movimentacao:

    def __init__(self,idFuncionario:int,dataMov:dt=dt.today()):
        self.__dataMov = dataMov
        self.__idFuncionario = idFuncionario
        self.__idProd = None
        self.__numeroSala = None
        self.__quantidade = None

    def entrarEstoque(self,idProd:int,quantidade:int):
        self.__idProd = idProd
        self.__quantidade = quantidade

    def saidaEstoque(self,idProd:int,quantidade:int,numeroSala:int):
        self.__idProd = idProd
        self.__quantidade = quantidade
        self.__numeroSala = numeroSala

    def movimento(self):
        return {
            "dataMovimento": self.__dataMov,
            "idFuncionario": self.__idFuncionario,
            "idProduto": self.__idProd,
            "numeroSala": self.__numeroSala,
            "quantidade": self.__quantidade
        }