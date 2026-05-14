from src.model.DAO.movementDAO import MovimentoDAO
from src.model.DAO.productsDAO import ProdutosDAO

dao = MovimentoDAO()
daoP = ProdutosDAO()

def id():
    for i in dao.viewList():
        for j in daoP.viewList():
            if i["idProd"] == j["idProd"]:
                return j["nome"]

print(id())