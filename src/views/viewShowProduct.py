
from flet import ResponsiveRow, Column, Container, View, Button,TextField,DataRow,DataCell,DataTable,DataColumn,Padding,Border,MainAxisAlignment,Text


class ViewShowProduct:

    def __init__(self):

        self.searchBar = TextField(label="Pesquisar por ID",col=7)
        self.btnSearch=Button("Procurar", col=3)
        self.route = ("/searchproduct")

        self.tabelaProduto = DataTable(
            columns=[
                DataColumn(label=Text("IdProd")),
                DataColumn(label=Text("Nome")),
                DataColumn(label=Text("Marca")),
                DataColumn(label=Text("Valor R$")),
            ],
            col=12
        )


    def build(self):
        modalBarra = Container(
            content=ResponsiveRow(controls=[self.searchBar, self.btnSearch], alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10, 20, 10, 20),
            border=Border.all(2, "Black"),
        )

        modalTabela = Container(
            content=ResponsiveRow(controls=[self.tabelaProduto], alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10, 20, 10, 20),
            border=Border.all(2, "Black"),
        )

        return Column(
            controls=[modalBarra,modalTabela],
            expand=True

            )
