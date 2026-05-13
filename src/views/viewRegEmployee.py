from flet import *

class ViewRegEmployee:

    def __init__(self):

        self.nome=TextField(label="Nome",icon=Icons.ADD_BOX,col=8)
        self.btnCadastrarFunc=Button("Add Func",icon=CupertinoIcons.PLUS,col=3,margin=Margin.only(top=10))
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
            ),border=Border.all(2,"Black"),height=80,padding=15,
            col=12
        )

        modalTabela=Container(
            content=ResponsiveRow(controls=[self.tabelaFunc],alignment=MainAxisAlignment.SPACE_BETWEEN),
            padding=Padding(10,20,10,20),
            border=Border.all(2, "Black"),
        )

        return Column(
            controls=[modalEmployee,modalTabela]

                    )



