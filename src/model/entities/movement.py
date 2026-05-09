from datetime import datetime as dt

class Movimentacao:

    def __init__(self,idFuncionario:int,dataMov:dt=dt.today()):
        self.__idMovimento = None
        self.__dataMov = dataMov
        self.__idFuncionario = idFuncionario
        self.__idProd = None
        self.__numeroSala = None
        self.__quantidade = None

    @property
    def idMov(self):
        return self.__idMovimento

    def entrarEstoque(self,idProd:int,quantidade:int):
        self.__idProd = idProd
        self.__quantidade = quantidade

    def saidaEstoque(self,idProd:int,quantidade:int,numeroSala:int):
        self.__idProd = idProd
        self.__quantidade = quantidade
        self.__numeroSala = numeroSala

    def movimento(self):
        return {
            "idMovimento": self.__idMovimento,
            "dataMovimento": self.__dataMov,
            "idFunc": self.__idFuncionario,
            "idProd": self.__idProd,
            "numeroSala": self.__numeroSala,
            "quantidade": self.__quantidade
        }