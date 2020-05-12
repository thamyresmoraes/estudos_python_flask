import datetime
import functools
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

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}

#criando funcionario
fabio = Funcionario('Fábio', 7000)

#buscando dados do funcionario criado
fabio.dados()

"""
vamos criar um administrador e ele vai ter total as funções de um funcionário e algo a mais.
Então vamos criar a classe admin que vai Herdar a classe Funcionario

"""

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario) #super referencia a classe funcionario, chamando a classe super e a função dela init passando o nome e o salário

    def atualizar_dados(self, nome):
        self.nome == nome
        return self.dados()

#Criando admin
gustavo = Admin('Gustavo', 13000)
fabio.dados()
gustavo.dados()

#Gustavo tem função adm
gustavo.atualizar_dados('Gusta')
gustavo.dados() #dados atualizados


print()
print("###### Métodos de Classes e Métodos Estáticos ######")
print()

class Funcionario():
    aumento = 1.04

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return{'nome': self.nome, 'salario': self.salario}

    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento
        return self.salario

    @classmethod
    def definir_novo_aumento(cls):
        cls.aumento = novo_aumento

    @staticmethod
    def dia_util(dia):
        #segunda-feira = 0
        #domingo = 6
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True


luisa = Funcionario('Luisa', 14000)
print(luisa.dados())
print(luisa.aplicar_aumento())


"""
    @classmethod -> É uma função que afeta a classe com um todo e recebe cls automaticamente

    @staticmethod -> Não exige nenhum argumento da classe Funcionario
"""

my_date = datetime.date(2020, 5, 22)
Funcionario.dia_util(my_date)



print()
print("###### **args e **kwargs ######")
print()

"""
args -> são argumentos
kwargs -> Keyord arguments (argumentos de palavras chaves)

"""

def meu_metodo(arg1, arg2):
    return arg1 + arg2

meu_metodo(5, 6)

#mas se eu quiser somais mais números?
#Use args enviei quantos argumentos vc quiser

def soma_simplificada(*args):
    return sum(args)

soma_simplificada(4, 5, 9, 1101, 14548, 48, 145)

#kwargs tem uma palavra chave como argumento,
def  metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

metodo_kwargs(3, 'sasa', 123, 'alguma coisa', nome = 'Pedro', idade=58)

#sempre coloque args antes de kwargs

print()
print("###### Decoradores ######")
print()

"""
    os decoradores utilizam a biblioteca functools, e altera o funcionamento da função que está embaixo 

    wraps -> Embrulhe a minha função
"""

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def func_que_roda_funcao():
        print("******Embrulhando função no decorador *********")
        funcao()
        print("**********Fechando embrulho*******")
    return func_que_roda_funcao

@meu_decorador
def minha_funcao():
    print("Eu sou uma função!")


minha_funcao()
