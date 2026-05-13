from src.views.viewEmployee import ViewEmployee

def employeeConstructor(page):
    viewEmployee = ViewEmployee(page)

    return viewEmployee.build()