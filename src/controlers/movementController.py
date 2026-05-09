from src.model.DAO.productsDAO import ProdutosDAO
from src.views.viewShowProduct import ViewShowProduct
from flet import DataCell, DataRow, Text


class searchProductController:

    def __init__(self, page, tela: ViewShowProduct):
        self.dao = ProdutosDAO()
        self.page = page
        self.tela = tela
        tela.searchBar.on_change = self.searchProduct
        self.listarProdutos()

    def addLinhas(self, produto):
        linhas = DataRow(
            cells=[
                DataCell(Text(produto["idProd"])),
                DataCell(Text(produto["nome"])),
                DataCell(Text(produto["marca"])),
                DataCell(Text(produto["valor"]))
            ]
        )
        self.tela.tabelaProduto.rows.append(linhas)

    def listarProdutos(self):
        self.tela.tabelaProduto.rows.clear()
        for produto in self.dao.viewList():
            self.addLinhas(produto)
        self.page.update()

    def searchProduct(self):
        self.tela.tabelaProduto.rows.clear()

        for produto in self.dao.viewList():
            if not self.tela.searchBar.value:
                self.addLinhas(produto)

            else:
                if len(self.tela.searchBar.value) == 1:
                    if (self.tela.searchBar.value == str(produto["idProd"])) or (
                            produto["nome"][0] == self.tela.searchBar.value[0]) or (
                            produto["marca"][0] == self.tela.searchBar.value[0]):
                        self.addLinhas(produto)

                else:
                    if (self.tela.searchBar.value == str(produto["idProd"])) or (
                            produto["nome"] == self.tela.searchBar.value) or (
                            produto["marca"] == self.tela.searchBar.value):
                        self.addLinhas(produto)

        self.page.update()


