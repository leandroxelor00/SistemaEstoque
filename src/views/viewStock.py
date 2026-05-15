from flet import *

from src.controlers.searchStockController import SearchStockController
from src.controlers.stockController import StockController


class ViewStock:

    def __init__(self, page):
        self.page = page
        self.cadastro_view = None
        self.consulta_view = None

        self.btn_cadastro = ElevatedButton(
            "Cadastrar no Estoque",
            icon=Icons.INVENTORY_2_OUTLINED,
            bgcolor="#2563EB",  # Ativo por padrão
            color="white",
            scale=1.05,
            animate_scale=Animation(300, "easeOutBack"),
            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
            on_click=lambda e: self.showCadastro(),
        )

        self.btn_consulta = ElevatedButton(
            "Consultar Estoque",
            icon=Icons.SEARCH,
            bgcolor="#1E293B",
            color="white",
            scale=1.0,
            animate_scale=Animation(300, "easeOutBack"),
            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
            on_click=lambda e: self.showConsulta(),
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

    def showCadastro(self):
        from src.views.viewRegStock import ViewRegStock

        self.sub_content.opacity = 0
        self.page.update()

        if not self.cadastro_view:
            self.cadastro_view = ViewRegStock()
            StockController(self.page, self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.sub_content.opacity = 1
        self.update_visuals("cadastro")

    def showConsulta(self):
        from src.views.viewShowStock import ViewShowStock

        self.sub_content.opacity = 0
        self.page.update()

        if not self.consulta_view:
            self.consulta_view = ViewShowStock()
            SearchStockController(self.page, self.consulta_view)

        self.sub_content.content = self.consulta_view.build()
        self.sub_content.opacity = 1
        self.update_visuals("consulta")

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
                                Text("Estoque", size=28, weight="bold", color="white"),
                                Text("Gerencie os produtos disponíveis no estoque.", size=14, color="#94A3B8"),
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