from src.controlers.searchSupplierController import SearchSupplierController
from src.views.viewShowSupplier import ViewShowSupplier

def searchSupplierConstructor(page):
    viewShowSupplier = ViewShowSupplier()
    SearchSupplierController(page, viewShowSupplier)

    return viewShowSupplier.build()