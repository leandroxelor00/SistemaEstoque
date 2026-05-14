from flet import *

class ViewRegStock:

    def __init__(self):
        self.idProd = TextField(
            label="idProd",
            col=5,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.quantidade = TextField(
            label="Quantidade",
            icon=Icons.INVENTORY_2_OUTLINED,
            col=4,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.btnCadastrarNoEstoque = ElevatedButton(
            "Add no Estoque",
            icon=Icons.ADD,

            col=3,

            bgcolor="#2563EB",
            color="white",

            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
        )

        self.route = "/stock"



        self.tabelaEstoque = DataTable(
            columns=[
                DataColumn(label=Text("idEstoque")),
                DataColumn(label=Text("idProd")),
                DataColumn(label=Text("Quantidade")),
            ],
            col=12
        )

    def build(self):
        modalEstoque=Container(
            content=Column(
                controls=[
                    ResponsiveRow(controls=[self.idProd,self.quantidade,self.btnCadastrarNoEstoque], alignment=MainAxisAlignment.SPACE_AROUND),
                ]),
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaEstoque],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
        )

        return Column(
            controls=[modalEstoque,modalTabela],
            scroll=ScrollMode.AUTO

                    )



