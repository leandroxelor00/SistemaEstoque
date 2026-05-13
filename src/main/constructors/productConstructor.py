from src.controlers.productController import ProdutoController
from src.controlers.searchProductController import searchProductController
from src.controlers.movementController import MovementController
from src.views.viewMovement import ViewMovimento
from src.views.viewProduct import ViewProduto
from src.views.viewShowProduct import ViewShowProduct


# def produtoConstructor(page):
#     viewProduto = ViewProduto()
#     produtoConstructor = ProdutoController(page,viewProduto)
#
#     return viewProduto

# def produtoConstructor(page):
#     viewShowProduct = ViewShowProduct()
#     searchProductConstructor = searchProductController(page,viewShowProduct)
#
#     return viewShowProduct

<<<<<<< Updated upstream
def produtoConstructor(page):
    viewMovevement = ViewMovimento()
    movimento = MovementController(page,viewMovevement)

    return viewMovevement
=======
# def produtoConstructor(page):
#     viewMovevement = ViewMovimento()
#     movimento = MovementController(page,viewMovevement)
#
#     return viewMovevement

# def produtoConstructor(page):
#     viewShowMovement = ViewShowMovement()
#     showMovement = SearchMovementController(page,viewShowMovement)
#
#     return viewShowMovement

# def produtoConstructor(page):
#      viewEmployee = ViewEmployee()
#      employee = EmployeeController(page,viewEmployee)
#
#      return viewEmployee

# def produtoConstructor(page):
#      viewShowEmployee = ViewShowEmployee()
#      employee = SearchEmployeeController(page,viewShowEmployee)
#
#      return viewShowEmployee

# def produtoConstructor(page):
#     viewSupplier = ViewSupplier()
#     supplier = SupplierController(page, viewSupplier)
#
#     return viewSupplier

# def produtoConstructor(page):
#     viewShowSupplier = ViewShowSupplier()
#     showSupplier = SearchSupplierController(page, viewShowSupplier)
#
#     return viewShowSupplier
import flet as ft


