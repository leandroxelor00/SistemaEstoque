
from flet import ResponsiveRow, Column, Container, ScrollMode, View, Button, TextField, DataRow, DataCell, DataTable, DataColumn, \
    Padding, Border, MainAxisAlignment, Text, Dropdown, dropdown, ElevatedButton, ButtonStyle, RoundedRectangleBorder


class ViewShowMovement:

    def __init__(self):
        super().__init__()
        self.searchBar = TextField(
            label="Pesquisar por...",

            col=5,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.searchPerType = Dropdown(
            label="Procurar por...",

            options=[
                dropdown.Option("idMovimento"),
                dropdown.Option("nome"),
                dropdown.Option("Entrada"),
                dropdown.Option("Saída"),
            ],

            col=5,
            width=250,
            height=50,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
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
        self.route = ("/searchmovement")

        self.tabelaMovimentos = DataTable(
            columns=[
                DataColumn(label=Text("idMovimento")),
                DataColumn(label=Text("nome")),
                DataColumn(label=Text("Quantidade")),
                DataColumn(label=Text("idFornecedor")),
                DataColumn(label=Text("idFuncionario")),
                DataColumn(label=Text("Tipo")),
            ],
            col=12
        )



    def build(self):

        modalBarra = Container(
            content=ResponsiveRow(
                controls=[
                    self.searchBar,
                    self.btnSearch
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=Padding(10, 20, 10, 20),
        )

        modalTabela = Container(
            expand=True,

            content=ResponsiveRow(
                controls=[self.tabelaMovimentos],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            ),

            padding=Padding(10, 20, 10, 20),
        )

        return Column(
            controls=[
                modalBarra,
                modalTabela
            ],
            expand=True,
            scroll=ScrollMode.AUTO,
        )