from src.model.DAO.supplierDAO import SupplierDAO
from src.views.viewShowSupplier import ViewShowSupplier
from flet import DataCell,DataRow,Text

class SearchSupplierController:

    def __init__(self,page,tela:ViewShowSupplier):
        self.dao = SupplierDAO()
        self.page = page
        self.tela = tela
        tela.searchBar.on_change=self.searchProduct
        self.listarFornecedor()

    def addLinhas(self,func):
        linhas = DataRow(
            cells=[
                DataCell(Text(func["idFornecedor"])),
                DataCell(Text(func["nome"])),
            ]
        )
        self.tela.tabelaFornecedor.rows.append(linhas)


    def listarFornecedor(self):
        self.tela.tabelaFornecedor.rows.clear()
        for fornecedor in self.dao.viewList():
            self.addLinhas(fornecedor)
        self.page.update()

    def searchProduct(self):
        self.tela.tabelaFornecedor.rows.clear()

        for fornecedor in self.dao.viewList():
            if not self.tela.searchBar.value:
                self.addLinhas(fornecedor)

            else:
                if (self.tela.searchBar.value == str(fornecedor["idFornecedor"])):
                    self.addLinhas(fornecedor)

        self.page.update()


