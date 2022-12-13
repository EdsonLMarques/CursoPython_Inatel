"""
Uma classe é o template de um objeto.
Um objeto é uma coletanea de dados e metodos (funções) unico e separado.
Fazendo um paralelo, uma classe é uma forma de bolo, e os bolos assados ali, segue o formato (peso, altura, contorno)
da forma, porem cada um deles é unico.
Um script ou projeto pode ter inumeras classes, e cada objeto, instaceado por aquela classe, carregará metodos daquela
classe
por exemplo, imagine um banco, onde voce tem uma classe chamada Cliente, nessa classe, cada cliente precisa do seus
proprios Dados ,Numero da conta, senha, saldo alem de funções exclusivas que podem ser feitas em uma conta, como por
exemplo, Sacar ou depositar dinheiro, verificar o saldo

para criarmos uma função, usamos a Tag "CLASS" seguida do nome da função e seus herança (nao vamos falar de herança aqui)
Apenas para curiosidade, uma erança siginifca que a classe ira ter aspectos de outra classe, dessa forma voce pode separar
informações em um novo objeto, porem ele faz uso de metodos de outros que foram herdados

Uma ves que a classe foi criada, precisamos definir quais os paremetros iniciais dela, ou seja, suas variaveis.
Para essa criação sempre utilizamos uma nova função seguido da tag "__init_", o parametro "SELF" e os paremetros que devem ser passados para a inicialização
o parametro self inidica que aquela função esta se autoreferenciando, ou seja, acessando as informações contidas naquele objeto criado
após a inicialização, cada novo metodo deve ser declarado como uma função.

Vamos continuar com exemplo anterior, vamos criar um menu, e esse menu ira decidir quais metodos de uma classe Usuario
dentro dessa classe, em breve vamos criar alguns novos metodos para um usuario"""

# classe Usuario
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
    objeto = Usuario(nome, idade)
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

#_______________________________________________________________________________________________________________________

"""
um informação importante no python é que nao existem metodos ou propriedades privadas, tudo pode ser acessado.
Porem por convenção, foi criado uma indicação de que algo é privado e nao deveria ser acessado ou modificado diretamente.
para isso usamos o underline "_" ou duplo "_" antes de uma variavel (propriedade) ou metodo da classe

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome.capitalize()
        self.idade = int(idade)
        self.maioridade = self.__testaMarioridade()

    def __testaMarioridade(self):
        if self.idade >= 18:
            return "Maior"
        else:
            return "Menor"
Para esse exemplo, isso indica a outros desenvolvedores que o metodo "testaMarioridade"
nunca deve ser acessado diretamente com um objeto.testamaioridade, pois seu acesso direto pode ser prejudicial a aplicação em questao

"""
#_______________________________________________________________________________________________________________________

"""
Existem outras informações que uma classe pode ter, como metodos de get e set, que pemitem a utilização de uma função
apenas para modificar ou buscar uma valor especifico do objeto nao vamos entrar em detalhes, mas esses metodos 
especificos chamados de setter e gatter permitem que uma informação especifica seja encontrada ou modificadas, eles sao
usados principalmente quando queremos permitir um caminho seguro para se buscar ou modificar uma propriedade daquele 
objeto, seja ele considerado privado ou nao.
"""

#_______________________________________________________________________________________________________________________
"""
Exercicio, vamos incrementar juntos essa classe de usuario para tornar o codigo mais completo.
para isso vamos adicionar os seguintes
- Criar um metodo para printar nome, idade e maioridade
- trocar no flxuo principal a forma com que as informações sao printadas
- Criar um metodo para modificar a idade e executar novamente o teste de maioridade
- Criar um atributo chamado periodo, que sempre incia zerado e nao é obrigatorio
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
    def printaUsuario(self):
        print("{} - {} - {}".format(self.nome, self.idade, self.maioridade))

    def mudaIdade(self, idade):
        self.idade = idade
        self.maioridade = self.testaMarioridade()

    def mudaPerido(self):
        ok = False
        periodo = int(input("Entre com um periodo para o usuario {}".format(self.nome)))
        while ok == False:
            if 0 <= periodo <= 10:
                self.periodo = int(periodo)
                ok = True
            else:
                periodo = int(input("Periodo invalido, tente novamente"))

    def mostraPeriodo(self):
        if self.periodo > 0:
            print("{} tem {} anos e esta no {}º periodo".format(self.nome, self.idade, self.periodo))
        else:
            print("{} nao esta na faculdade".format(self.nome))

# fluxo padrão de informações
def menu_principal ():
    print("\n\n____menu____")
    print("1 - Cadastrar novo usuario\n"
          "2 - verificar lista de usuarios\n"
          "3 - Ultimo cadastrado\n"
          "4 - Deletar Item\n"
          "5 - mudar perido\n"
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
        print("A lista de usuario é:")
        for objeto in lista:
            objeto.printaUsuario()
            if objeto.periodo > 0:
                objeto.mostraPeriodo()
    elif menu == "3":
        objeto = lista[-1]
        objeto.printaUsuario()
    elif menu =="4":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                lista.remove(objeto)
    elif menu == "5":
        nome = input("Nome: ").capitalize()
        for objeto in lista:
            if nome == objeto.nome:
                objeto.mudaPerido()
    elif menu == "S":
        sair = True
print("\nprograma finalizado\n")