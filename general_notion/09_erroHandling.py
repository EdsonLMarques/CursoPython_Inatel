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