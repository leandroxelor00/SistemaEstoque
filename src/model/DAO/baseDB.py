import json
from json import JSONDecodeError

class BaseDB:

    def __init__(self,fileDB:str):
        # self.__path = fr"E:\Aulas\SistemaEstoque\src\infrastructure\database\{fileDB}"
        self.__path = fr"C:\Users\rafael.smoralli\Documents\GitHub\SistemaEstoque\src\infrastructure\database\{fileDB}"
        self.__fileDB = fileDB

    def listData(self):
        try:
            with open(self.__path,"r+", encoding="utf-8") as file:
                return json.load(file)
        except JSONDecodeError:
            return []
        except:
            raise ValueError("Erro ao abrir o arquivo: ",self.__fileDB)


    def save(self,data):
        listDB = self.listData()
        try:
            with open(self.__path,"w",encoding="utf-8") as file:
                listDB.append(data)
                json.dump(listDB,file,indent=4,ensure_ascii=False)
                print("Salvo com susseeço")
        except:
            raise print("Erro ao salvar no arquivo: ", self.__fileDB)


    def saveList(self, data):
        try:
            with open(self.__path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                print("Salvo com susseeço")
        except:
            raise print("Erro ao salvar a lista do produto deletado: ", self.__fileDB)
