from src.infrastructure.services.idGen import GeradorID
from src.model.entities.employee import Funcionario
from src.model.DAO.employeeDAO import EmployeeDAO
from src.views.viewEmployee import ViewEmployee
from flet import *

class EmployeeController:

    def __init__(self,page,tela:ViewEmployee):
        self.dao = EmployeeDAO()
        self.page = page
        tela.btnCadastrarFunc.on_click=self.handleAddProd
        self.tela = tela
        self.listarFuncs()

    def listarFuncs(self):
        self.tela.tabelaFunc.rows.clear()
        for func in self.dao.viewList():
            linhas = DataRow(
                cells=[
                    DataCell(Text(func["idFunc"])),
                    DataCell(Text(func["nome"])),
                ]
            )
            self.tela.tabelaFunc.rows.append(linhas)
        self.page.update()


    def handleAddProd(self):
        print("Entrou no handleAddProd")
        f = Funcionario(GeradorID("employee.json", "idFunc").idGerado, self.tela.nome.value)


        try:
            self.dao.addFunc(f.funcionario())
            self.tela.nome.value = ""
            self.tela.nome.update()
            self.listarFuncs()
        except Exception as e:
            print(e)
