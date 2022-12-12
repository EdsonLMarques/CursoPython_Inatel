"""
- Menu com opções
    - Cadastro
    - Mostrar todos usuarios
    - Mostrar ultimo cadastrado
    - Sair
"""


def cadastro():
    nome = input("Qual o seu nome: ").capitalize()
    idade = input("{}, qual a sua idade: ".format(nome))
    if 0 <= int(idade) < 18:
        maioridade = "menor"
    elif int(idade) >= 18:
        maioridade = "maior"
    else:
        print("Idade incorreta")
    return [nome, idade, maioridade]

def menu():
    print(
        "\n___MENU___\n"
        "1-Cadastrar\n"
        "2-Usuarios cadastrados\n"
        "3-Ultimo Cadastrado\n"
        "4-Deletar Usuario\n"
        "S-Sair\n"
    )
    resposta = input("")
    return resposta

def listarUsuarios(lista):
    for usuario in lista:
        print("{} - {} - {}".format(usuario[0], usuario[1], usuario[2]))

def mostrarUltimo(lista):
    ultimo_usuario = lista[-1]
    print("{} - {} - {}".format(lista[-1][0],
                                lista[-1][1],
                                lista[-1][2]
                                ))

    print("{} - {} - {}".format(ultimo_usuario[0],
                                ultimo_usuario[1],
                                ultimo_usuario[2]
                                ))

def deletarUsuario(nome, lista):
    i = 0
    for usuario in lista:
        if usuario[0].capitalize() == nome.capitalize():
            lista.pop(i)
            return lista
        i += 1

sair = False
lista_usuario = []
while sair == False:
    resposta = menu()
    if resposta == "1":
        usuario = cadastro()
        lista_usuario.append(usuario)
    elif resposta == "2":
        listarUsuarios(lista_usuario)
    elif resposta == "3":
        mostrarUltimo(lista_usuario)
    elif resposta == "4":
        nome = input("Quem voce quer excluir? ")
        deletarUsuario(nome, lista_usuario)
        # ou
        deletarUsuario(nome=nome, lista=lista_usuario)
    elif resposta.upper() == "S":
        sair = True
    else:
        print("Escolha uma opção correta")

listarUsuarios(lista_usuario)