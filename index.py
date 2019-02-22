#-*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

class Scanner():

    def __init__(self,tags):
        ListaFiles = []
        directory  = os.path.join(os.getcwd(),"www")
        ListaFiles = self.searchByFolder(directory)
        self.searchbayidFiles(ListaFiles,tags)

    
    def searchByFolder(self,directory):
        absolutePath = os.path.abspath(directory)
        ListFiles = []
        for currentfolder, subFolders, files  in os.walk(absolutePath):
           if not currentfolder.find('lib') > 0:
                ListFiles.extend([os.path.join(currentfolder,archive) for archive in files if archive.endswith('.html')])
           
        return ListFiles

    def searchbayidFiles(self,files,tags):
        
        allFiles = []

        for f in files:
            try:
                with open(f) as fp:
                    soup = BeautifulSoup(fp,"html5lib")

                listItems = []

                # tag = ["button","input"]

                for item in soup.findAll(tags):
                    if item.get('id') == None:
                        listItems.append(item)

                allFiles.append({"pagina":f,"items":listItems})

            except:
                print("Arquivo {%s} não encontrado no diretorio" % (f))
            
        
        for i in allFiles:
            if len(i['items']) > 0:
                print("##############-INICIO-##################")
                print("Arquivo: {%s} , Contém {%s} tags sem id \n" % (i['pagina'],len(i['items'])))
                for x in i['items']:
                    print("%s \n"%x)
                print("#####################-FIM-#########################")
                print("\n")

        try:
            file_name = "log.txt"
            archive = open(file_name, 'r+',encoding='UTF-8')
        except FileNotFoundError:
            archive = open(file_name, 'w+',encoding='UTF-8')
        
        
        for i in allFiles:
            if len(i['items']) > 0:
                archive.writelines(u"##############-INICIO-##################\n")
                archive.writelines(u"Arquivo: {%s} , Contém {%s} tags sem id \n" % (i['pagina'],len(i['items'])))
                for x in i['items']:
                    archive.writelines(u"%s \n" % (x))
                archive.writelines(u"#####################-FIM-#########################\n")
        
        archive.writelines(u" \n")
        archive.close()
                
           
#Inicia a aplicação
print("#===============================#")
print("|      Verificador de id        |")
print("#===============================#")
print("|  default ['input','button']   |")
print("#===============================#")
Lista = input("insira as tag que deseja procurar separadas por (,) para valores default aperte enter: ")
if len(Lista) > 0 :
    tags = Lista.split(",")
else:
    tags = ["input","button"]

scanner = Scanner(tags)






