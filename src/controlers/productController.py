from src.infrastructure.services.idGen import GeradorID
from src.model.entities.product import Produto
from src.model.DAO.productsDAO import ProdutosDAO
from src.views.viewProduct import ViewProduto
from flet import *

class ProdutoController:

    def __init__(self,page,tela:ViewProduto):
        self.dao = ProdutosDAO()
        self.page = page
        tela.btnCadastrarProduto.on_click=self.handleAddProd
        self.tela = tela
        self.listarProdutos()

    def listarProdutos(self):
        self.tela.tabelaProduto.rows.clear()
        for produto in self.dao.viewList():
            linhas = DataRow(
                cells=[
                    DataCell(Text(produto["idProd"])),
                    DataCell(Text(produto["nome"])),
                    DataCell(Text(produto["marca"])),
                    DataCell(Text(produto["valor"]))
                ]
            )
            self.tela.tabelaProduto.rows.append(linhas)
        self.page.update()


    def buscarProdutoID(self,id:int):
        try:
            return self.dao.searchById(id)
        except:
            print("sei la, deu erro ao procurar, deve ser isso, pelo ID")

    def handleAddProd(self):
        print("Entrou no handleAddProd")
        p = Produto(GeradorID("products.json", "idProd").idGerado, self.tela.nomeProd.value, self.tela.marcaProd.value, self.tela.valorProd.value)


        try:
            self.dao.addProd(p.produto())
            self.tela.nomeProd.value = ""
            self.tela.marcaProd.value = ""
            self.tela.valorProd.value = ""
            self.tela.nomeProd.update()
            self.tela.marcaProd.update()
            self.tela.valorProd.update()
            self.listarProdutos()
        except Exception as e:
            print(e)
