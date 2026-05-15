from src.model.DAO.stockDAO import EstoqueDAO
from src.views.viewShowStock import ViewShowStock
from flet import DataCell,DataRow,Text

class SearchStockController:

    def __init__(self,page,tela:ViewShowStock):
        self.dao = EstoqueDAO()
        self.page = page
        self.tela = tela
        tela.searchBar.on_change=self.searchProduct
        self.listarFuncs()

    def addLinhas(self,func):
        linhas = DataRow(
            cells=[
                DataCell(Text(func["idEstoque"])),
                DataCell(Text(func["idProd"])),
                DataCell(Text(func["quantidade"])),
            ]
        )
        self.tela.tabelaEstoque.rows.append(linhas)


    def listarFuncs(self):
        self.tela.tabelaEstoque.rows.clear()
        for estoque in self.dao.verEstoque():
            self.addLinhas(estoque)
        self.page.update()

    def searchProduct(self):
        self.tela.tabelaEstoque.rows.clear()

        for estoque in self.dao.verEstoque():
            if not self.tela.searchBar.value:
                self.addLinhas(estoque)

            else:
                if (self.tela.searchBar.value == str(estoque["idProd"])):
                    self.addLinhas(estoque)

        self.page.update()


