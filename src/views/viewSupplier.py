from flet import *

class ViewSupplier(View):

    def __init__(self):
        super().__init__()
        self.nome=TextField(label="Nome",icon=Icons.ADD_BOX,col=8)
        self.btnCadastrarFornecedor=Button("Add Fornecedor",icon=CupertinoIcons.PLUS,col=3,margin=Margin(0,10,0,0))
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
            ),border=Border.all(2,"Black"),height=80,padding=15,
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaFornecedor],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
            border=Border.all(2, "Black"),
        )

        self.controls=[Column(
            controls=[modalFornecedor,modalTabela]

                    )
            ]

        return self.controls


