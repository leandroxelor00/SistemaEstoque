from flet import *

class ViewRegProduto:

    def __init__(self):

        self.nomeProd=TextField(label="Nome",icon=Icons.PERSON,col=7)
        self.marcaProd=TextField(label="Marca",icon=Icons.ADD_BOX,col=7)
        self.valorProd=TextField(label="Valor",prefix="R$",col=3)
        self.btnCadastrarProduto=Button("Add Prod",icon=CupertinoIcons.PLUS,col=3,margin=Margin.only(top=10))
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
            ),border=Border.all(2,"Black"),height=150,padding=15,
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaProduto],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
            border=Border.all(2, "Black"),
        )

        return Column(
            controls=[modalProduto,modalTabela],
            expand=True

                    )

