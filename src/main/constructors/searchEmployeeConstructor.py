from src.controlers.searchEmployeeController import SearchEmployeeController
from src.views.viewShowEmployee import ViewShowEmployee

def searchEmployeeConstructor(page):
    viewShowEmployee = ViewShowEmployee()
    SearchEmployeeController(page,viewShowEmployee)

    return viewShowEmployee.build()