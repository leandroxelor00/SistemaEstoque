from src.model.DAO.baseDB import BaseDB

class EstoqueDAO(BaseDB):
    def __init__(self):
        super().__init__("stock.json")

    def verEstoque(self):
        return self.listData()

    def addNovoProdEstoque(self,data):
        self.save(data)

    def aumentarQttProd(self,id,data):
        index, produto = [(index,produto) for index, produto in enumerate(self.listData()) if produto["idProd"] == id][0]
        produto["quantidade"]+= data
        novaLista = self.listData()
        novaLista[index] = produto
        self.saveList(novaLista)

    def retirarQttProd(self,id,data):
        index, produto = [(index, produto) for index, produto in enumerate(self.listData()) if produto["idProd"] == id][0]
        produto["quantidade"] -= data
        novaLista = self.listData()
        novaLista[index] = produto
        self.saveList(novaLista)

#     def procurarProdNoEstoque(self, id):
#         produto = [produto for produto in self.verEstoque() if produto["idProd"] == id]
#         if produto:
#             for produto in produto:
#                 return f"ID: {produto["idProd"]} | Quantidade: {produto["quantidade"]}"
#         else:
#             raise ValueError("Produto não encontrado por esse ID")
#
#
#
# if __name__ == '__main__':
#     es1 = EstoqueDAO()
#     prod = {
#         "idProd": 5,
#         "quantidade": 0
#     }
#     es1.addNovoProdEstoque(prod)
#     print(es1.verEstoque())

