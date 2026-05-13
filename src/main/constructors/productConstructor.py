from src.views.viewProduct import ViewProduct

def productConstructor(page):
    viewProduct = ViewProduct(page)

    return viewProduct.build()