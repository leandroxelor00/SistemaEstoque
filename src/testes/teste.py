from flet import *

def app(page):

    selectFunc = Dropdown(label="Fornecedor", width=250, height=50)

    lista = [{"id": 1, "nome": "Dani"},
             {"id": 2, "nome": "Mari"}]

    listaNomes = []

    for i in lista:
        listaNomes.append(dropdown.Option(text=i["nome"]))

    selectFunc.options = listaNomes
    page.add(selectFunc)

if __name__ == '__main__':
    run(app)