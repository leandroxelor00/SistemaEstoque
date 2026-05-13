from src.infrastructure.services.idGen import GeradorID
from src.model.entities.supplier import Fornecedor
from src.model.DAO.supplierDAO import SupplierDAO
from src.views.viewRegSupplier import ViewRegSupplier
from flet import *

class SupplierController:

    def __init__(self, page, tela:ViewRegSupplier):
        self.dao = SupplierDAO()
        self.page = page
        tela.btnCadastrarFornecedor.on_click=self.handleAddProd
        self.tela = tela
        self.listarFuncs()

    def listarFuncs(self):
        self.tela.tabelaFornecedor.rows.clear()
        for fornecedor in self.dao.viewList():
            linhas = DataRow(
                cells=[
                    DataCell(Text(fornecedor["idFornecedor"])),
                    DataCell(Text(fornecedor["nome"])),
                ]
            )
            self.tela.tabelaFornecedor.rows.append(linhas)
        self.page.update()


    def handleAddProd(self):
        print("Entrou no handleAddProd")
        f = Fornecedor(GeradorID("supplier.json", "idFornecedor").idGerado, self.tela.nome.value)


        try:
            self.dao.addFornecedor(f.fornecedor())
            self.tela.nome.value = ""
            self.tela.nome.update()
            self.listarFuncs()
        except Exception as e:
            print(e)
