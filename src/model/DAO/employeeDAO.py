from src.model.DAO.baseDB import BaseDB


class EmployeeDAO:

    def __init__(self):
        self.__conn = BaseDB("employee.json")

    def addFunc(self, data):
        try:
            self.__conn.save(data)
            print("Funcionário adicionado")
        except Exception as e:
            raise ValueError("Erro ao dicionar o funcionário no db: ", self.__conn, e)

    def viewList(self):
        return self.__conn.listData()

    def deleteFunc(self, id):
        newList = [funcionario for funcionario in self.viewList() if funcionario["idFunc"] != id]
        if len(newList) == len(self.viewList()):
            raise ValueError("Erro ao tentar deletar o funcionário")

        self.__conn.saveList(newList)
        print("Funcionário deletado com sucesso")


    def searchById(self,id):
        funcionario = [funcionario for funcionario in self.viewList() if funcionario["idFornecedor"] == id]
        if funcionario:
            for i in funcionario:
                return f"ID: {i["idFornecedor"]} | Fornecedor: {i["nome"]}"
        else:
            raise ValueError("Erro ao procurar o fornecedor por esse ID")

if __name__ == '__main__':
    f = EmployeeDAO()
    f.addFunc({
        "idFunc": 1,
        "nome": "dan"
    })

    f.deleteFunc(2)


    try:
        for i in f.viewList():
            print(f"ID: {i["idFunc"]} | Nome: {i["nome"]}")
    except:
        print("erro ao consultar os funcionários")