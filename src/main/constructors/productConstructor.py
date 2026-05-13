from src.controlers.productController import ProdutoController
from src.views.viewProduct import ViewProduto

def productConstructor(page):
    viewProduto = ViewProduto()
    ProdutoController(page, viewProduto)

    return viewProduto.build()