from src.controlers.employeeController import EmployeeController
from src.views.viewEmployee import ViewEmployee

def employeeConstructor(page):
    viewEmployee = ViewEmployee()
    EmployeeController(page,viewEmployee)

    return viewEmployee.build()