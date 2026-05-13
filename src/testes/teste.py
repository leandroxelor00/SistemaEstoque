import flet as ft
from src.main.constructors.productConstructor import produtoConstructor


def main(page: ft.Page):
    page.title = "Sistema de Estoque - Debug"
    page.window_width = 1200
    page.window_height = 700
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900

    # ====================== NavigationRail ======================
    def change_navigation(e):
        routes = {0: "/home", 1: "/product", 2: "/usuarios", 3: "/config"}
        page.go(routes.get(e.control.selected_index, "/home"))

    navigation = ft.NavigationRail(
        selected_index=0,
        extended=True,
        min_width=100,
        min_extended_width=240,
        label_type=ft.NavigationRailLabelType.ALL,
        leading=ft.Icon(ft.Icons.STORE, size=40),
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.INVENTORY_2_OUTLINED, selected_icon=ft.Icons.INVENTORY_2,
                                         label="Produtos"),
            ft.NavigationRailDestination(icon=ft.Icons.PEOPLE_OUTLINED, selected_icon=ft.Icons.PEOPLE,
                                         label="Usuários"),
            ft.NavigationRailDestination(icon=ft.Icons.SETTINGS_OUTLINED, selected_icon=ft.Icons.SETTINGS,
                                         label="Configurações"),
        ],
        on_change=change_navigation,
    )

    def layout_page(content):
        return ft.Row([navigation, ft.VerticalDivider(width=1), ft.Container(expand=True, padding=20, content=content)],
                      expand=True)

    # ====================== Route Change com Debug ======================
    def route_change(e):
        try:
            page.views.clear()

            route_to_index = {"/home": 0, "/product": 1, "/usuarios": 2, "/config": 3}
            navigation.selected_index = route_to_index.get(page.route, 0)

            if page.route == "/product":
                print("🔄 Carregando produtoConstructor...")  # debug
                body = produtoConstructor(page)
                print("✅ produtoConstructor carregado com sucesso")

            elif page.route == "/home":
                body = ft.Column([ft.Text("🏠 HOME", size=32, weight=ft.FontWeight.BOLD)], expand=True)

            else:
                body = ft.Text(f"Página: {page.route}", size=20)

            page.views.append(ft.View(route=page.route, controls=[layout_page(body)], padding=0))
            page.update()

        except Exception as ex:
            print(f"❌ ERRO no route_change: {ex}")
            import traceback
            traceback.print_exc()

            # Mostra erro na tela
            body = ft.Column([
                ft.Text("Erro ao carregar a tela", size=24, color=ft.Colors.RED_400),
                ft.Text(str(ex), color=ft.Colors.RED_200),
            ])
            page.views.append(ft.View(route=page.route, controls=[layout_page(body)], padding=0))
            page.update()

    def view_pop(e):
        page.views.pop()
        page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/home")


if __name__ == '__main__':
    ft.run(main, port=8000)