def main(page: ft.Page):
   page.title = "Estoque"
   page.padding = 0


   def view_cadastrar_produto():
       return ft.Column(
           scroll=ft.ScrollMode.AUTO,
           expand=True,
           controls=[
               ft.Text("Cadastrar Produto", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.TextField(label="Nome do Produto"),
               ft.TextField(label="Marca"),
               ft.TextField(label="Preço"),
               ft.Row(
                   controls=[
                       ft.ElevatedButton("Salvar"),
                       ft.OutlinedButton("Limpar"),
                   ]
               ),
           ],
       )

   def view_consultar_produto():
       return ft.Column(
           scroll=ft.ScrollMode.AUTO,
           expand=True,
           controls=[
               ft.Text("Consultar Produtos", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.TextField(label="Buscar produto", prefix_icon=ft.Icons.SEARCH),
               ft.ElevatedButton("Buscar"),
               ft.Divider(),
               ft.DataTable(
                   columns=[
                       ft.DataColumn(ft.Text("Nome")),
                       ft.DataColumn(ft.Text("Marca")),
                       ft.DataColumn(ft.Text("Preço")),
                   ],
                   rows=[
                       ft.DataRow(cells=[
                           ft.DataCell(ft.Text("001")),
                           ft.DataCell(ft.Text("Produto Exemplo")),
                           ft.DataCell(ft.Text("R$ 0,00")),
                           ft.DataCell(ft.Text("0")),
                       ]),
                   ],
               ),
           ],
       )


   def view_cadastrar_funcionario():
       return ft.Column(
           scroll=ft.ScrollMode.AUTO,
           expand=True,
           controls=[
               ft.Text("Cadastrar Funcionário", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.TextField(label="Nome Completo"),
               ft.Row(
                   controls=[
                       ft.ElevatedButton("Salvar"),
                       ft.OutlinedButton("Limpar"),
                   ]
               ),
           ],
       )

   def view_consultar_funcionario():
       return ft.Column(
           scroll=ft.ScrollMode.AUTO,
           expand=True,
           controls=[
               ft.Text("Consultar Funcionários", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.TextField(label="Buscar funcionário", prefix_icon=ft.Icons.SEARCH),
               ft.ElevatedButton("Buscar"),
               ft.Divider(),
               ft.DataTable(
                   columns=[
                       ft.DataColumn(ft.Text("Nome")),
                   ],
                   rows=[
                       ft.DataRow(cells=[
                           ft.DataCell(ft.Text("Funcionário Exemplo")),
                       ]),
                   ],
               ),
           ],
       )


   def view_cadastrar_fornecedor():
       return ft.Column(
           scroll=ft.ScrollMode.AUTO,
           expand=True,
           controls=[
               ft.Text("Cadastrar Fornecedor", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.TextField(label="Nome"),
               ft.Row(
                   controls=[
                       ft.ElevatedButton("Salvar"),
                       ft.OutlinedButton("Limpar"),
                   ]
               ),
           ],
       )

   def view_consultar_fornecedor():
       return ft.Column(
           scroll=ft.ScrollMode.AUTO,
           expand=True,
           controls=[
               ft.Text("Consultar Fornecedores", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.TextField(label="Buscar fornecedor", prefix_icon=ft.Icons.SEARCH),
               ft.ElevatedButton("Buscar"),
               ft.Divider(),
               ft.DataTable(
                   columns=[
                       ft.DataColumn(ft.Text("Razão Social")),
                   ],
                   rows=[
                       ft.DataRow(cells=[
                           ft.DataCell(ft.Text("Fornecedor Exemplo")),

                       ]),
                   ],
               ),
           ],
       )


   def tela_produtos():
       return ft.Column(
           expand=True,
           controls=[
               ft.Text("Produtos", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.Row(
                   controls=[
                       ft.ElevatedButton(
                           "Cadastrar Produto",
                           icon=ft.Icons.ADD,
                           on_click=lambda e: trocar_corpo(view_cadastrar_produto()),
                       ),
                       ft.OutlinedButton(
                           "Consultar Produtos",
                           icon=ft.Icons.SEARCH,
                           on_click=lambda e: trocar_corpo(view_consultar_produto()),
                       ),
                   ]
               ),
           ],
       )

   def tela_funcionarios():
       return ft.Column(
           expand=True,
           controls=[
               ft.Text("Funcionários", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.Row(
                   controls=[
                       ft.ElevatedButton(
                           "Cadastrar Funcionário",
                           icon=ft.Icons.ADD,
                           on_click=lambda e: trocar_corpo(view_cadastrar_funcionario()),
                       ),
                       ft.OutlinedButton(
                           "Consultar Funcionários",
                           icon=ft.Icons.SEARCH,
                           on_click=lambda e: trocar_corpo(view_consultar_funcionario()),
                       ),
                   ]
               ),
           ],
       )

   def tela_fornecedores():
       return ft.Column(
           expand=True,
           controls=[
               ft.Text("Fornecedores", size=24, weight=ft.FontWeight.BOLD),
               ft.Divider(),
               ft.Row(
                   controls=[
                       ft.ElevatedButton(
                           "Cadastrar Fornecedor",
                           icon=ft.Icons.ADD,
                           on_click=lambda e: trocar_corpo(view_cadastrar_fornecedor()),
                       ),
                       ft.OutlinedButton(
                           "Consultar Fornecedores",
                           icon=ft.Icons.SEARCH,
                           on_click=lambda e: trocar_corpo(view_consultar_fornecedor()),
                       ),
                   ]
               ),
           ],
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
       label_type=ft.NavigationRailLabelType.ALL,
       min_width=100,
       min_extended_width=400,
       group_alignment=-0.9,
       on_change=on_nav_change,
               destinations=[
                   ft.NavigationRailDestination(
                       icon=ft.Icons.PERSON_SEARCH_OUTLINED,
                       selected_icon=ft.Icon(ft.Icons.PERSON_SEARCH),
                       label="Produtos",
                   ),
                   ft.NavigationRailDestination(
                       icon=ft.Icons.PERSON_SEARCH_OUTLINED,
                       selected_icon=ft.Icon(ft.Icons.PERSON_SEARCH),
                       label="Funcionarios"
                   ),
                   ft.NavigationRailDestination(
                       icon=ft.Icons.PERSON_SEARCH_OUTLINED,
                       selected_icon=ft.Icon(ft.Icons.PERSON_SEARCH),
                       label="Fornecedores"
                   ),
               ],
           )

   page.add(
       ft.SafeArea(
           expand=True,
           content=ft.Row(
               expand=True,
               controls=[
                   rail,
                   ft.VerticalDivider(width=1),
                   ft.Container(
                       expand=True,
                       padding=24,
                       content=corpo,
                   ),
               ],
           ),
       )
   )


ft.app(target=main)
>>>>>>> Stashed changes
