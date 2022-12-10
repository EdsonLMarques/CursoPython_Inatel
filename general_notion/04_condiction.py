# para resolver a questao criada no exercicio anterior, vamos precisar fazer a seguinte pergunta:
# SE a idedade for maior ou igual a 18 anos, entao o usuario é maior de idade
# o principal pergunta é o "SE", que em python é escrito como IF
# Seguindo o exemplo anterior:

idade = input("Qual a seu idade: ")
nome = input("Qual a sua nome: ")
print("{} tem {} anos de idade".format(nome, idade))
if idade > 18:
    print("{} é maior de idade".format(nome))


# porem se tentarmos usar o codigo anterior, vamos ter um erro dizendo que é impossivel comparar um inteiro com uma string
# Tudo que vem do "INPUT" é sempre uma string, logo, precisamos transformar essa string para inteiro para isso fazemos
idade = int(input("Qual a seu idade: "))

idade = int(input("Qual a seu idade: "))
nome = input("Qual a sua nome: ")
print("{} tem {} anos de idade".format(nome, idade))
if idade > 18:
    print("{} é maior de idade".format(nome))

# agora, como indicar que o usuario é menor de idade.
# temos 2 formas, a primeira é criar um novo if perguntando se ele é menor que 18

idade = int(input("Qual a seu idade: "))
nome = input("Qual a sua nome: ")
print("{} tem {} anos de idade".format(nome, idade))
if idade >= 18:
    print("{} é maior de idade".format(nome))
if idade < 18:
    print("{} é menor de idade".format(nome))

# OU utiliamos um artificio chamado SENÃO, ou seja, caso nenhuma condição nao for atendida...
# o codigo ficaria dessa foma

idade = int(input("Qual a seu idade: "))
nome = input("Qual a sua nome: ")
print("{} tem {} anos de idade".format(nome, idade))
if idade >= 18:
    print("{} é maior de idade".format(nome))
else:
    print("{} é menor de idade".format(nome))


# ainda poderiamos criar outras condições, como analisar se a idade é negativa ou com valores estranhos
# outro ponto inportante é caso formos executar o mesmo codigo mais de uma vez
