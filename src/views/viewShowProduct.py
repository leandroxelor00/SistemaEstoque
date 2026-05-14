
from flet import ResponsiveRow, Column, Container, View, Button, TextField, DataRow, DataCell, DataTable, DataColumn, \
    Padding, Border, MainAxisAlignment, Text, ElevatedButton, ButtonStyle, RoundedRectangleBorder


class ViewShowProduct(View):

    def __init__(self):
<<<<<<< Updated upstream
        super().__init__()
        self.searchBar = TextField(label="Pesquisar por ID",col=7)
        self.btnSearch=Button("Procurar", col=3)
        self.route = ("/search")
=======
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
        self.route = ("/searchproduct")
>>>>>>> Stashed changes

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