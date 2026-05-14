import json
from json import JSONDecodeError


class GeradorID:

    def __init__(self,path,atributo):
<<<<<<< Updated upstream
        # self.path = fr"E:\Aulas\SistemaEstoque\src\infrastructure\database\{path}"
=======
>>>>>>> Stashed changes
        self.path = fr"C:\Users\rafael.smoralli\Documents\GitHub\SistemaEstoque\src\infrastructure\database\{path}"
        self.idGerado = None
        try:
            with open(self.path,"r",encoding="utf-8") as file:
                lista = json.load(file)
                listaId = (data[atributo] for data in lista)
                self.idGerado=max(listaId)+1

        except JSONDecodeError as e:
            self.idGerado = 1

if __name__ == '__main__':
    ge = GeradorID("produtos.json",1)
    print(ge.idGerado)