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



