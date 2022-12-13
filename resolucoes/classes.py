"""
Exercicio, vamos incrementar juntos essa classe de usuario para tornar o codigo mais completo.
para isso vamos adicionar os seguintes
- Criar um metodo para printar nome, idade e maioridade
    trocar no flxuo principal a forma com que as informações sao printadas
- Criar um metodo para modificar a idade e executar novamente o teste de maioridade
- Criar um atributo chamado periodo, que sempre incia zerado e nao é obrigatorio
- criar um metodo para modificar o periodo

- criar um metodo que mostra se o usuario tem um periodo e se tiver, em qual periodo ele esta.
    Essa função deve ser executada ao printar a lista de usuarios
"""


# classe Usuario
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome.capitalize()
        self.idade = int(idade)
        self.maioridade = self.testaMarioridade()
        self.periodo = 0

    def testaMarioridade(self):
        if self.idade >= 18:
            return "Maior"
        else:
            return "Menor"

    def PrintaUsuario(self):
        print("\n{} - {} - {}".format(self.nome, self.idade, self.maioridade))
        self.printaPeriodo()

    def MudaIdade(self, idade):
        self.idade = int(idade)
        self.maioridade = self.testaMarioridade()

    def MudaPeriodo(self, periodo):
        self.periodo = int(periodo)

    def printaPeriodo(self):
        if self.periodo > 0:
            print("O aluno {} esta no {}º periodo".format(self.nome, self.periodo))
        else:
            print("O aluno {} não esta em uma faculdade".format(self.nome))

# fluxo padrão de informações
def menu_principal ():
    print("\n\n____menu____")
    print("1 - Cadastrar novo usuario\n"
          "2 - verificar lista de usuarios\n"
          "3 - Ultimo cadastrado\n"
          "4 - Deletar Item\n "
          "5 - Muda idade\n"
          "6 - Escolhe Periodo\n"
          "S - sair\n")
    return input()

sair = False
lista= []
while sair == False:
    menu = menu_principal()
    if menu == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        lista.append(Usuario(nome, idade))
    elif menu == "2":
         for objeto in lista:
             objeto.PrintaUsuario()
    elif menu == "3":
        objeto = lista[-1]
        objeto.PrintaUsuario()
    elif menu == "4":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                lista.remove(objeto)
    elif menu == "5":
        nome = input("Nome: ").capitalize()
        idade = input("Nova idade: ")
        for objeto in lista:
            if nome == objeto.nome:
                objeto.MudaIdade(idade=idade)
    elif menu == "6":
        nome = input("Nome: ").capitalize()
        periodo = input("Periodo: ")
        for objeto in lista:
            if nome == objeto.nome:
                objeto.MudaPeriodo(periodo=periodo)
    elif menu == "S":
        sair = True
print("\nprograma finalizado\n")
