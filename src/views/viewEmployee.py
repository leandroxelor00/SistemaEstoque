from flet import *

from src.controlers.searchEmployeeController import SearchEmployeeController
from src.controlers.employeeController import EmployeeController


class ViewEmployee:

    def __init__(self, page):
        self.page = page

        self.cadastro_view = None
        self.consulta_view = None

        self.btn_cadastrar = ElevatedButton(
            "Cadastrar Funcionário",
            icon=Icons.PERSON_ADD,
            bgcolor="#2563EB",
            color="white",
            scale=1.05,
            animate_scale=Animation(300, "easeOutBack"),
            style=ButtonStyle(
                padding=20,
                shape=RoundedRectangleBorder(radius=12),
            ),
            on_click=lambda e: self.showCadastro(),
        )

        self.btn_consultar = ElevatedButton(
            "Consultar Funcionários",
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
            self.btn_cadastrar.bgcolor = "#2563EB"
            self.btn_cadastrar.scale = 1.05
            self.btn_cadastrar.elevation = 8

            self.btn_consultar.bgcolor = "#1E293B"
            self.btn_consultar.scale = 0.95
            self.btn_consultar.elevation = 0
        else:
            self.btn_consultar.bgcolor = "#2563EB"
            self.btn_consultar.scale = 1.05
            self.btn_consultar.elevation = 8

            self.btn_cadastrar.bgcolor = "#1E293B"
            self.btn_cadastrar.scale = 0.95
            self.btn_cadastrar.elevation = 0

        self.page.update()

    def showCadastro(self):
        from src.views.viewRegEmployee import ViewRegEmployee

        self.sub_content.opacity = 0
        self.page.update()

        if not self.cadastro_view:
            self.cadastro_view = ViewRegEmployee()
            EmployeeController(self.page, self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.sub_content.opacity = 1
        self.update_visuals("cadastro")

    def showConsulta(self):
        from src.views.viewShowEmployee import ViewShowEmployee

        self.sub_content.opacity = 0
        self.page.update()

        if not self.consulta_view:
            self.consulta_view = ViewShowEmployee()
            SearchEmployeeController(self.page, self.consulta_view)

        self.sub_content.content = self.consulta_view.build()
        self.sub_content.opacity = 1
        self.update_visuals("consulta")

    def build(self):
        self.showCadastro()

        return Container(
            expand=True,
            padding=20,
            bgcolor="#0F172A",
            content=Column(
                expand=True,
                controls=[
                    Container(
                        padding=20,
                        border_radius=16,
                        bgcolor="#111827",
                        border=Border.all(1, "#1E293B"),
                        margin=Margin(0, 0, 0, 20),
                        content=Column(
                            spacing=15,
                            controls=[
                                Text("Funcionários", size=28, weight="bold", color="white"),
                                Text("Gerencie os funcionários do sistema.", size=14, color="#94A3B8"),
                                Row(
                                    spacing=15,
                                    controls=[
                                        self.btn_cadastrar,
                                        self.btn_consultar,
                                    ]
                                )
                            ]
                        )
                    ),
                    Container(
                        expand=True,
                        padding=20,
                        border_radius=16,
                        bgcolor="#111827",
                        border=Border.all(1, "#1E293B"),
                        content=self.sub_content
                    )
                ]
            )
        )