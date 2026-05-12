

class Funcionario:

    def __init__(self,idFunc:int,nome:str):
        self.__idFunc = idFunc
        self.__nome = nome


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idFuncionario(self):
        return self.__idFunc

    def __eq__(self, other):
        return self.__idFunc==other.idFunc

    def funcionario(self):
        return {
            "idFunc": self.__idFunc,
            "nome": self.__nome,
        }

    @staticmethod
    def dictToObject(data):
        return Funcionario(
            data["idFunc"],
            data["nome"]
        )