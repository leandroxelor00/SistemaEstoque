from flet import *

def app(page):

    def onClick():
        texto2.value = selecionar.value

    btn = Button("Printar o valor do campo",on_click=onClick)
    selecionar = Dropdown(label="Tipo de Movimento", width=150, height=50,
                    options=[dropdown.Option("Entrada"),
                             dropdown.Option("Saída")])
    texto = Text("Valor: ")
    texto2 = Text("")
    linha = ResponsiveRow(controls=[texto,texto2])



    page.add(selecionar,btn,linha)

if __name__ == '__main__':
    run(app)





