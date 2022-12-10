# o primeiro pensamento quando precisamos executar o mesmo codigo algumas ou varias vezes é escreve-lo varias vezes
# Na liguagem de programação existem artficios para resolver esse problema, o primeiro deles é o FOR
# o FOR é um loop com quantidade definida, exemplo se quisermos cadastrar 5 usuarios podemos
# Para auxiliar no for, vamos usar uma função interna do python chamada range, o range tem um começo "0" e um final "5"
# ele ira contar de 1 em 1 ate chegar no seu final, o qual nao sera executado.
# apenas para demonstrar o RANGE vamos printar todos os valores do range de 0 a 10

for valor in range(0, 10, 2):
    print(valor)


# voltando ao exemplo, vamos cadastrar 5 usuarios analisado o nome e idade.
# for numero_usuario in range(0,5):
    idade = int(input("Qual a idade: "))
    nome = input("Qual o nome: ")
    print("{} tem {} anos de idade".format(nome, idade))
    if idade >= 18:
        print("{} é maior de idade".format(nome))
    else:
        print("{} é menor de idade".format(nome))
    print("_____")

# com o for, seremos obrigados a cadastrar exatamente 5 usuarios. sendo que, da forma que o codigo foi escrito é impossivel alterar essa quantidade pela interface
# Para resolver esse problema, podemos usar um outro tipo de loop o WHILE ou em portugues "enquanto"
# para explicar o uso do while:

numero = 0
while numero < 5:
    print(numero)
    numero+=1

# ou ainda, com auxilio de um input

numero = int(input("escolha um numero: "))
while numero < 5:
    numero = int(input("escolha outro numero: "))

# EXERCICIO
# Vamos criar um sistema para cadastrar n usuarios questionando apos cada cadastro,
# se ele quer continuar cadastrando novos usuarios.
# alem disso, vamos guardar em uma lista todos os nomes, idades e se sao maiores ou nao

continuar = "S"
lista = []
while continuar != "N":
    nome = input("entre com seu nome: ")
    idade = input("{} qual a sua idade? ".format(nome))
    if int(idade) >= 18:
        maioridade = "maior"
    else:
        maioridade = "menor"
    print("{} de {} é {} de idade".format(nome, idade, maioridade))
    lista.append([nome, idade, maioridade])
    continuar = input("Deseja conferir mais alguem? S/N")
print("foi cadastrado os seguintes usuarios")
for nome, idade, maioridade in lista:
    print("{} - {} - {}".format(nome, idade, maioridade))