# continuando a ideia da interface
# vamos perguntar o nome e emitir um "OLA + nome do usuario"
# existem varias formas de se trabalhar com frases prontas + variaveis

print("Sistema de Nomes TIPO 01")
nome = input("entre com seu nome: ")
print("Olá ", nome, "\n\n")

print("Sistema de Nomes TIPO 02")
nome = input("entre com seu nome: ")
print("Olá {} \n\n".format(nome))

print("Sistema de Nomes TIPO 03")
nome = input("entre com seu nome: ")
print("Olá {argumento} \n\n".format(argumento=nome))

# Diferentes cenarios precisam de diferentes soluções. Sempre analise qual o mais eficiente para resolver o
# problema que voce esta enfrentando

# vamos imaginar que queriamos agora mostrar a idade do usuario junto com o nome.
idade = input("Qual a seu idade: ")
nome = input("Qual a sua nome: ")
print("{} tem {} anos de idade".format(nome, idade))

# para incrementar, vamos dizer se o usuario é maior ou menor de idade.