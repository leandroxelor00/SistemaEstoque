from src.model.DAO.baseDB import BaseDB


class ProdutosDAO:

    def __init__(self):
        self.__conn = BaseDB("products.json")

    def addProd(self, data: dict):
        try:
            self.__conn.save(data)
            return "Produto adicionado"
        except Exception as e:
            raise print("Erro ao adicionar product")

    def viewList(self):
        return self.__conn.listData()

    def deleteProd(self, id):
        newList = [product for product in self.viewList() if product["idProd"] != id]
        if len(newList) == len(self.viewList()):
            raise ValueError("Nenhum product encontrado por esse ID")

        self.__conn.saveList(newList)
        print("product deletado com sucesso")

    def searchById(self, id):
        product = [product for product in self.viewList() if product["idProd"] == id]
        if product:
            for product in product:
                return f"ID: {product["idProd"]} | Produto: {product["nome"]} | Preço: {product["valor"]}"
        else:
            raise ValueError("Produto não encontrado por esse ID")

# if __name__ == '__main__':
    # p = ProdutosDAO()
    # prod = {
    #         "idProd": 1,
    #         "nome": "dada",
    #         "valor":75,
    #     }
    # p.addProd(prod)

    # print(p.searchById(1))

    # try:
    #     for i in p.viewList():
    #         print(f"ID: {i["idProd"]} | Produto: {i["nome"]} | R$$: {i["valor"]}")
    # except:
    #     print("erro ao consultar os produtos")