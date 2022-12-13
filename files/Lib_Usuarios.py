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
