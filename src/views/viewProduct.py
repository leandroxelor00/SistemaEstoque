
from flet import *
from src.controlers.productController import ProdutoController
from src.controlers.searchProductController import SearchProductController 

class ViewProduct:
    # View principal dos produtos

    def __init__(self, page):
        self.page = page

        self.cadastro_view = None
        self.consulta_view = None

        self.sub_content = Container(
            expand=True,
            animate=Animation(300, "ease"),
        )

    def show_cadastro(self):

        from src.views.viewRegProduct import ViewRegProduto

        if not self.cadastro_view:
            self.cadastro_view = ViewRegProduto()
            ProdutoController(self.page, self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.page.update()

    def show_consulta(self):

        from src.views.viewShowProduct import ViewShowProduct

        if not self.consulta_view:
            self.consulta_view = ViewShowProduct()
            SearchProductController(self.page, self.consulta_view)

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
                                    "Produtos",
                                    size=28,
                                    weight="bold",
                                    color="white",
                                ),

                                Text(
                                    "Gerencie os produtos cadastrados no sistema.",
                                    size=14,
                                    color="#94A3B8",
                                ),

                                Row(
                                    spacing=15,

                                    controls=[

                                        ElevatedButton(
                                            "Cadastrar Produto",
                                            icon=Icons.ADD_BOX_OUTLINED,

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
                                            "Consultar Produtos",
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