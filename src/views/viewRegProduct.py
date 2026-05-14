from flet import *

class ViewRegProduto:

    def __init__(self):
        self.nomeProd = TextField(
            label="Nome",
            icon=Icons.PERSON,
            col=7,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            cursor_color="white",
            color="white",

            label_style=TextStyle(
                color="#94A3B8"
            ),

            border_radius=12,
        )
        self.marcaProd = TextField(
            label="Marca",
            icon=Icons.ADD_BOX,
            col=7,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            cursor_color="white",
            color="white",

            label_style=TextStyle(
                color="#94A3B8"
            ),

            border_radius=12,
        )
        self.valorProd = TextField(
            label="Valor",
            prefix="R$",
            col=3,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            cursor_color="white",
            color="white",

            label_style=TextStyle(
                color="#94A3B8"
            ),

            border_radius=12,
        )
        self.btnCadastrarProduto = ElevatedButton(
            "Add Prod",
            icon=Icons.ADD,

            col=3,

            bgcolor="#2563EB",
            color="white",

            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
        )
        self.route = "/product"



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
        modalProduto=Container(
            content=Column(
                controls=[
                    ResponsiveRow(controls=[self.nomeProd,self.valorProd], alignment=MainAxisAlignment.SPACE_AROUND),
                    ResponsiveRow(controls=[self.marcaProd, self.btnCadastrarProduto], alignment=MainAxisAlignment.SPACE_AROUND)
                ]
            ),
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaProduto],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
        )

        return Column(
            controls=[modalProduto,modalTabela],
            expand=True

                    )

