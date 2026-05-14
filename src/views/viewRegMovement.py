from flet import *
from src.model.DAO.employeeDAO import EmployeeDAO

class ViewRegMovimento:

    def __init__(self):
        super().__init__()
        self.tipo = Dropdown(
            label="Tipo de Movimento",

            options=[
                dropdown.Option("Entrada"),
                dropdown.Option("Saída"),
            ],

            col=4,
            width=250,
            height=50,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            border_radius=12,
        )

        self.selectFunc = Dropdown(
            label="Funcionário",

            col=4,
            width=250,
            height=50,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            border_radius=12,
        )

        self.idProd = TextField(
            label="idProd",
            col=3,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.quantidade = TextField(
            label="Quantidade",
            col=4,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.idFornecedor = TextField(
            label="idFornecedor",
            col=4,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.idFuncionario = TextField(
            label="idFuncionario",
            col=3,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.btnCadastrarMovimento = ElevatedButton(
            "Add Movimento",
            icon=Icons.ADD,

            col=4,
            width=100,

            disabled=True,

            bgcolor="#2563EB",
            color="white",

            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
        )
        self.route = "/movement"



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
        modalMovimento=Container(
            content=Column(
                controls=[
                    ResponsiveRow(controls=[self.idProd,self.quantidade, self.tipo], alignment=MainAxisAlignment.SPACE_AROUND),
                    ResponsiveRow(controls=[self.idFuncionario, self.idFornecedor, self.btnCadastrarMovimento], alignment=MainAxisAlignment.SPACE_AROUND)
                ]),
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaMovimentos],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
        )

        return Column(
            controls=[modalMovimento,modalTabela],
            expand=True,
            scroll=ScrollMode.AUTO



                    )


