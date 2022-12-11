# classe Usuario

class Usuario ():
    def __init__(self, nome, idade):
        self.nome = nome.capitalize()
        self.idade = int(idade)
        self.maioridade = self.testaMarioridade()

    def testaMarioridade(self):
        if self.idade >= 18:
            return "Maior"
        else:
            return "Menor"

# fluxo padrão de informações
def menu_principal ():
    print("\n\n____menu____")
    print("1 - Cadastrar novo usuario\n"
          "2 - verificar lista de usuarios\n"
          "3 - Ultimo cadastrado\n"
          "4 - Deletar Item "
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
         for objeto in lista:
             print("{} - {} - {}".format(objeto.nome, objeto.idade, objeto.maioridade))
    elif menu == "3":
        objeto = lista[-1]
    elif menu =="4":
        nome = input("Nome: ")
    elif menu == "S":
        sair = True
print("\nprograma finalizado\n")