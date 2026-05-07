from src.model.DAO.productsDAO import ProdutosDAO
from src.views.viewShowProduct import ViewShowProduct
from flet import DataCell,DataRow,Text

class searchProductController:

    def __init__(self,page,tela:ViewShowProduct):
        self.dao = ProdutosDAO()
        self.page = page
        self.tela = tela
        tela.btnSearch.on_click=self.searchProduct
        self.listarProdutos()


    def listarProdutos(self):
        self.tela.tabelaProduto.rows.clear()
        for produto in self.dao.viewList():
            linhas = DataRow(
                cells=[
                    DataCell(Text(produto["idProd"])),
                    DataCell(Text(produto["nome"])),
                    DataCell(Text(produto["marca"])),
                    DataCell(Text(produto["valor"]))
                ]
            )
            self.tela.tabelaProduto.rows.append(linhas)
        self.page.update()

    def searchProduct(self):
        self.tela.tabelaProduto.rows.clear()
        for produto in self.dao.viewList():
            if not self.tela.searchBar.value and not self.tela.searchBar2.value:
                linhas = DataRow(
                    cells=[
                        DataCell(Text(produto["idProd"])),
                        DataCell(Text(produto["nome"])),
                        DataCell(Text(produto["marca"])),
                        DataCell(Text(produto["valor"]))
                    ]
                )
                self.tela.tabelaProduto.rows.append(linhas)

                if produto["idProd"] == int(self.tela.searchBar.value):
                    linhas = DataRow(
                        cells=[
                            DataCell(Text(produto["idProd"])),
                            DataCell(Text(produto["nome"])),
                            DataCell(Text(produto["marca"])),
                            DataCell(Text(produto["valor"]))
                        ]
                    )
                    self.tela.tabelaProduto.rows.append(linhas)

            if (produto["nome"] == self.tela.searchBar2.value) or (produto["marca"]== self.tela.searchBar2.value):
                linhas = DataRow(
                    cells=[
                        DataCell(Text(produto["idProd"])),
                        DataCell(Text(produto["nome"])),
                        DataCell(Text(produto["marca"])),
                        DataCell(Text(produto["valor"]))
                    ]
                )
                self.tela.tabelaProduto.rows.append(linhas)
            self.page.update()


