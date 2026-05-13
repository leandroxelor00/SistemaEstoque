from src.controlers.SearchProductController import SearchProductController
from src.views.viewShowProduct import ViewShowProduct

def searchProductConstructor(page):
    viewShowProduct = ViewShowProduct()
    SearchProductController(page, viewShowProduct)

    return viewShowProduct.build()