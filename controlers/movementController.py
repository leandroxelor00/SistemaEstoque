from src.model.DAO.movementDAO import MovimentoDAO
from src.model.DAO.productsDAO import ProdutosDAO
from src.views.viewRegMovement import ViewRegMovimento
from src.model.DAO.employeeDAO import EmployeeDAO
from flet import *

class MovementController:

    def __init__(self, page, tela:ViewRegMovimento):
        self.dao = MovimentoDAO()
        self.daoProd = ProdutosDAO()
        self.page = page
        tela.btnCadastrarMovimento.on_click=self.handleAddMov
        tela.tipo.on_select=self.deixarDisabled
        tela.idFuncionario.on_change=self.deixarBtnDisabled
        tela.idFornecedor.on_change=self.deixarBtnDisabled
        self.tela = tela
        self.listarMovimentos()
        self.addDropdownOptions()


    def listarMovimentos(self):
        self.tela.tabelaMovimentos.rows.clear()
        for produto in self.dao.viewList():
            linhas = DataRow(
                cells=[
                    DataCell(Text(produto["idMovimento"])),
                    DataCell(Text(produto["nome"])),
                    DataCell(Text(produto["quantidade"])),
                    DataCell(Text(produto["idFornecedor"])),
                    DataCell(Text(produto["idFunc"])),
                    DataCell(Text(produto["tipo"])),
                ]
            )
            self.tela.tabelaMovimentos.rows.append(linhas)
        self.page.update()

    def deixarBtnDisabled(self):
        if self.tela.tipo.value == "Entrada":
            if any(val == "" for val in [self.tela.idProd.value,self.tela.quantidade.value,self.tela.idFornecedor.value]):

                self.tela.btnCadastrarMovimento.disabled = True
            else:
                self.tela.btnCadastrarMovimento.disabled = False

        elif self.tela.tipo.value == "Saída":
            if any(val == "" for val in[self.tela.idProd.value, self.tela.quantidade.value, self.tela.idFuncionario.value]):
                self.tela.btnCadastrarMovimento.disabled = True
            else:
                self.tela.btnCadastrarMovimento.disabled = False

    def deixarDisabled(self):
        if self.tela.tipo.value == "Entrada":
            self.tela.idFuncionario.value = 0
            self.tela.idFuncionario.disabled = True
            self.tela.idFornecedor.disabled = False
            self.tela.btnCadastrarMovimento.disabled= True

        elif self.tela.tipo.value == "Saída":
            self.tela.idFornecedor.value = 0
            self.tela.idFornecedor.disabled = True
            self.tela.idFuncionario.disabled = False
            self.tela.btnCadastrarMovimento.disabled= True


    def handleAddMov(self):
        print("Entrou no handleAddMov")

        try:
            if self.tela.tipo.value == "Entrada":
                self.dao.addMovimentoEntrada(int(self.tela.idProd.value),int(self.tela.quantidade.value),int(self.tela.idFornecedor.value))
            elif self.tela.tipo.value == "Saída":
                self.dao.addMovimentoSaida(int(self.tela.idProd.value),int(self.tela.quantidade.value),int(self.tela.idFuncionario.value))
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
            self.listarMovimentos()
        except Exception as e:
            print(e)

    def addDropdownOptions(self):
        e = EmployeeDAO()
        lista = []
        for i in e.viewList():
            lista.append(dropdown.Option(text=i["nome"]))

        self.tela.selectFunc.options = lista
