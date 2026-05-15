from flet import *

<<<<<<< Updated upstream
class ViewProduto(View):

    def __init__(self):
        super().__init__()
        self.nomeProd=TextField(label="Nome",icon=Icons.PERSON,col=7)
        self.marcaProd=TextField(label="Marca",icon=Icons.ADD_BOX,col=7)
        self.valorProd=TextField(label="Valor",prefix="R$",col=3)
        self.btnCadastrarProduto=Button("Add Prod",icon=CupertinoIcons.PLUS,col=3)
        self.route = "/"



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

        self.controls=[Column(
            controls=[modalProduto,modalTabela]

                    )
            ]

        return self.controls


=======
from src.controlers.searchProductController import SearchProductController
from src.controlers.productController import ProdutoController
<<<<<<< Updated upstream
=======
from src.controlers.searchProductController import SearchProductController
>>>>>>> Stashed changes


class ViewProduct:

    def __init__(self, page):
        self.page = page
        self.cadastro_view = None
        self.consulta_view = None

        self.btn_cadastro = ElevatedButton(
            "Cadastrar Produto",
            icon=Icons.ADD_BOX_OUTLINED,
            bgcolor="#2563EB",  # Azul Ativo
            color="white",
            scale=1.05,
            animate_scale=Animation(300, "easeOutBack"),
            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
            on_click=lambda e: self.show_cadastro(),
        )

        self.btn_consulta = ElevatedButton(
            "Consultar Produtos",
            icon=Icons.SEARCH,
            bgcolor="#1E293B",  # Cinza Inativo
            color="white",
            scale=1.0,
            animate_scale=Animation(300, "easeOutBack"),
            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
            on_click=lambda e: self.show_consulta(),
        )

        self.sub_content = Container(
            expand=True,
            animate=Animation(400, "decelerate"),
            opacity=1,
        )

    def update_visuals(self, active_tab):
        if active_tab == "cadastro":
            self.btn_cadastro.bgcolor = "#2563EB"
            self.btn_cadastro.scale = 1.05
            self.btn_cadastro.elevation = 8

            self.btn_consulta.bgcolor = "#1E293B"
            self.btn_consulta.scale = 0.95
            self.btn_consulta.elevation = 0
        else:
            self.btn_consulta.bgcolor = "#2563EB"
            self.btn_consulta.scale = 1.05
            self.btn_consulta.elevation = 8

            self.btn_cadastro.bgcolor = "#1E293B"
            self.btn_cadastro.scale = 0.95
            self.btn_cadastro.elevation = 0

        self.page.update()

    def show_cadastro(self):
        from src.views.viewRegProduct import ViewRegProduto

        self.sub_content.opacity = 0
        self.page.update()

        if not self.cadastro_view:
            self.cadastro_view = ViewRegProduto()
            from src.controlers.productController import ProdutoController
            ProdutoController(self.page, self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.sub_content.opacity = 1
        self.update_visuals("cadastro")

    def show_consulta(self):
        from src.views.viewShowProduct import ViewShowProduct

        self.sub_content.opacity = 0
        self.page.update()

        if not self.consulta_view:
            self.consulta_view = ViewShowProduct()
            from src.controlers.searchProductController import SearchProductController
            SearchProductController(self.page, self.consulta_view)

        self.sub_content.content = self.consulta_view.build()
        self.sub_content.opacity = 1
        self.update_visuals("consulta")

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
                                Text("Produtos", size=28, weight="bold", color="white"),
                                Text("Gerencie os produtos cadastrados no sistema.", size=14, color="#94A3B8"),
                                Row(
                                    spacing=15,
                                    controls=[
                                        self.btn_cadastro,
                                        self.btn_consulta,
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
>>>>>>> Stashed changes
