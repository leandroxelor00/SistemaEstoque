from flet import *

from src.controlers.movementController import MovementController
from src.controlers.searchMovementController import SearchMovementController
from src.model.DAO.employeeDAO import EmployeeDAO

class ViewMovement:
    def __init__(self, page):
        self.page = page
        self.cadastro_view = None
        self.consulta_view = None

        self.btn_cadastro = ElevatedButton(
            "Cadastrar Movimento",
            icon=Icons.SWAP_HORIZ_OUTLINED,
            bgcolor="#2563EB",
            color="white",
            scale=1.05,
            animate_scale=Animation(300, "easeOutBack"),
            animate_offset=Animation(300),
            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
            on_click=lambda e: self.show_cadastro(),
        )

        self.btn_consulta = ElevatedButton(
            "Consultar Movimentos",
            icon=Icons.SEARCH,
            bgcolor="#1E293B",
            color="white",
            scale=1.0,

            animate_scale=Animation(300, "easeOut"),

            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
            on_click=lambda e: self.show_consulta(),
        )

        self.sub_content = Container(
            expand=True,
            animate=Animation(400, "decelerate"),  # Animação da troca de tela
            opacity=1,
        )

    def update_button_visuals(self, active_tab):
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
        from src.views.viewRegMovement import ViewRegMovimento

        self.sub_content.opacity = 0
        self.page.update()

        if not self.cadastro_view:
            self.cadastro_view = ViewRegMovimento()
            MovementController(self.page, self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.sub_content.opacity = 1  # Fade-in
        self.update_button_visuals("cadastro")

    def show_consulta(self):
        from src.views.viewShowMovement import ViewShowMovement

        self.sub_content.opacity = 0
        self.page.update()

        if not self.consulta_view:
            self.consulta_view = ViewShowMovement()
            SearchMovementController(self.page, self.consulta_view)

        self.sub_content.content = self.consulta_view.build()
        self.sub_content.opacity = 1
        self.update_button_visuals("consulta")

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
                    Container(
                        padding=20,
                        border_radius=16,
                        bgcolor="#111827",
                        border=Border.all(1, "#1E293B"),
                        content=Column(
                            spacing=15,
                            controls=[
                                Text("Movimentações", size=28, weight="bold", color="white"),
                                Row(
                                    spacing=15,
                                    controls=[self.btn_cadastro, self.btn_consulta],
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
