from flet import *

class ViewMovimento(View):

    def __init__(self):
        super().__init__()
        self.tipo=Dropdown(label="Tipo de Movimento", width=250, height=50,
                           options=[dropdown.Option("Entrada"),
                                    dropdown.Option("Saída")],col=4)
        self.idProd=TextField(label="idProd",col=3)
        self.quantidade=TextField(label="Quantidade",col=4)
        self.idFornecedor=TextField(label="idFornecedor",col=4)
        self.idFuncionario=TextField(label="idFuncionario",col=3)
        self.btnCadastrarMovimento=Button("Add Movimento",icon=CupertinoIcons.PLUS,col=4,width=100,margin=Margin(0,10,0,0))
        self.route = "/movimentos"



        self.tabelaMovimentos = DataTable(
            columns=[
                DataColumn(label=Text("idMovimento")),
                DataColumn(label=Text("idProd")),
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
                ]
            ),border=Border.all(2,"Black"),height=150,padding=15,
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaMovimentos],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
            border=Border.all(2, "Black"),
        )

        self.controls=[Column(
            controls=[modalMovimento,modalTabela]

                    )
            ]

        return self.controls


