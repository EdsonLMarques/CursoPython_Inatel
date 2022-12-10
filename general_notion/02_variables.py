# para colocarmos as informações do nome, precisamos entender primeiro o que sao as variaveis e como elas se comportam

# declarando uma variavel
# NOME_DA_VARIAVEL = VALOR_DA_VARIAVEL
numero = 0
string = "Rumo Ao Hexa"
lista = []
tupla = ()
dicionario = {}

print("declaração inicial")
print("variavel numero", type(numero))
print("variavel string", type(string))
print("variavel lista", type(lista))
print("variavel tupla", type(tupla))
print("variavel dicionario", type(dicionario), "\n\n")

# Python tem tipagem fraca, ou seja, as variaveis sao maleaveis, podendo assumir diferentes tipos independente do que
# era antes
# logo, podemos modificar as variaveis da seguinte forma
numero = []
string = ()
lista = {}
tupla = 0
dicionario = "Rumo Ao Hexa"

print("Modificando tipos")
print("variavel numero", type(numero))
print("variavel string", type(string))
print("variavel lista", type(lista))
print("variavel tupla", type(tupla))
print("variavel dicionario", type(dicionario), "\n\n")


# Numero pode ser INT (inteiro) ou FLOT (ponto flutuante)
# Uma string é um conjunto de caracteres
# Lista é um conjunto de dados de varios tipos. A lista pode ser modificada
# Tupla é um conjunto de dados de varios tipos. A tupla nao pode ser modificada, porem é indexada*
# Set é um conjunto de dados de varios tipos. O Set nao pode ser modificado nem indexado*
# Dicionario é um conjunto de Duplas de dados, sendo que o primeiro é a chave e o segundo o valor. O valor pode ser modificado
# Em etapas futuras vamos ver mais a fundo como trabalhar com cada um deles.
# * indexação siginifca identificar cada item do conjunto com um ID unico.

# lista, tupla e set


# dicionario