from flet import *

class ViewRegSupplier:

    def __init__(self):
        self.nome = TextField(
            label="Nome",
            icon=Icons.LOCAL_SHIPPING_OUTLINED,
            col=8,

            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#2563EB",

            color="white",
            cursor_color="white",

            border_radius=12,
        )

        self.btnCadastrarFornecedor = ElevatedButton(
            "Add Fornecedor",
            icon=Icons.ADD,

            col=3,

            bgcolor="#2563EB",
            color="white",

            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
        )
        self.route = "/supplier"

        self.tabelaFornecedor = DataTable(
            columns=[
                DataColumn(label=Text("idFornecedor")),
                DataColumn(label=Text("Nome")),
            ],
            col=12
        )

    def build(self):
        modalFornecedor=Container(
            content=Column(
                controls=[
                    ResponsiveRow(controls=[self.nome, self.btnCadastrarFornecedor], alignment=MainAxisAlignment.SPACE_BETWEEN),
                ]
            ),
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaFornecedor],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
        )

        return Column(
            controls=[modalFornecedor,modalTabela],
            scroll=ScrollMode.AUTO

                    )


