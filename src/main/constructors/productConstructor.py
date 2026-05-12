from src.controlers.productController import ProdutoController
from src.controlers.searchProductController import searchProductController
from src.controlers.movementController import MovementController
from src.controlers.employeeController import EmployeeController
from src.controlers.searchEmployeeController import SearchEmployeeController
from src.controlers.searchMovementController import SearchMovementController
from src.views.viewShowEmployee import ViewShowEmployee
from src.views.viewEmployee import ViewEmployee
from src.views.viewShowMovement import ViewShowMovement
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

def produtoConstructor(page):
     viewShowEmployee = ViewShowEmployee()
     employee = SearchEmployeeController(page,viewShowEmployee)

     return viewShowEmployee