# classe Usuario

class Usuario ():
    def __init__(self):





# fluxo padrão de informações

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