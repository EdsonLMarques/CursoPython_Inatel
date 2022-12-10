# O python contem inumeras funções internas que permitem um desenolvimento rapido e eficiente
# Algumas dessas funções ja estao sendo utilizadas como é o caso do "INPUT()" ou da transformação de string para inteiro
# o "INT()"
# alem dessas funções, temos os methodos (funções especificas)
# pegando como exemplo uma variavel tipo lista

minha_lista_1 = ["maça","banana","pera","BWM"]
tamanho_lista = len(minha_lista_1)
print("a lista tem o total de {} elementos".format(tamanho_lista))

#adicionando um item na utima posição
minha_lista_1.append("melancia")
print("lista 1 = {}".format(minha_lista_1))

#adicionando um item em uma posição especifica
minha_lista_1.insert(0, "abobora")
print("lista 1 = {}".format(minha_lista_1))

# retirando um item por posição
minha_lista_1.pop(3)
print("lista 1 = {}".format(minha_lista_1))

# retirando um item por valor
minha_lista_1.remove("melancia")
print("lista 1 = {}".format(minha_lista_1))

# invertendo a lista
minha_lista_1.reverse()
print("lista 1 = {}".format(minha_lista_1))

# existem funções para inumeros cenarios e objetivos. Continuando com o exemplo de cadastro de usuario,
# vamos entender como fazer uso desses metodos para conseguir contruir um sistema de cadastro melhor
# lembrando que vamos continuar o exemplo do ultimo exercicio

continuar = "S"
lista = []
while continuar.upper().strip() != "N":
    nome = input("entre com seu nome: ").capitalize()
    idade = input("{} qual a sua idade? ".format(nome))
    while not (idade.isnumeric()) and (idade > 0 and idade < 120):
        print("Voce entrou com um dado invalido")
        idade = input("{} qual a sua idade? ".format(nome))
    if int(idade) >= 18:
        maioridade = "maior"
    else:
        maioridade = "menor"
    print("{} de {} é {} de idade".format(nome, idade, maioridade))
    lista.append([nome, idade, maioridade])
    continuar = input("Deseja conferir mais alguem? S/N\n")

print("\n___________________________________\n"
      "foi cadastrado os seguintes usuarios")
for nome, idade, maioridade in lista:
    print("{} - {} - {}".format(nome, idade, maioridade))