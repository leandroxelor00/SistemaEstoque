from src.infrastructure.services.idGen import GeradorID
from src.model.entities.movement import Movimentacao
from src.model.DAO.movementDAO import MovimentoDAO
from src.views.viewMovement import ViewMovimento
from src.model.DAO.employeeDAO import EmployeeDAO
from flet import *

class MovementController:

    def __init__(self,page,tela:ViewMovimento):
        self.dao = MovimentoDAO()
        self.page = page
        tela.btnCadastrarMovimento.on_click=self.handleAddMov
        self.tela = tela
        self.listarProdutos()
        self.addDropdownOptions()



    def listarProdutos(self):
        self.tela.tabelaMovimentos.rows.clear()
        for produto in self.dao.viewList():
            linhas = DataRow(
                cells=[
                    DataCell(Text(produto["idMovimento"])),
                    DataCell(Text(produto["idProd"])),
                    DataCell(Text(produto["quantidade"])),
                    DataCell(Text(produto["idFornecedor"])),
                    DataCell(Text(produto["idFunc"])),
                    DataCell(Text(produto["tipo"])),
                ]
            )
            self.tela.tabelaMovimentos.rows.append(linhas)
        self.page.update()


    def handleAddMov(self):
        print("Entrou no handleAddMov")

        try:
            if self.tela.tipo.value == "Entrada":
                self.dao.addMovimentoEntrada(int(self.tela.idProd.value),int(self.tela.quantidade.value),int(self.tela.idFornecedor.value))
            elif self.tela.tipo.value == "Saída":
                self.dao.addMovimentoSaida(int(self.tela.idProd.value),int(self.tela.quantidade.value),int(self.tela.idFornecedor.value))
            self.tela.idProd.value = ""
            self.tela.quantidade.value = ""
            self.tela.idFuncionario.value = ""
            self.tela.idFornecedor.value = ""
            self.tela.tipo.value = ""
            self.tela.idProd.update()
            self.tela.quantidade.update()
            self.tela.idFuncionario.update()
            self.tela.idFornecedor.update()
            self.tela.tipo.update()
            self.listarProdutos()
        except Exception as e:
            print(e)

    def addDropdownOptions(self):
        e = EmployeeDAO()
        lista = []
        for i in e.viewList():
            lista.append(dropdown.Option(text=i["nome"]))

        self.tela.selectFunc.options = lista
