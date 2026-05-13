
from src.views.viewSupplier import ViewSupplier

def supplierConstructor(page):
    viewSupplier = ViewSupplier(page)

    return viewSupplier.build()