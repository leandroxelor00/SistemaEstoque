
from flet import ResponsiveRow, Column, Container, View, Button, TextField, DataRow, DataCell, DataTable, DataColumn, \
    Padding, Border, MainAxisAlignment, Text, ElevatedButton, ButtonStyle, RoundedRectangleBorder


class ViewSearchMovement(View):

    def __init__(self):
        super().__init__()
        self.searchBar = TextField(label="Pesquisar por ID",col=7)
        self.btnSearch=Button("Procurar", col=3)
        self.route = ("/search")

        self.searchBar = TextField(
            label="Pesquisar por ID",
            col=7,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.btnSearch = ElevatedButton(
            "Procurar",

            col=3,

            bgcolor="#2563EB",
            color="white",

            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
        )
        self.route = ("/searchstock")

        self.tabelaProduto = DataTable(
            columns=[
                DataColumn(label=Text("IdMovimento")),
                DataColumn(label=Text("IdProd")),
                DataColumn(label=Text("Quantidade")),
                DataColumn(label=Text("Fornecedor")),
                DataColumn(label=Text("Funcionario")),
                DataColumn(label=Text("Tipo")),
            ],
            col=12
        )


    def build(self):
        modalBarra = Container(
            content=ResponsiveRow(controls=[self.searchBar, self.btnSearch], alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10, 20, 10, 20),
        )

        modalTabela = Container(
            content=ResponsiveRow(controls=[self.tabelaProduto], alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10, 20, 10, 20),
        )

        self.controls = [Column(
            controls=[modalBarra,modalTabela]

            )
        ]

        return self.controls