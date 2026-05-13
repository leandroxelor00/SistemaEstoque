from src.infrastructure.services.idGen import GeradorID
from src.model.entities.stock import Estoque
from src.model.DAO.stockDAO import EstoqueDAO
from src.views.viewStock import ViewStock
from flet import *

class StockController:

    def __init__(self,page,tela:ViewStock):
        self.dao = EstoqueDAO()
        self.page = page
        tela.btnCadastrarNoEstoque.on_click=self.handleAddProd
        self.tela = tela
        self.listarEstoque()

    def listarEstoque(self):
        self.tela.tabelaEstoque.rows.clear()
        for estoque in self.dao.verEstoque():
            linhas = DataRow(
                cells=[
                    DataCell(Text(estoque["idEstoque"])),
                    DataCell(Text(estoque["idProd"])),
                    DataCell(Text(estoque["quantidade"])),
                ]
            )
            self.tela.tabelaEstoque.rows.append(linhas)
        self.page.update()


    def handleAddProd(self):
        print("Entrou no handleAddProd")
        e = Estoque(GeradorID("stock.json", "idEstoque").idGerado,int(self.tela.idProd.value),int(self.tela.quantidade.value))


        try:
            self.dao.addNovoProdEstoque(e.estoque())
            self.tela.idProd.value = ""
            self.tela.quantidade.value = ""
            self.tela.idProd.update()
            self.tela.quantidade.update()
            self.listarEstoque()
        except Exception as e:
            print(e)

