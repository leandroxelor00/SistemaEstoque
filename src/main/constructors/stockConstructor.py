from src.views.viewStock import ViewStock

def stockConstructor(page):
    viewStock = ViewStock(page)

    return viewStock.build()
