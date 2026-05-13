from flet import *

from src.controlers.searchMovementController import SearchMovementController
from src.controlers.movementController import MovementController


class ViewMovement:
    #View principal das movimentações

    def __init__(self, page):
        self.page = page

        self.cadastro_view = None
        self.consulta_view = None

        self.sub_content = Container(expand=True)

        self.btn_cadastrar = Button(
            "Cadastrar Movimento",
            on_click=lambda e: self.show_cadastro()
        )

        self.btn_consultar = Button(
            "Consultar Movimentos",
            on_click=lambda e: self.show_consulta()
        )

    def show_cadastro(self):

        from src.views.viewRegMovement import ViewRegMovimento

        if not self.cadastro_view:
            self.cadastro_view = ViewRegMovimento()
            MovementController(self.page,self.cadastro_view)

        self.sub_content.content = self.cadastro_view.build()
        self.page.update()

    def show_consulta(self):

        from src.views.viewShowMovement import ViewShowMovement

        if not self.consulta_view:
            self.consulta_view = ViewShowMovement()
            SearchMovementController(self.page,self.consulta_view)

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

        self.show_cadastro()

        return Column(
            controls=[
                sub_nav_bar,
                self.sub_content,
            ],
            expand=True,
        )