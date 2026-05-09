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

def produtoConstructor(page):
    viewMovevement = ViewMovimento()
    movimento = MovementController(page,viewMovevement)

    return viewMovevement