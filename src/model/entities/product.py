

class Produto:

    def __init__(self,idProd:int,nome:str,marca:str,valor:float=None):
        self.__idProd = idProd
        self.__nome = nome
        self.__marca = marca
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def idProd(self):
        return self.__idProd

    def __eq__(self, other):
        return (self.__idProd,self.__nome) == (other.idProd,other.nome)

    def __gt__(self, other):
        return self.__nome > other.nome


    def produto(self):
        return {
            "idProd": self.__idProd,
            "nome": self.__nome,
            "marca": self.__marca,
            "valor": self.__valor
        }

    @staticmethod
    def dictToObject(data):
        return Produto(
            data["idProd"],
            data["nome"],
            data["marca"],
            data["valor"]
        )