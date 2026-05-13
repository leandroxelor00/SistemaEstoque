from flet import *

class ViewRegStock:

    def __init__(self):

        self.idProd = TextField(label="idProd",col=5)
        self.quantidade=TextField(label="Quantidade",icon=Icons.PERSON,col=4)
        self.btnCadastrarNoEstoque=Button("Add no Estoque",icon=CupertinoIcons.PLUS,col=3,margin=Margin.only(top=10))
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
            ),border=Border.all(2,"Black"),height=80,padding=15,
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaEstoque],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
            border=Border.all(2, "Black"),
        )

        return Column(
            controls=[modalEstoque,modalTabela]

                    )



