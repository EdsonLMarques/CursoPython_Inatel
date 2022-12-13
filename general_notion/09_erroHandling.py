"""
Uma coisa que voces viram ate agora, é que sempre que entravamos com um valor errado em algum momento, o codigo gerava
um erro.
Esse erro fazia com que o sistema travasse e tivessemos que reinicia-lo

para solucionar isso, o python oferece o "try-except" que é literalemente "tenta isso, se nao der tenta isso..."

vamos usar ele para solucionar o problema que tivemos com a questao da idade nao ser numerica.
"""


while True:
    try:
        idade = int(input("entre com uma idade: "))
        print("a idade é {} \n".format(idade))
    except:
        print("voce entrou com um valor nao numerico")

"""
nesse exemplo, criamos uma forma de evitar que o codigo trave após um erro do usuario.
Seu uso é essencial para qualquer aplicação nao apenas para evitar que ela trava mas tambem para podermos mostrar ao 
usuario ou desenvolvedor, o que esta acontecendo de errado no script
"""

class Usuario:
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
    if menu == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        lista.append(Usuario(nome,idade))
    elif menu == "2":
         for objeto in lista:
             print("{} - {} - {}".format(objeto.nome, objeto.idade, objeto.maioridade))
    elif menu == "3":
        objeto = lista[-1]
        print("{} - {} - {}".format(objeto.nome, objeto.idade, objeto.maioridade))
    elif menu =="4":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                lista.remove(objeto)
    elif menu == "S":
        sair = True
print("\nprograma finalizado\n")