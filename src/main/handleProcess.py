from flet import *
from src.main.constructors.productConstructor import produtoConstructor

def app(page:Page):
    page.title = "Cadastro de Edulto"

    def changeRoute():
        page.views.clear()
        page.views.append(
            produtoConstructor(page)
        )

        page.update()

    page.on_route_change=changeRoute
    changeRoute()
