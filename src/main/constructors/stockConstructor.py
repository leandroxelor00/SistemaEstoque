from src.controlers.stockController import StockController
from src.views.viewStock import ViewStock

def stockConstructor(page):
    viewStock = ViewStock()
    StockController(page, viewStock)

    return viewStock.build()
