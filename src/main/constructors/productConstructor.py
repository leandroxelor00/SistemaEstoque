from src.controlers.productController import ProdutoController
from src.controlers.searchProductController import searchProductController
from src.views.viewProduct import ViewProduto
from src.views.viewShowProduct import ViewShowProduct


# def produtoConstructor(page):
#     viewProduto = ViewProduto()
#     produtoConstructor = ProdutoController(page,viewProduto)
#
#     return viewProduto

def produtoConstructor(page):
    viewShowProduct = ViewShowProduct()
    searchProductConstructor = searchProductController(page,viewShowProduct)

    return viewShowProduct