from src.controlers.productController import ProdutoController
from src.controlers.searchProductController import searchProductController
from src.controlers.movementController import MovementController
from src.controlers.employeeController import EmployeeController
from src.controlers.searchEmployeeController import SearchEmployeeController
from src.controlers.searchMovementController import SearchMovementController
from src.controlers.searchSupplierController import SearchSupplierController
from src.controlers.stockController import StockController
from src.controlers.supplierController import SupplierController
from src.controlers.searchStockController import SearchStockController
from src.views.viewShowEmployee import ViewShowEmployee
from src.views.viewEmployee import ViewEmployee
from src.views.viewShowMovement import ViewShowMovement
from src.views.viewMovement import ViewMovimento
from src.views.viewProduct import ViewProduto
from src.views.viewShowProduct import ViewShowProduct
from src.views.viewShowStock import ViewShowStock
from src.views.viewShowSupplier import ViewShowSupplier
from src.views.viewStock import ViewStock
from src.views.viewSupplier import ViewSupplier


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

# def produtoConstructor(page):
#     viewStock = ViewStock()
#     stock = StockController(page, viewStock)
#
#     return viewStock

def produtoConstructor(page):
    viewShowStock = ViewShowStock()
    showStock = SearchStockController(page,viewShowStock)

    return viewShowStock