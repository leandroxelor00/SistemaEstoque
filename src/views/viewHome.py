import flet as ft
from src.views.viewProduct import ViewProduto  # ← Import mantido


def main(page: ft.Page):
    page.title = "Sistema com NavigationRail"
    page.window_width = 1000
    page.window_height = 650
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    # ====================== NavigationRail ======================
    def change_navigation(e):
        routes = {0: "/home", 1: "/product", 2: "/usuarios", 3: "/config"}
        page.go(routes.get(e.control.selected_index, "/home"))

    navigation = ft.NavigationRail(
        selected_index=0,
        extended=True,
        min_width=100,
        min_extended_width=220,
        label_type=ft.NavigationRailLabelType.ALL,
        leading=ft.Icon(ft.Icons.STORE, size=40),
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.INVENTORY_2_OUTLINED, selected_icon=ft.Icons.INVENTORY_2, label="Produtos"),
            ft.NavigationRailDestination(icon=ft.Icons.PEOPLE_OUTLINED, selected_icon=ft.Icons.PEOPLE, label="Usuários"),
            ft.NavigationRailDestination(icon=ft.Icons.SETTINGS_OUTLINED, selected_icon=ft.Icons.SETTINGS, label="Configurações"),
        ],
        on_change=change_navigation,
    )

    # ====================== Layout Base ======================
    def layout_page(content: ft.Control):
        return ft.Row(
            [
                navigation,
                ft.VerticalDivider(width=1),
                ft.Container(
                    expand=True,
                    padding=30,
                    content=content,
                )
            ],
            expand=True,
        )

    # ====================== Route Change ======================
    def route_change(e):
        page.views.clear()

        # Atualiza o item selecionado no menu
        route_to_index = {"/home": 0, "/product": 1, "/usuarios": 2, "/config": 3}
        navigation.selected_index = route_to_index.get(page.route, 0)

        # ==================== Rotas ====================
        # ... (restante do código anterior igual)

        # ==================== Rotas ====================
        if page.route == "/product":
            # Agora ViewProduto é uma Column, então funciona como 'body'
            body = ViewProduto()

        elif page.route == "/home":
            body = ft.Column([
                ft.Text("Tela HOME", size=32, weight=ft.FontWeight.BOLD),
                ft.Text("Bem-vindo ao sistema!", size=16),
            ], spacing=20)

        # ... (restante do código igual)

        elif page.route == "/usuarios":
            body = ft.Text("Tela de Usuários", size=24)

        elif page.route == "/config":
            body = ft.Text("Tela de Configurações", size=24)

        else:
            body = ft.Text(f"Página não encontrada: {page.route}", size=20, color=ft.Colors.RED_400)

        page.views.append(
            ft.View(
                route=page.route,
                controls=[layout_page(body)],
                padding=0,
            )
        )
        page.update()

    def view_pop(e):
        page.views.pop()
        page.go(page.views[-1].route)

    # ====================== Configuração ======================
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Inicialização
    page.go("/home" if page.route in ("/", "") else page.route)


if __name__ == '__main__':
    ft.run(main, port=8000)