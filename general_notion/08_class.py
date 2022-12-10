# Uma classe é o template de um objeto.
# Um objeto é uma coletanea de dados e metodos (funções) unico e separado
# Fazendo um paralelo, uma classe é uma forma de bolo, e os bolos assados ali, segue o formato (peso, altura, contorno) da forma, porem cada um deles é unico.
# Um script ou projeto pode ter inumeras classes, e cada objeto, instaceado por aquela classe, carregará metodos daquela classe
# por exemplo, imagine um banco, onde voce tem uma classe chamada Cliente, nessa classe, cada cliente precisa do seus
# proprios Dados ,Numero da conta, senha, saldo alem de funções exclusivas que podem ser feitas em uma conta, como por exemplo:
# Sacar ou depositar dinheiro, verificar o saldo

# para criarmos uma função, usamos a Tag "CLASS" seguida do nome da função e seus herança (nao vamos falar de herança aqui)
# Apenas para curiosidade, uma erança siginifca que a classe ira ter aspectos de outra classe, dessa forma voce pode separar
# informações em um novo objeto, porem ele faz uso de metodos de outros que foram herdados

# Uma ves que a classe foi criada, precisamos definir quais os paremetros iniciais dela, ou seja, suas variaveis.
# Para essa criação sempre utilizamos uma nova função seguido da tag "__init_", o parametro "SELF" e os paremetros que devem ser passados para a inicialização
# o parametro self inidica que aquela função esta se autoreferenciando, ou seja, acessando as informações contidas naquele objeto criado
# após a inicialização, cada novo metodo deve ser declarado como uma função.

# Vamos continuar com exemplo anterior, vamos criar um menu, e esse menu ira decidir quais metodos de uma classe Usuario
# dentro dessa classe, em breve vamos criar alguns novos metodos para um usuario
#

class MinhaClasse():
    def __init__(self):
        pass
    def metodo_01(self):
        pass
    def metodo_02(self):
        pass


