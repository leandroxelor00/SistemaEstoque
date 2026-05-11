from src.model.DAO.movementDAO import MovimentoDAO
from src.views.viewShowMovement import ViewShowMovement
from src.controlers.movementController import MovementController
from flet import DataCell,DataRow,Text

class SearchMovementController:

    def __init__(self,page,tela:ViewShowMovement):
        self.dao = MovimentoDAO()
        self.page = page
        self.tela = tela
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
            if not self.tela.searchBar.value and not self.tela.searchBar2.value:
                self.addLinhas(movimentos)

            else:
                if self.tela.searchBar.value == str(movimentos["idMovimento"]):
                    self.addLinhas(movimentos)
                else:

                    if self.tela.searchBar2.value == str(movimentos["idProd"]):
                        self.addLinhas(movimentos)

        self.page.update()


