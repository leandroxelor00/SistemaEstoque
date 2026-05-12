from src.model.DAO.movementDAO import MovimentoDAO
from src.views.viewShowMovement import ViewShowMovement
from src.controlers.movementController import MovementController
from flet import DataCell,DataRow,Text

class SearchMovementController:

    def __init__(self,page,tela:ViewShowMovement):
        self.dao = MovimentoDAO()
        self.page = page
        self.tela = tela
        tela.searchPerType.on_select=self.searchMovement
        tela.searchBar.on_change=self.searchMovement
        self.listarMovimentos()

    def addLinhas(self,produto):
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

    def listarMovimentos(self):
        self.tela.tabelaMovimentos.rows.clear()
        for movimentos in self.dao.viewList():
            self.addLinhas(movimentos)
        self.page.update()


    def searchMovement(self):
        self.tela.tabelaMovimentos.rows.clear()

        for movimentos in self.dao.viewList():

            if self.tela.searchPerType.value not in ("Entrada", "Saída"):
                self.tela.searchBar.disabled = False

                if self.tela.searchPerType.value == "idMovimento":
                    self.tela.searchBar.label = "Pesquisar por id movimento"

                    if not self.tela.searchBar.value:
                        self.addLinhas(movimentos)

                    elif self.tela.searchBar.value == str(movimentos["idMovimento"]):
                        self.addLinhas(movimentos)

                elif self.tela.searchPerType.value == "idProd":
                    self.tela.searchBar.label = "Pesquisar por id produto"

                    if not self.tela.searchBar.value:
                        self.addLinhas(movimentos)

                    elif self.tela.searchBar.value == str(movimentos["idProd"]):
                        self.addLinhas(movimentos)

            else:
                self.tela.searchBar.label = "Pequisar por..."
                self.tela.searchBar.disabled = True
                if self.tela.searchPerType.value == movimentos["tipo"]:
                    self.addLinhas(movimentos)


        self.page.update()


