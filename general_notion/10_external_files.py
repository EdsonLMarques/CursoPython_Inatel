'''
o objetivo desde capitulo é mostrar como abrir, processar e salvar dados de arquivos internos.
Esse tipo de arquivo é conhecido como input quando é um arquivo que "entra" no sistema e output quando é uma saida do
sistema.

O primeiro passo da aula é entender qual o tipo de arquivo que queremos trabalhar.

Existem varios tipos de arquivos como txt, csv, xlxs e etc. Cada um deles tem suas vantagens e desvantagens de acordo
com o cenario

Vamos inicialmente focar aqui em trabalhar com arquivos do tipo txt, pois sao mais simples de se lidar o que facilita
o aprendizado

Para trabalhar com arquivos existe a função open com as seguintes opções
    "x" - Create - cria um novo arquivo
    "w" - Write - escreve o arquivo do inicio
    "a" - Append - Continua o arquivo da ultima linha
    "r" - Read - Apenas le o arquivo

a linha da função open ficaria dessa forma:

f = open("n.e", "m") onde, 'f' é o objeto python que recebera o arquivo, 'n' o nome do arquivo, 'e' a extensao do
arquivo e 'm' o metodo de leitura do arquivo

vale ressaltar que o W tambem pode criar um novo arquivo caso o nome selecionado nao exista

para escrever o conteudo em um arquivo usamos a metodo Write e entre parenteses, o que queremos escrever em formato de
string

para ler um arquivo usamos a metodo read. Por padrão o read ira ler o arquivo inteiro

Algo muito importante a se fazer sempre que trabalhamos com arquivos, é fecha-los apos o seu uso. Isso impedira erros

nosso primeiro objetivo é abrir o arquivo e escrever nele algumas informações
'''

# f = open("meu_primeiro_arquivo.txt", "w")
# f.write("Minha primeira frase")
# f.write("Minha segunda frase")
# f.write("Minha terceira frase")
# f.close()

"""
Vamos tetar outros metodos, na pasta files existe um arquivo chamado clubes.txt, vamos utilizar ele para fazer a leitura
nosso objetivo é plotar os clubes listados no arquivo e poder trabalhar com cada nome separadamente
"""
# teste 1
# f = open("files\clubes.txt", "r")
# conteudo = f.read()
# print(conteudo)
# f.close()

"""
Nesse primeiro teste, vemos que ele plotou exatamente as informações que estavam no arquivo, porem, todos os dados estao 
juntos em uma grande string. para provar, vou excluir a quebra de linhas "\ n" do arquivo
"""
# # teste 2
# f = open("files\clubes.txt", "r")
# conteudo = f.read().replace("\n", " - ")
# print(conteudo)
# f.close()

"""
como podemos observar, o resultado foi uma string que contem todos os nomes. para isso podemos fazer o seguinte
Usar a função split() para separar cada uma das linhas e colocar cada nome de clube como sendo um item de uma lista
"""
# teste 3
# f = open("files\clubes.txt", "r")
# conteudo = f.read().split("\n")
# print(conteudo)
# f.close()

"""
Agora que temos um lista de clubes separados, podemos trabalhar com eles individualmente 
"""
# _____________________________________________________________________________________________________________________
"""
agora que ja entendemos como um txt é escrito e lido, vamos trabalhar mais a fundo com a lista de clubes.
Escreva um outro clube que nao esta listado (nao é necessario fazer verificação nenhuma) na lista
Para isso vamos utilizar uma variação dos metodos de leitura
    "r+" - Read and Write - Abre um arquivo existente e incia a escrita do inicio do arquivo
    "w+" - Write and Read - Abre/Cria um arquivo, dados existente sao perdidos.
    
Vamos usar a lista com nome de clubes_pts.txt
Façam uma copia do arquivo por segurança, pois se usar o metodo errado, o arquivo pode ser deletado

Como objetivo desse teste vamos ordenar o clubes de acordo com o numero de pontos e plotar a ordem da competição
"""
#abrindo o arquivo como READ and WRITE
f = open("files\clubes_pts.txt", "r+")
# separando cada linha
lista = f.read().split("\n")
nova_lista = []
# Separando o nome do clube com o nome da
for auxiliar in lista:
    time = auxiliar.split(" - ")
    nova_lista.append(time)
# Ordenando a nova
nova_lista.sort(key= lambda x: x[1], reverse=True)
for index, time in enumerate(nova_lista):
    print("em {}º lugar temos {} com {} pontos".format((index+1),time[0], time[1]))
f.close()

"""
Fizemos uso de um principio muito importante nesse trecho, o LAMBDA, ele nos permite executar funções na propria linha, 
 sem ter que criar funções usando def...
Para explicar melhor, o lambda nesse caso esta pegando o valor da segunda posição de cada item da nova lista
no caso a nova_lista é:
[['Milan', '12'], ['Real Madrid', '11'], ['Liverpool', '09'], ['Boca Juniors', '09'], ['Barcelona', '07'], ['Sao Paulo', '07'], ['PSG', '06']]
a lambda ira pegar o primeiro item
    ['Milan', '12']
    no index 1 (segunda posição)
    '12'
    e usara esse valor para ordenar a nova_lista

"""