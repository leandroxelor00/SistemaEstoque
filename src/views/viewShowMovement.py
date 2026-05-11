
from flet import ResponsiveRow, Column, Container, View, Button,TextField,DataRow,DataCell,DataTable,DataColumn,Padding,Border,MainAxisAlignment,Text


class ViewShowMovement(View):

    def __init__(self):
        super().__init__()
        self.searchBar = TextField(label="Pesquisar movimento por ID",col=5)
        self.searchBar2 = TextField(label="Pesquisar produto por ID", col=5)
        self.btnSearch=Button("Procurar", col=3)
        self.route = ("/searchmovement")

        self.tabelaMovimentos = DataTable(
            columns=[
                DataColumn(label=Text("idMovimento")),
                DataColumn(label=Text("idProd")),
                DataColumn(label=Text("Quantidade")),
                DataColumn(label=Text("idFornecedor")),
                DataColumn(label=Text("idFuncionario")),
                DataColumn(label=Text("Tipo")),
            ],
            col=12
        )



    def build(self):
        modalBarra = Container(
            content=ResponsiveRow(controls=[self.searchBar, self.searchBar2], alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10, 20, 10, 20),
            border=Border.all(2, "Black"),
        )

        modalTabela = Container(
            content=ResponsiveRow(controls=[self.tabelaMovimentos], alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10, 20, 10, 20),
            border=Border.all(2, "Black"),
        )

        self.controls = [Column(
            controls=[modalBarra,modalTabela]

            )
        ]

        return self.controls