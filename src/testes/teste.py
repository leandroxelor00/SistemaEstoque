from flet import *
from src.main.constructors.productConstructor import productConstructor
from src.main.constructors.searchProductConstructor import searchProductConstructor


def main(page:Page):
    page.title = "Sistema de Estoque"
    page.window_width = 1000
    page.window_height = 600
    page.padding = 0
    page.theme_mode = ThemeMode.DARK

    # Container que vai receber o conteúdo
    content_container = Container(expand=True, padding=20)

    # Função para trocar o conteúdo diretamente
    def change_content(index):
        if index == 0:  # Home
            content_container.content = Column(
                [
                    Text("🏠 Home", size=40, weight=FontWeight.BOLD),
                    Text("Bem-vindo ao Sistema de Estoque", size=20),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                expand=True,
            )
        elif index == 1:  # Produtos
            content_container.content = productConstructor(page)
        elif index == 2:  # Produtos
            content_container.content = searchProductConstructor(page)

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
                label="Produtos"
            ),
            NavigationRailDestination(
                icon=Icons.CIRCLE_OUTLINED,
                label="Consultar Produtos"
            ),
        ],
        on_change=lambda e: change_content(e.control.selected_index),
    )

    # Layout
    page.add(
        Row(
            [
                navigation,
                VerticalDivider(width=1),
                content_container,
            ],
            expand=True,
        )
    )

    # Inicia com Home
    change_content(0)


if __name__ == '__main__':
    run(main)