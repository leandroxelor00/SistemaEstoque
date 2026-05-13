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
            content=Row(
                controls=[
                    self.btn_cadastrar,
                    Container(width=10),
                    self.btn_consultar,
                ],
                alignment=MainAxisAlignment.START,
            ),
            padding=Padding.all(10),
            border=Border.all(2,"Black"),
            border_radius=5,
            margin=margin.only(bottom=20),
        )

        self.showCadastro()

        return Column(
            controls=[
                sub_nav_bar,
                self.sub_content,
            ],
            expand=True,
        )