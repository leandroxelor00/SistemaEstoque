from src.controlers.searchStockController import SearchStockController
from src.views.viewShowStock import ViewShowStock

def searchStockConstructor(page):
    viewShowStock = ViewShowStock()
    SearchStockController(page,viewShowStock)

    return viewShowStock.build()