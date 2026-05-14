from flet import *
from src.main.constructors.productConstructor import produtoConstructor

def app(page:Page):
    page.title = "Cadastro de Edulto"

<<<<<<< Updated upstream
    def changeRoute():
        page.views.clear()
        page.views.append(
            produtoConstructor(page)
        )

        page.update()

    page.on_route_change=changeRoute
    changeRoute()
=======

def main(page:Page):
    page.title = "Sistema de Estoque"
    page.theme_mode = ThemeMode.DARK
    page.bgcolor="#111827"
    container = Container(expand=True, padding=20,margin=Margin(0,0,25,0))
    container.bgcolor="#111827"

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
        bgcolor="#111827",
        extended=True,
        min_width=90,
        min_extended_width=240,
        group_alignment=-0.9,
        indicator_color="#2563EB",
        label_type=NavigationRailLabelType.NONE,

        leading=Container(
            padding=20,

            content=Column(
                tight=True,
                controls=[
                    Icon(
                        Icons.INVENTORY_2,
                        size=42,
                        color="#3B82F6",
                    ),

                    Text(
                        "StockPro",
                        size=24,
                        weight=FontWeight.BOLD,
                        color="white",
                    ),

                    Text(
                        "Controle de Estoque",
                        size=12,
                        color="#94A3B8",
                    ),
                ],
            ),
        ),
        destinations=[
            NavigationRailDestination(
                icon=Icons.HOME_OUTLINED,
                selected_icon=Icons.HOME,
                label="Home"
            ),
            NavigationRailDestination(
                icon=Icons.INVENTORY_2_OUTLINED,
                selected_icon=Icon(Icons.INVENTORY_2),
                label="Produtos",
            ),
            NavigationRailDestination(
                icon=Icons.LOCAL_SHIPPING_OUTLINED,
                selected_icon=Icon(Icons.LOCAL_SHIPPING),
                label="Fornecedores",
            ),
            NavigationRailDestination(
                icon=Icons.GROUP_OUTLINED,
                selected_icon=Icon(Icons.GROUP),
                label="Funcionários",
            ),
            NavigationRailDestination(
                icon=Icons.INVENTORY_2_OUTLINED,
                selected_icon=Icon(Icons.INVENTORY,),
                label="Estoque"
            ),
            NavigationRailDestination(
                icon=Icons.COMPARE_ARROWS_OUTLINED,
                selected_icon=Icon(Icons.COMPARE_ARROWS),
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
>>>>>>> Stashed changes
