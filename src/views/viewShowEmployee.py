
from flet import ResponsiveRow, Column, Container, View, Button,TextField,DataRow,DataCell,DataTable,DataColumn,Padding,Border,MainAxisAlignment,Text


class ViewShowEmployee(View):

    def __init__(self):
        super().__init__()
        self.searchBar = TextField(label="Pesquisar por ID",col=7)
        self.btnSearch=Button("Procurar", col=3)
        self.route = ("/searchemployee")

        self.tabelaFuncs = DataTable(
            columns=[
                DataColumn(label=Text("IdFunc")),
                DataColumn(label=Text("Nome")),
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
            content=ResponsiveRow(controls=[self.tabelaFuncs], alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10, 20, 10, 20),
            border=Border.all(2, "Black"),
        )

        self.controls = [Column(
            controls=[modalBarra,modalTabela]

            )
        ]

        return self.controls