from src.controlers.supplierController import SupplierController
from src.views.viewSupplier import ViewSupplier

def supplierConstructor(page):
    viewSupplier = ViewSupplier()
    SupplierController(page, viewSupplier)

    return viewSupplier.build()