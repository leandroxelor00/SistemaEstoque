from src.model.DAO.employeeDAO import EmployeeDAO
from src.views.viewShowEmployee import ViewShowEmployee
from flet import DataCell,DataRow,Text

class SearchEmployeeController:

    def __init__(self,page,tela:ViewShowEmployee):
        self.dao = EmployeeDAO()
        self.page = page
        self.tela = tela
        tela.searchBar.on_change=self.searchProduct
        self.listarFuncs()

    def addLinhas(self,func):
        linhas = DataRow(
            cells=[
                DataCell(Text(func["idFunc"])),
                DataCell(Text(func["nome"])),
            ]
        )
        self.tela.tabelaFuncs.rows.append(linhas)


    def listarFuncs(self):
        self.tela.tabelaFuncs.rows.clear()
        for funcs in self.dao.viewList():
            self.addLinhas(funcs)
        self.page.update()

    def searchProduct(self):
        self.tela.tabelaFuncs.rows.clear()

        for funcs in self.dao.viewList():
            if not self.tela.searchBar.value:
                self.addLinhas(funcs)

            else:
                if (self.tela.searchBar.value == str(funcs["idFunc"])):
                    self.addLinhas(funcs)

        self.page.update()


