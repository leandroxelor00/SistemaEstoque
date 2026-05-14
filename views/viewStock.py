from flet import *

from src.controlers.searchStockController import SearchStockController
from src.controlers.stockController import StockController


class ViewStock:
    # View principal do estoque

    def __init__(self, page):
        self.page = page

        self.cadastro_view = None
        self.consulta_view = None

        self.sub_content = Container(
            expand=True,
            animate=Animation(300, "ease"),
        )

    def showCadastro(self):

        from src.views.viewRegStock import ViewRegStock

        if not self.cadastro_view:
            self.cadastro_view = ViewRegStock()
            StockController(self.page, self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.page.update()

    def showConsulta(self):

        from src.views.viewShowStock import ViewShowStock

        if not self.consulta_view:
            self.consulta_view = ViewShowStock()
            SearchStockController(self.page, self.consulta_view)

        self.sub_content.content = self.consulta_view.build()
        self.page.update()

    def build(self):

        self.showCadastro()

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
                                    "Estoque",
                                    size=28,
                                    weight="bold",
                                    color="white",
                                ),

                                Text(
                                    "Gerencie os produtos disponíveis no estoque.",
                                    size=14,
                                    color="#94A3B8",
                                ),

                                Row(
                                    spacing=15,

                                    controls=[

                                        ElevatedButton(
                                            "Cadastrar no Estoque",
                                            icon=Icons.INVENTORY_2_OUTLINED,

                                            bgcolor="#2563EB",
                                            color="white",

                                            style=ButtonStyle(
                                                padding=20,
                                                shape=RoundedRectangleBorder(
                                                    radius=12
                                                ),
                                            ),

                                            on_click=lambda e: self.showCadastro(),
                                        ),

                                        ElevatedButton(
                                            "Consultar Estoque",
                                            icon=Icons.SEARCH,

                                            bgcolor="#1E293B",
                                            color="white",

                                            style=ButtonStyle(
                                                padding=20,
                                                shape=RoundedRectangleBorder(
                                                    radius=12
                                                ),
                                            ),

                                            on_click=lambda e: self.showConsulta(),
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