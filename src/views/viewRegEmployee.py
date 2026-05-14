from flet import *

class ViewRegEmployee:

    def __init__(self):
        self.nome = TextField(
            label="Nome",
            icon=Icons.PERSON,
            col=8,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.btnCadastrarFunc = ElevatedButton(
            "Add Func",
            icon=Icons.ADD,

            col=3,

            bgcolor="#2563EB",
            color="white",

            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
        )
        self.route = "/employee"



        self.tabelaFunc = DataTable(
            columns=[
                DataColumn(label=Text("idFunc")),
                DataColumn(label=Text("Nome")),
            ],
            col=12
        )

    def build(self):
        modalEmployee=Container(
            content=Column(
                controls=[
                    ResponsiveRow(controls=[self.nome, self.btnCadastrarFunc], alignment=MainAxisAlignment.SPACE_BETWEEN),
                ]
            ),
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaFunc],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
        )

        return Column(
            controls=[modalEmployee,modalTabela]

                    )



