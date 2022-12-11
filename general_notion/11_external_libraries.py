"""
Vamos aprender a usar aqui bibliotecas externas.
primeiro, o que sao bibliotecas externas?
Sao coletaneas de scripts, funções e classes capazes de executar funcionalidades de todos os tipos de complexidade.
Essas bibliotecas sao feitas por outros programadores e disponibilizadas para uso publico

Normlamente, quando vamos fazer um projeto mais extenso, muitas das funcionalidades basicas ja foram feitas por alguem e
elas estao nessas bibliotecas, basta encontra-las e utiliza-las.

Imagine a dificuldade que seria ter que criar uma biblioteca para retirar valores especificos de uma coluna do excel.
A biblioteca pandas já tem a solução para isso
Ou entao fazer t0do o trabalho de comunicação HTTP para que sua aplicação consiga acessar apenas verificar se tem internet

O primeiro passo é aprender a criar a nossas proprias bibliotecas
Para isso vamos voltar no exemplo de classes e transformar a classe Usuario em uma biblioteca externa.
1º - separar a classe em um outro arquivo
2º Dispoonibilizar
3º - Importar a classe
    from "caminho do arquivo.nome do arquivo" import "nome da função
"""

from files.Lib_Usuarios import Usuario

def menu_principal ():
    print("\n\n____menu____")
    print("1 - Cadastrar novo usuario\n"
          "2 - verificar lista de usuarios\n"
          "3 - Ultimo cadastrado\n"
          "4 - Deletar Item\n"
          "5 - mudar perido\n"
          "S - sair\n")
    return input()

sair = False
lista= []
while sair == False:
    menu = menu_principal()
    objeto = ""
    if menu == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        lista.append(Usuario(nome,idade))
    elif menu == "2":
        print("A lista de usuario é:")
        for objeto in lista:
            objeto.printaUsuario()
            if objeto.periodo > 0:
                objeto.mostraPeriodo()
    elif menu == "3":
        objeto = lista[-1]
        objeto.printaUsuario()
    elif menu =="4":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                lista.remove(objeto)
    elif menu == "5":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                objeto.mudaPerido()
    elif menu == "S":
        sair = True
print("\nprograma finalizado\n")



"""
Dessa forma podemos utilizar livremente nossas classes e funções de acordo com a necessidade.
Uma vez que essa biblioteca é importada, ela passa a ser conhecida como modulo.
O maior ganho que conseguimos dividindo um codigo em multiplos modulos é organização e escalabilidade, pois, tornamos todos
permitimos que alterações sejam feitas em locais especificos

Outro ganho é que, usando a padronização de entradas e saidas de uma função o projeto se torna quase que um quebra
cabeça, onde cada função se encaixa com a proximo, e mesmo que voce altera a forma com que aquela função trabalha, isso
nao ira afetar a proxima função
"""


"""
Para importarmos bibliotecas externas, o primeiro passo e escolhermos quais bibliotecas iremos utilizar. O exemplo que 
vou dar a voces envolve uma biblioteac de mapas chamada "Folium". Essa biblioteca consegue gerar paginas HTML com mapas
e com pontos interativos plotados.
Esse sera o nosso desafio final
Vou apenas executar o primeiro passo, os demais iremos executar juntos

como objetivo vamos criar uma aplicação que mostra um mapa, em uma localização especifica e com pontos interativos 
plotados.
todas as informações de laitude e longitude verião de um arquivo txt disponibilizados na pasta files (lat_lon.txt)

todo o processamento das informações deve ser feito em função ou classe seja elas externas (modulos) ou internas, porem,
manter a organização no projeto é crucial.

para auxilia-lo, utilize o site oficial da biblioteca:
https://python-visualization.github.io/folium/index.html

1º importar a biblioteca follium
    "pip install folium" ou "conda install folium -c conda-forge"
"""
#
# # passo 1
# import folium
#
# mapa = folium.Map(location=[-22.257044861335906, -45.69635809285212])
# mapa.save("index.html")

"""
abrindo a biblioteca com controle+click no "Map" podemos ver tudo que a biblioteca folium tem
podemos ver que essa primeira função pode ter muito mais parametros do que os que passamos
como por exemplo, zoom
"""
# passo 2
import folium

mapa = folium.Map(location=[-22.257044861335906, -45.69635809285212], zoom_start=17)
mapa.save("index.html")


"""
O proximo passo é entender como plotar pontos utilizando o folium
para isso vamos utilizar o metodo MARKER que precisa das seguintes informações
    location, popup, tooltip, icon, draggable
Nem todas essas informções sao realmente necessarias.
"""

# passo 3
import folium
lat_lon = [-22.257044861335906, -45.69635809285212]

mapa = folium.Map(location=lat_lon, zoom_start=17)

popup_text = "<i>Inatel</i>"
tooltip_text = "Clique aqui"

folium.Marker(location=lat_lon, popup=popup_text, tooltip=tooltip_text).add_to(mapa)

mapa.save("index.html")

"""
Vamos ao que interessa, plotar os pontos disponibilizados no lat_lon.txt e suas descrições
"""

