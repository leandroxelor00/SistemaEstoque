from flet import *

from src.controlers.searchSupplierController import SearchSupplierController
from src.controlers.supplierController import SupplierController


class ViewSupplier:
    # View principal dos fornecedores

    def __init__(self, page):
        self.page = page

        self.cadastro_view = None
        self.consulta_view = None

        self.sub_content = Container(
            expand=True,
            animate=Animation(300, "ease"),
        )

    def show_cadastro(self):

        from src.views.viewRegSupplier import ViewRegSupplier

        if not self.cadastro_view:
            self.cadastro_view = ViewRegSupplier()
            SupplierController(self.page, self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.page.update()

    def show_consulta(self):

        from src.views.viewShowSupplier import ViewShowSupplier

        if not self.consulta_view:
            self.consulta_view = ViewShowSupplier()
            SearchSupplierController(self.page, self.consulta_view)

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
                                    "Fornecedores",
                                    size=28,
                                    weight="bold",
                                    color="white",
                                ),

                                Text(
                                    "Gerencie os fornecedores cadastrados.",
                                    size=14,
                                    color="#94A3B8",
                                ),

                                Row(
                                    spacing=15,

                                    controls=[

                                        ElevatedButton(
                                            "Cadastrar Fornecedor",
                                            icon=Icons.LOCAL_SHIPPING_OUTLINED,

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
                                            "Consultar Fornecedores",
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