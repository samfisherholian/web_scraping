import requests
import re

#variavel que recebe o input de link do wikipedia
checagem = ""

#artigo usado como exemplo: https://en.wikipedia.org/wiki/Car

#funcao que lista os indices da pagina
def indices():

    #pega o html da pagina inteira
    req = requests.get(str(checagem))

    # expressao que da match nos indices
    indice = re.findall('<li class=".+"><a href="#(.+)"><span class="tocnumber">.+<\/span> <span class="toctext">.+<\/span><\/a>',req.text)
    
    for index in indice:
        print(index)

#funcao que pega todos os nomes de arquivos de imagen da pagina
def nomesArquivoImagens():

    req = requests.get(str(checagem))
    
    #da match em todos os nomes de arquivos de imagens .jpg, png e JPG
    imagefile = re.findall(r'([\w\-\d(?=.+#_$%&@)]*)\.(jpg|png|JPG)',req.text)

    for image in imagefile:
        print(image)
    
#funcao que lista os links da pagina
def listaLinks():

    req = requests.get(str(checagem))
    
    #expressao que da match nos links da pagina da wikipedia
    links = re.findall(r'href="/wiki/([\w._+?&@%#=()!\/-]*)', req.text)

    for link in links:
        print("https://en.wikipedia.org/wiki/{}".format(link))

if __name__ == "__main__":

    checagem = str(input("digite o link para verificar: "))

    #expressao que verifica se o link eh da wikipedia
    x = re.search('\w.*.wikipedia.org.*', checagem)

    #se o link for do wikipedia entao imprime 'bateu' e executa o menu'
    #se nao, entao imprime uma mensagem 'o link nao eh do wikipedia' e encerra o programa
    if x:

        print("bateu")

    else:

        print("o link nao eh do wikipedia: ")

        exit()    

    #menu onde o usuario escolhe uma das opcoes 
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('''digite 1 para listar os indices \ndigite 2 para ver os nomes de arquivos de imagens \ndigite 3 para listar todos os links do artigo''')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    menu = int(input())

    #verifica so numero digitado eh igual ao do menu e maior que 0, entao executa a funcao chamada
    if menu == 1 and menu > 0:

        indices()

    if menu == 2 and menu > 0:

        nomesArquivoImagens()

    if menu == 3 and menu > 0:

        listaLinks()    
