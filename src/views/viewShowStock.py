
from flet import *

class ViewShowStock:

    def __init__(self):

        self.searchBar = TextField(label="Pesquisar por ID",
                                   icon=Icons.SEARCH,
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

        self.tabelaEstoque = DataTable(
            columns=[
                DataColumn(label=Text("idEstoque")),
                DataColumn(label=Text("idProd")),
                DataColumn(label=Text("Quantidade")),
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
                controls=[self.tabelaEstoque],
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
