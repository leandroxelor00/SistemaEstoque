

class Funcionario:

    def __init__(self,nome:str,idFuncionario:int=None):
        self.__nome = nome
        self.__idFuncionario = idFuncionario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idFuncionario(self):
        return self.__idFuncionario

    def __eq__(self, other):
        return self.__idFuncionario==other.idFuncionario

    def funcionario(self):
        return {
            "idFuncionario": self.__idFuncionario,
            "nome": self.__nome,
        }

    @staticmethod
    def dictToObject(data):
        return Funcionario(
            data["idFuncionario"],
        )