from src.model.DAO.baseDB import BaseDB


class SupplierDAO:

    def __init__(self):
        self.__conn = BaseDB("supplier.json")

    def addFornecedor(self, data):
        try:
            self.__conn.save(data)
            print("Fornecedor adicionado")
        except Exception as e:
            raise ValueError("Erro ao adicionar o fornecedor no db: ", self.__conn, e)

    def viewList(self):
        return self.__conn.listData()

    def deleteFornecedor(self, id):
        newList = [fornecedor for fornecedor in self.viewList() if fornecedor["idFunc"] != id]
        if len(newList) == len(self.viewList()):
            raise ValueError("Erro ao tentar deletar o fornecedor")

        self.__conn.saveList(newList)
        print("Funcionário deletado com sucesso")


    def searchById(self,id):
        fornecedor = [fornecedor for fornecedor in self.viewList() if fornecedor["idFornecedor"] == id]
        if fornecedor:
            for i in fornecedor:
                return f"ID: {i["idFornecedor"]} | Fornecedor: {i["nome"]}"
        else:
            raise ValueError("Erro ao procurar o fornecedor por esse ID")

if __name__ == '__main__':
    f = SupplierDAO()
    f.addFornecedor({
        "idFornecedor": 1,
        "nome": "dan"
    })

    f.deleteFornecedor(2)


    try:
        for i in f.viewList():
            print(f"ID: {i["idFunc"]} | Nome: {i["nome"]}")
    except:
        print("erro ao consultar os fornecedores")