
from flet import ResponsiveRow, Column, Container, View, Button, TextField, DataRow, DataCell, DataTable, DataColumn, \
    Padding, Border, MainAxisAlignment, Text, Dropdown, dropdown


class ViewShowMovement(View):

    def __init__(self):
        super().__init__()
        self.searchBar = TextField(label="Pesquisar por...",col=5)
        self.searchPerType = Dropdown(label="Procurar por...", width=250,height=50,
                                      options=[dropdown.Option("idMovimento"),
                                               dropdown.Option("idProd"),
                                               dropdown.Option("Entrada"),
                                               dropdown.Option("Saída")],col=5)

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
            content=ResponsiveRow(controls=[self.searchPerType,self.searchBar], alignment=MainAxisAlignment.SPACE_AROUND),
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