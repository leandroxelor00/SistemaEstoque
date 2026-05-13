from flet import *

from src.main.constructors.movementConstructor import movementConstructor
from src.main.constructors.productConstructor import productConstructor
from src.main.constructors.employeeConstructor import employeeConstructor
from src.main.constructors.stockConstructor import stockConstructor
from src.main.constructors.supplierConstructor import supplierConstructor


def main(page:Page):
    page.title = "Sistema de Estoque"
    page.theme_mode = ThemeMode.DARK

    container = Container(expand=True, padding=20,margin=Margin(0,0,25,0))

    def changeContent(index):
        if index == 0:  # Home
            container.content = Column(
                [
                    Text("Bem-vindo ao Sistema de Estoque", size=40),
                    Text("Escolha uma opção à esquerda", size=20, weight=FontWeight.BOLD),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                expand=True,
            )
        elif index == 1:  # Produtos
            container.content = productConstructor(page)
        elif index == 2:  # Fornecedores
            print("ta entrando")
            container.content = supplierConstructor(page)
            print("ta atualizando")
        elif index == 3:  # Funcionários
            container.content = employeeConstructor(page)
        elif index == 4:  # Estoque
            container.content = stockConstructor(page)
        elif index == 5:  # Movimentações
            container.content = movementConstructor(page)

        page.update()

    # NavigationRail
    navigation = NavigationRail(
        selected_index=0,
        extended=True,
        label_type=NavigationRailLabelType.ALL,
        destinations=[
            NavigationRailDestination(
                icon=Icons.HOME_OUTLINED,
                selected_icon=Icons.HOME,
                label="Home"
            ),
            NavigationRailDestination(
                icon=Icons.INVENTORY_2_OUTLINED,
                selected_icon=Icons.INVENTORY_2,
                label="Produtos",
            ),
            NavigationRailDestination(
                icon=Icons.CIRCLE_OUTLINED,
                label="Fornecedores"
            ),
            NavigationRailDestination(
                icon=Icons.CIRCLE_OUTLINED,
                label="Funcionários"
            ),
            NavigationRailDestination(
                icon=Icons.CIRCLE_OUTLINED,
                label="Estoque"
            ),
            NavigationRailDestination(
                icon=Icons.CIRCLE_OUTLINED,
                label="Movimentos"
            ),
        ],
        on_change=lambda e: changeContent(e.control.selected_index),
    )

    page.add(
        Row(
            [
                navigation,
                VerticalDivider(width=50),
                container,
            ],
            expand=True,
        )
    )

    changeContent(0)