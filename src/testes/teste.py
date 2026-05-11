from logging import disable

from flet import *

def app(page):

    texto1 = TextField(label="Sei la")
    texto2 = TextField(label="Texto disabled")

    def teste():
        if texto1.value.upper() == "DISABLED":
            texto2.disabled=True
        else:
            texto2.disabled=False


    texto1.on_change = teste
    page.add(texto1, texto2)
if __name__ == '__main__':
    run(app)