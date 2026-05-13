from flet import *
from src.main.constructors.productConstructor import productConstructor

def app(page:Page):
    page.title = "Sistema de Estoque"

    def changeRoute():
        page.views.clear()
        page.views.append(
            productConstructor(page)
        )

        page.update()

    page.on_route_change=changeRoute
    changeRoute()
