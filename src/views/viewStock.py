from flet import *

class ViewStock(View):

    def __init__(self):
        super().__init__()
        self.idProd = TextField(label="idProd",col=5)
        self.quantidade=TextField(label="Quantidade",icon=Icons.PERSON,col=4)
        self.btnCadastrarNoEstoque=Button("Add no Estoque",icon=CupertinoIcons.PLUS,col=3)
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
                ]
            ),border=Border.all(2,"Black"),height=150,padding=15,
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaEstoque],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
            border=Border.all(2, "Black"),
        )

        self.controls=[Column(
            controls=[modalEstoque,modalTabela]

                    )
            ]

        return self.controls


