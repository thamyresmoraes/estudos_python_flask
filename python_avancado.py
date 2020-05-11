
"""

    PYTHON AVANÇADO

"""


print("###### Compreenção de listas (List Comprenhension) ######")
print()

[x for x in range(5)]

[x ** 2 for x in range(5)]

[x ** 3 for x in range(5)]

[x + 2 for x in range(5)]


#Cria uma lista e apresenta e retorna apenas os números pares. Se reste de n for igual a zero, então é par.
print("Numeros pares: ", [n for n in range(11) if n % 2 == 0])

#Cria uma lista e apresenta e retorna apenas os números ímpares. Se reste de n for igual a um, então é impar.
print("Numeros impares: ", [n for n in range(11) if n % 2 == 1])

#Escrever todos os nomes na mesma formatação usando a Compreensão de lista:
pessoas = [' Ana ', 'manuela', 'FELIPe ', 'PedrO ']
print("Pessoas com diferentes formatações: ", pessoas)

pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas]
print("Pessoas normalizadas", pessoas_normalizadas)
print()



print("###### Dicionários ######")
print()

print("set são valores desordenados assim como o dicionários. Porém, o set não suporta index!")
print("O dicionários também não percorre os valores através do index como uma lista, porém tem um chave e um valor nesta chave.")


meu_dicionario = {'nome': 'Juliana', 'idade': 80}

#acessando o valor
print(meu_dicionario['nome'])
print(meu_dicionario['idade'])

#Uma lista de pessoas:
minha_lista_dict = [{'nome': 'Juliana', 'idade': 80}, {'nome': 'Augusto', 'idade': 70}, {'nome': 'Lucia', 'idade': 22}]

#Acessando um elemento da lista de pessoas:
print(minha_lista_dict[2])

#buscando o nome do indice 1
print(minha_lista_dict[1]['nome'])

#a idade do indice 0
print(minha_lista_dict[0]['idade'])

#Loteria: Como o número tem que ser imutavel, devo colocar dentro de uma tupla.
loteria = {"nome": 'Pedro', 'numeros': (13,4, 53,10)}

#ver quais são os numeros da loteria do Pedro
print(loteria['numeros'])

#somar numeros da Loteria
print(sum(loteria['numeros']))

#dicionario combinado com lista
universidades = [
    {
    'nome': 'Universidade Federal do Sul da Bahia',
    'sigla': 'UFSB'
    },
    {
        'nome': 'Universisdade de São Paulo',
        'sigla': 'USP'
    },

]

print("Podemos adicionar dados aos dicionários mas eles não são objetos. Objetos geralmente pertecem a uma classe e o objeto pode ter funções imbutidas nele para fazer operações, coisa que um dicionario não seria capaz de fazer!")


print()
print("###### Objetos e Classes ######")
print()

print("Uma classe é um modelo ou uma representação de um objeto.")
print("Um objeto é uma instância de uma classe.")

class JogadorLoteria:
    #metodo init é um método padrão do python para instanciar um objeto quando a gente for chamar a classe criando um objeto.
    #O self significa "ele mesmo"
    def __init__(self):
        self.nome = "Pedro"
        self.numeros = (13,4, 53,10)

    def total(self):
        return sum(self.numeros)


#instanciando a classe
jogador_1 = JogadorLoteria()
jogador_2 = JogadorLoteria()

#Para acessar os atributos da classe
jogador_1.nome
jogador_2.numeros

#para acessar uma função
jogador_1.total()

#passando o argumento

class JogadorLoteria:
    #metodo init é um método padrão do python para instanciar um objeto quando a gente for chamar a classe criando um objeto.
    #O self significa "ele mesmo"
    def __init__(self, nome):
        self.nome = nome
        self.numeros = (13,4, 53,10)

    def total(self):
        return sum(self.numeros)

#instanciando a classe pasando o argumento
jogador_1 = JogadorLoteria('Maria')
jogador_2 = JogadorLoteria('João')


print(jogador_1.nome)
print(jogador_2.nome)

print()
print("###### Heranças ######")
print()



print()
print("###### Métodos de Classes e Métodos Estáticos ######")
print()


print()
print("###### **args e **kwargs ######")
print()



print()
print("###### Decoradores ######")
print()
