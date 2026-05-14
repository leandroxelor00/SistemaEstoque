
from flet import ResponsiveRow, Column, Container, ScrollMode, View, Button, TextField, DataRow, DataCell, DataTable, DataColumn, \
    Padding, Border, MainAxisAlignment, Text, ElevatedButton, ButtonStyle, RoundedRectangleBorder


class ViewShowEmployee:

    def __init__(self):

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
        )

        modalTabela = Container(
            content=ResponsiveRow(controls=[self.tabelaFuncs], alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10, 20, 10, 20),
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
                controls=[self.tabelaFuncs],
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

