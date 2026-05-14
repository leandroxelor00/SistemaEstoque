from flet import *
from src.model.DAO.employeeDAO import EmployeeDAO
from src.controlers.searchMovementController import SearchMovementController
from src.controlers.movementController import MovementController
    

class ViewMovimento(View):

    def __init__(self):
        super().__init__()
        self.tipo=Dropdown(label="Tipo de Movimento", width=250, height=50,
                           options=[dropdown.Option("Entrada"),
                                    dropdown.Option("Saída")],col=4)
        self.selectFunc = Dropdown(label="Funcionario", width=250, height=50,col=4)

        self.idProd=TextField(label="idProd",col=3)
        self.quantidade=TextField(label="Quantidade",col=4)
        self.idFornecedor=TextField(label="idFornecedor",col=4)
        self.idFuncionario=TextField(label="idFuncionario",col=3)
        self.btnCadastrarMovimento=Button("Add Movimento",icon=CupertinoIcons.PLUS,col=4,width=100,margin=Margin(0,10,0,0),disabled=True)
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


class ViewMovement:
    # View principal das movimentações

    def __init__(self, page):
        self.page = page

        self.cadastro_view = None
        self.consulta_view = None

        self.sub_content = Container(
            expand=True,
            animate=Animation(300, "ease"),
        )

    def show_cadastro(self):

        from src.views.viewRegMovement import ViewRegMovimento

        if not self.cadastro_view:
            self.cadastro_view = ViewRegMovimento()
            MovementController(self.page, self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.page.update()

    def show_consulta(self):

        from src.views.viewShowMovement import ViewShowMovement

        if not self.consulta_view:
            self.consulta_view = ViewShowMovement()
            SearchMovementController(self.page, self.consulta_view)

        self.sub_content.content = self.consulta_view.build()
        self.page.update()

    def build(self):

        self.show_cadastro()

        return Container(
            expand=True,
            bgcolor="#0F172A",
            padding=20,

            content=Column(
                expand=True,
                spacing=20,

                controls=[

                    # HEADER
                    Container(
                        padding=20,
                        border_radius=16,
                        bgcolor="#111827",
                        border=Border.all(1, "#1E293B"),

                        content=Column(
                            spacing=15,

                            controls=[

                                Text(
                                    "Movimentações",
                                    size=28,
                                    weight="bold",
                                    color="white",
                                ),

                                Text(
                                    "Gerencie entradas e saídas de produtos.",
                                    size=14,
                                    color="#94A3B8",
                                ),

                                Row(
                                    spacing=15,

                                    controls=[

                                        ElevatedButton(
                                            "Cadastrar Movimento",
                                            icon=Icons.SWAP_HORIZ_OUTLINED,

                                            bgcolor="#2563EB",
                                            color="white",

                                            style=ButtonStyle(
                                                padding=20,
                                                shape=RoundedRectangleBorder(
                                                    radius=12
                                                ),
                                            ),

                                            on_click=lambda e: self.show_cadastro(),
                                        ),

                                        ElevatedButton(
                                            "Consultar Movimentos",
                                            icon=Icons.SEARCH,

                                            bgcolor="#1E293B",
                                            color="white",

                                            style=ButtonStyle(
                                                padding=20,
                                                shape=RoundedRectangleBorder(
                                                    radius=12
                                                ),
                                            ),

                                            on_click=lambda e: self.show_consulta(),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),

                    # CONTEÚDO
                    Container(
                        expand=True,
                        padding=20,
                        border_radius=16,
                        bgcolor="#111827",
                        border=Border.all(1, "#1E293B"),

                        content=self.sub_content,
                    ),
                ],
            ),
        )
