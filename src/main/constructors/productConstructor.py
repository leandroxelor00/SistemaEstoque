import flet as ft


def main(page: ft.Page):
    page.title = "Sistema de Estoque"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0F172A"
    page.window.bgcolor = "#0F172A"

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#3B82F6",
            secondary="#38BDF8",
            surface="#1E293B",
        ),
        font_family="Poppins",
    )

    def titulo(texto):
        return ft.Text(
            texto,
            size=30,
            weight=ft.FontWeight.BOLD,
            color="white",
        )

    def subtitulo(texto):
        return ft.Text(
            texto,
            size=14,
            color="#94A3B8",
        )

    def campo(label, icon=None):
        return ft.TextField(
            label=label,
            prefix_icon=icon,
            border_radius=14,
            filled=True,
            bgcolor="#1E293B",
            border_color="#334155",
            focused_border_color="#3B82F6",
            color="white",
            label_style=ft.TextStyle(color="#CBD5E1"),
            cursor_color="#3B82F6",
        )

    def botao_primario(texto, icon=None, on_click=None):
        return ft.ElevatedButton(
            texto,
            icon=icon,
            on_click=on_click,
            height=48,
            style=ft.ButtonStyle(
                bgcolor="#2563EB",
                color="white",
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=5,
            ),
        )

    def botao_secundario(texto, icon=None, on_click=None):
        return ft.OutlinedButton(
            texto,
            icon=icon,
            on_click=on_click,
            height=48,
            style=ft.ButtonStyle(
                side=ft.BorderSide(1, "#334155"),
                color="#E2E8F0",
                shape=ft.RoundedRectangleBorder(radius=12),
            ),
        )

    def card(content):
        return ft.Container(
            bgcolor="#111827",
            border_radius=20,
            padding=30,
            expand=True,
            border=ft.Border(
                top=ft.BorderSide(1, "#1E293B"),
                bottom=ft.BorderSide(1, "#1E293B"),
                left=ft.BorderSide(1, "#1E293B"),
                right=ft.BorderSide(1, "#1E293B"),
            ),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color="#00000055",
                offset=ft.Offset(0, 4),
            ),
            content=content,
        )

    def view_cadastrar_produto():
        return card(
            ft.Column(
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                spacing=20,
                controls=[
                    titulo("Cadastrar Produto"),
                    subtitulo("Preencha as informações do produto."),
                    ft.Divider(color="#1E293B"),

                    campo("Nome do Produto", ft.Icons.INVENTORY_2_OUTLINED),
                    campo("Marca", ft.Icons.BRANDING_WATERMARK_OUTLINED),
                    campo("Preço", ft.Icons.ATTACH_MONEY),

                    ft.Row(
                        spacing=15,
                        controls=[
                            botao_primario("Salvar", ft.Icons.SAVE),
                            botao_secundario("Limpar", ft.Icons.CLEANING_SERVICES),
                        ],
                    ),
                ],
            )
        )

    def view_consultar_produto():
        return card(
            ft.Column(
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                spacing=20,
                controls=[
                    titulo("Consultar Produtos"),
                    subtitulo("Pesquise produtos cadastrados."),
                    ft.Divider(color="#1E293B"),

                    campo("Buscar produto", ft.Icons.SEARCH),

                    botao_primario("Buscar", ft.Icons.SEARCH),

                    ft.Container(
                        border_radius=16,
                        bgcolor="#1E293B",
                        padding=15,

                        content=ft.DataTable(
                            bgcolor="#1E293B",
                            heading_row_color="#0F172A",

                            columns=[
                                ft.DataColumn(ft.Text("Nome", color="white")),
                                ft.DataColumn(ft.Text("Marca", color="white")),
                                ft.DataColumn(ft.Text("Preço", color="white")),
                            ],

                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(
                                            ft.Text("Produto Exemplo", color="white")
                                        ),
                                        ft.DataCell(
                                            ft.Text("Marca Exemplo", color="white")
                                        ),
                                        ft.DataCell(
                                            ft.Text("R$ 0,00", color="white")
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )

    def view_cadastrar_funcionario():
        return card(
            ft.Column(
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                spacing=20,
                controls=[
                    titulo("Cadastrar Funcionário"),
                    subtitulo("Adicione novos funcionários."),
                    ft.Divider(color="#1E293B"),

                    campo("Nome Completo", ft.Icons.PERSON_OUTLINE),

                    ft.Row(
                        spacing=15,
                        controls=[
                            botao_primario("Salvar", ft.Icons.SAVE),
                            botao_secundario("Limpar", ft.Icons.CLEANING_SERVICES),
                        ],
                    ),
                ],
            )
        )

    def view_consultar_funcionario():
        return card(
            ft.Column(
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                spacing=20,
                controls=[
                    titulo("Consultar Funcionários"),
                    subtitulo("Pesquise funcionários cadastrados."),
                    ft.Divider(color="#1E293B"),

                    campo("Buscar funcionário", ft.Icons.SEARCH),

                    botao_primario("Buscar", ft.Icons.SEARCH),

                    ft.Container(
                        border_radius=16,
                        bgcolor="#1E293B",
                        padding=15,

                        content=ft.DataTable(
                            bgcolor="#1E293B",
                            heading_row_color="#0F172A",

                            columns=[
                                ft.DataColumn(ft.Text("Nome", color="white")),
                            ],

                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(
                                            ft.Text(
                                                "Funcionário Exemplo",
                                                color="white",
                                            )
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )

    def view_cadastrar_fornecedor():
        return card(
            ft.Column(
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                spacing=20,
                controls=[
                    titulo("Cadastrar Fornecedor"),
                    subtitulo("Adicione novos fornecedores."),
                    ft.Divider(color="#1E293B"),

                    campo("Nome", ft.Icons.LOCAL_SHIPPING_OUTLINED),

                    ft.Row(
                        spacing=15,
                        controls=[
                            botao_primario("Salvar", ft.Icons.SAVE),
                            botao_secundario("Limpar", ft.Icons.CLEANING_SERVICES),
                        ],
                    ),
                ],
            )
        )

    def view_consultar_fornecedor():
        return card(
            ft.Column(
                scroll=ft.ScrollMode.AUTO,
                expand=True,
                spacing=20,
                controls=[
                    titulo("Consultar Fornecedores"),
                    subtitulo("Pesquise fornecedores cadastrados."),
                    ft.Divider(color="#1E293B"),

                    campo("Buscar fornecedor", ft.Icons.SEARCH),

                    botao_primario("Buscar", ft.Icons.SEARCH),

                    ft.Container(
                        border_radius=16,
                        bgcolor="#1E293B",
                        padding=15,

                        content=ft.DataTable(
                            bgcolor="#1E293B",
                            heading_row_color="#0F172A",

                            columns=[
                                ft.DataColumn(
                                    ft.Text("Razão Social", color="white")
                                ),
                            ],

                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(
                                            ft.Text(
                                                "Fornecedor Exemplo",
                                                color="white",
                                            )
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )

    def tela_produtos():
        return card(
            ft.Column(
                expand=True,
                spacing=25,
                controls=[
                    titulo("Produtos"),
                    subtitulo("Gerencie os produtos do estoque."),

                    ft.Row(
                        spacing=15,
                        controls=[
                            botao_primario(
                                "Cadastrar Produto",
                                ft.Icons.ADD,
                                lambda e: trocar_corpo(
                                    view_cadastrar_produto()
                                ),
                            ),

                            botao_secundario(
                                "Consultar Produtos",
                                ft.Icons.SEARCH,
                                lambda e: trocar_corpo(
                                    view_consultar_produto()
                                ),
                            ),
                        ],
                    ),
                ],
            )
        )

    def tela_funcionarios():
        return card(
            ft.Column(
                expand=True,
                spacing=25,
                controls=[
                    titulo("Funcionários"),
                    subtitulo("Gerencie os funcionários."),

                    ft.Row(
                        spacing=15,
                        controls=[
                            botao_primario(
                                "Cadastrar Funcionário",
                                ft.Icons.ADD,
                                lambda e: trocar_corpo(
                                    view_cadastrar_funcionario()
                                ),
                            ),

                            botao_secundario(
                                "Consultar Funcionários",
                                ft.Icons.SEARCH,
                                lambda e: trocar_corpo(
                                    view_consultar_funcionario()
                                ),
                            ),
                        ],
                    ),
                ],
            )
        )

    def tela_fornecedores():
        return card(
            ft.Column(
                expand=True,
                spacing=25,
                controls=[
                    titulo("Fornecedores"),
                    subtitulo("Gerencie os fornecedores."),

                    ft.Row(
                        spacing=15,
                        controls=[
                            botao_primario(
                                "Cadastrar Fornecedor",
                                ft.Icons.ADD,
                                lambda e: trocar_corpo(
                                    view_cadastrar_fornecedor()
                                ),
                            ),

                            botao_secundario(
                                "Consultar Fornecedores",
                                ft.Icons.SEARCH,
                                lambda e: trocar_corpo(
                                    view_consultar_fornecedor()
                                ),
                            ),
                        ],
                    ),
                ],
            )
        )

    corpo = ft.Column(
        expand=True,
        controls=[tela_produtos()],
    )

    def trocar_corpo(nova_view):
        corpo.controls = [nova_view]
        page.update()

    def on_nav_change(e):
        index = e.control.selected_index

        if index == 0:
            trocar_corpo(tela_produtos())

        elif index == 1:
            trocar_corpo(tela_funcionarios())

        elif index == 2:
            trocar_corpo(tela_fornecedores())

    rail = ft.NavigationRail(
        selected_index=0,
        bgcolor="#111827",
        extended=True,
        min_width=90,
        min_extended_width=240,
        group_alignment=-0.9,
        indicator_color="#2563EB",
        label_type=ft.NavigationRailLabelType.NONE,
        on_change=on_nav_change,

        leading=ft.Container(
            padding=20,

            content=ft.Column(
                tight=True,
                controls=[
                    ft.Icon(
                        ft.Icons.INVENTORY_2,
                        size=42,
                        color="#3B82F6",
                    ),

                    ft.Text(
                        "StockPro",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),

                    ft.Text(
                        "Controle de Estoque",
                        size=12,
                        color="#94A3B8",
                    ),
                ],
            ),
        ),

        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.INVENTORY_2_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.INVENTORY_2),
                label="Produtos",
            ),

            ft.NavigationRailDestination(
                icon=ft.Icons.GROUP_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.GROUP),
                label="Funcionários",
            ),

            ft.NavigationRailDestination(
                icon=ft.Icons.LOCAL_SHIPPING_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.LOCAL_SHIPPING),
                label="Fornecedores",
            ),
        ],
    )

    page.add(
        ft.SafeArea(
            expand=True,

            content=ft.Row(
                expand=True,
                spacing=0,

                controls=[
                    rail,

                    ft.VerticalDivider(
                        width=1,
                        color="#1E293B",
                    ),

                    ft.Container(
                        expand=True,
                        padding=30,
                        content=corpo,
                    ),
                ],
            ),
        )
    )


ft.app(target=main)