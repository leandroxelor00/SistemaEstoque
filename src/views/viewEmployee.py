from flet import *

from src.controlers.searchEmployeeController import SearchEmployeeController
from src.controlers.employeeController import EmployeeController


class ViewEmployee:
    #View principal dos funcionários

    def __init__(self, page):
        self.page = page

        self.cadastro_view = None
        self.consulta_view = None

        self.sub_content = Container(expand=True)

        self.btn_cadastrar = Button(
            "Cadastrar funcionário",
            on_click=lambda e: self.showCadastro()
        )

        self.btn_consultar = Button(
            "Consultar funcionários",
            on_click=lambda e: self.showConsulta()
        )

    def showCadastro(self):

        from src.views.viewRegEmployee import ViewRegEmployee

        if not self.cadastro_view:
            self.cadastro_view = ViewRegEmployee()
            EmployeeController(self.page,self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.page.update()

    def showConsulta(self):

        from src.views.viewShowEmployee import ViewShowEmployee

        if not self.consulta_view:
            self.consulta_view = ViewShowEmployee()
            SearchEmployeeController(self.page,self.consulta_view)

        self.sub_content.content = self.consulta_view.build()
        self.page.update()

    def build(self):

        sub_nav_bar = Container(
            padding=20,
            border_radius=16,
            bgcolor="#111827",
            border=Border.all(1, "#1E293B"),
            margin=Margin(0, 0, 0, 20),

            content=Column(
                spacing=15,
                controls=[

                    Text(
                        "Funcionários",
                        size=28,
                        weight="bold",
                        color="white",
                    ),

                    Text(
                        "Gerencie os funcionários do sistema.",
                        size=14,
                        color="#94A3B8",
                    ),

                    Row(
                        spacing=15,
                        controls=[

                            ElevatedButton(
                                "Cadastrar Funcionário",
                                icon=Icons.PERSON_ADD,
                                bgcolor="#2563EB",
                                color="white",
                                style=ButtonStyle(
                                    padding=20,
                                    shape=RoundedRectangleBorder(radius=12),
                                ),
                                on_click=lambda e: self.showCadastro(),
                            ),

                            ElevatedButton(
                                "Consultar Funcionários",
                                icon=Icons.SEARCH,
                                bgcolor="#1E293B",
                                color="white",
                                style=ButtonStyle(
                                    padding=20,
                                    shape=RoundedRectangleBorder(radius=12),
                                ),
                                on_click=lambda e: self.showConsulta(),
                            ),
                        ]
                    )
                ]
            )
        )

        self.showCadastro()

        return Container(
            expand=True,
            padding=20,
            bgcolor="#0F172A",

            content=Column(
                expand=True,
                controls=[

                    sub_nav_bar,

                    Container(
                        expand=True,
                        padding=20,
                        bgcolor="#111827",

                        content=self.sub_content
                    )
                ]
            )
        )