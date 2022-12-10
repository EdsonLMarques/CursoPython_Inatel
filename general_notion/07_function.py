# nesse capitulo vamos aprender a criar nossas proprias funções
# primeiro, para que queremos criar funções?
# o principal objetivo é criar um codigo padrão que pode ser reutilizado quantas vezes quisermos, apenas nos momentos necesssario.
# Outro imenso ganho que usar funções nos tras é a organização do codigo.
# Todas as funções no python seguem o mesmo modelo, sao definidas pela tag "DEF" seguido pelo nome e entre parenteses fica a informação dos parametros de entrada.
# por fim, ao final da função temos um "RETURN" que indica o que sera retornado por essa função

def minha_funcao (entrada_da_funcao):
    return entrada_da_funcao.upper()

nome = input("entre com um nome: ")
novo_nome = minha_funcao(nome)
print(novo_nome)

# essa função criada vai pegar uma string, independente de qual for e transformar todas as letras para maiusculo
# é uma função muito simples e talvez ate desnecessaria, porem nos da uma ideia de como funções funcionam

# vamos pensar em um exemplo mais complexo. vamos imaginar o sistema de cadastro porem com uma especie de menu incial
# onde posso escolher, encerrar o programa, cadastrar um novo usuario e ver a lista de usuarios.
# Vamos partir do principio que o script ja esta pronto e nos precisamos apenas colocar eles em funções especificas.
# talvez voce olhe para esse codigo e pense... nao esta tao complexo e que usar funções possa ser um pouco exagerado
# Pense que vamos ter que adicionar novas funcionalidades como verificar o ultimo que foi cadastrado ou ainda que precisamos deletar um item especifico.


#sem funções
sair = False
lista= []
while sair == False:
    print("____menu____")
    print("1 - Cadastrar novo usuario\n"
          "2 - verificar lista de usuarios\n"
          "3 - sair\n")
    menu = input()
    if menu == "1":
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
    elif menu == "2":
        print("foi cadastrado os seguintes usuarios")
        for nome, idade, maioridade in lista:
            print("{} - {} - {}".format(nome, idade, maioridade))
    elif menu == "3":
        sair = True

print("\nprograma finalizado\n")

# com função
def menu_principal ():
    print("____menu____")
    print("1 - Cadastrar novo usuario\n"
          "2 - verificar lista de usuarios\n"
          "3 - sair\n")
    return input()

def cadastro ():
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
    # return lista

def usuarios_cadastrados (lista_de_usuarios):
    print("foi cadastrado os seguintes usuarios")
    for nome, idade, maioridade in lista_de_usuarios:
        print("{} - {} - {}".format(nome, idade, maioridade))


sair = False
lista= []
while sair == False:
    menu = menu_principal()
    if menu == "1":
        cadastro()
    elif menu == "2":
        usuarios_cadastrados(lista)
    elif menu == "3":
        sair = True
print("\nprograma finalizado\n")

# incrementando um processo com funções

# incrementando o codigo para mostrar a real uso da funções
def menu_principal ():
    print("\n\n____menu____")
    print("1 - Cadastrar novo usuario\n"
          "2 - verificar lista de usuarios\n"
          "3 - Ultimo cadastrado\n"
          "4 - Deletar Item "
          "S - sair\n")
    return input()

def cadastro ():
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
    return lista

def usuarios_cadastrados (lista_de_usuarios):
    print("foi cadastrado os seguintes usuarios")
    for nome, idade, maioridade in lista_de_usuarios:
        print("{} - {} - {}".format(nome, idade, maioridade))

def ultimo_cadastro ():
    if len(lista) > 0:
        nome, idade, maioridade = lista.pop()
        print("{} - {} - {}".format(nome, idade, maioridade))
    else:
        print("Sem Usuarios cadastrados")

def deletar(lista_de_usuarios):
    nome_para_deletar = input("Escreve o nome do usuario que voce deseja deletar: ").capitalize()
    i = 0
    for nome, idade, maioridade in lista_de_usuarios:
        if nome_para_deletar == nome:
            lista_de_usuarios.pop(i)
            return lista_de_usuarios
        i += 1


sair = False
lista= []
while sair == False:
    menu = menu_principal()
    if menu == "1":
        lista = cadastro()
    elif menu == "2":
        usuarios_cadastrados(lista)
    elif menu == "3":
        ultimo_cadastro()
    elif menu =="4":
        lista = deletar(lista)
    elif menu == "S":
        sair = True
print("\nprograma finalizado\n")