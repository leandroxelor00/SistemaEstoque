from src.model.DAO.baseDB import BaseDB
from src.infrastructure.services.idGen import GeradorID
from src.model.DAO.stockDAO import EstoqueDAO


class MovimentoDAO:

    def __init__(self):
        self.__conn = BaseDB("movement.json")

    def addMovimentoEntrada(self, idProduto, quantidade, idFornecedor):
        try:
            data = {
                "idMovimento": GeradorID("movement.json","idMovimento").idGerado,
                "idProd": idProduto,
                "quantidade": quantidade,
                "idFornecedor": idFornecedor,
                "tipo": "Entrada"
            }
            self.__conn.save(data)

            estoque = EstoqueDAO()
            for i in estoque.verEstoque():
                if i["idProd"] == idProduto:
                    estoque.aumentarQttProd(idProduto,quantidade)

            return "Movimento adicionado"
        except Exception as e:
            raise ValueError("Erro ao adicionar o movimento no db: ", self.__conn, e)

    def addMovimentoSaida(self, idProduto, quantidade, idFuncionario):
        try:
            data = {
                "idMovimento": GeradorID("movement.json","idMovimento").idGerado,
                "idProd": idProduto,
                "quantidade": quantidade,
                "idFunc": idFuncionario,
                "tipo": "Saída"
            }
            self.__conn.save(data)

            estoque = EstoqueDAO()
            for i in estoque.verEstoque():
                if i["idProd"] == idProduto:
                    estoque.retirarQttProd(idProduto, quantidade)

            return "Movimento adicionado"
        except Exception as e:
            raise ValueError("Erro ao adicionar o movimento no db: ", self.__conn, e)

    def viewList(self):
        return self.__conn.listData()

    def deleteMovimento(self, id):
        newList = [movimento for movimento in self.viewList() if movimento["idMovimento"] != id]
        if len(newList) == len(self.viewList()):
            raise ValueError("Erro ao tentar deletar o movimento")

        self.__conn.saveList(newList)
        print("Funcionário deletado com sucesso")

    def searchById(self,id):
        movimento = [movimento for movimento in self.viewList() if movimento["idMovimento"] == id]
        if movimento:
            for i in movimento:
                return f"idMovimento: {i["idMovimento"]} | idProd: {i["idProd"]}"
        else:
            raise ValueError("Erro ao procurar um movimento por esse ID")

# if __name__ == '__main__':
#     mov = MovimentoDAO()
#     mov.addMovimento({
#         "idMovimento": 1,
#         "idProd": 1,
#         "quantidade": 10,
#         "tipo": 1
#     })
#
#
#     try:
#         for i in mov.viewList():
#             print(f"ID: {i["idMovimento"]} | Nome: {i["nome"]}")
#     except:
#         print("erro ao consultar os funcionários")
#     stk = EstoqueDAO()
#     for i in stk.verEstoque():
#         print(i["idProd"])
if __name__ == '__main__':
    mov = MovimentoDAO()
    # mov.addMovimentoEntrada(5,10,1)
    mov.addMovimentoSaida(5,10,1)
