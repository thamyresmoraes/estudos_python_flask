

"""

    PYTHON INICIANTE

"""

#variáveis
print('Declaração de variáveis: ')
a = 2
b = 4
print('a = ', a)
print('b = ', b)
print('')

#printar variavel
print('printar as variáveis: ')
print("O valor de 'a' é: ", a)
print("O valor de 'b' é: ", b)
print('')

#soma e print do resultado
print('Soma das variaveis declaradas')
print("O resultado da soma é: ", a+b)
print('')

#subscrever variável
print('Subscrevendo a variável a para 5:')
a = 5
print("a = 5")
print("O valor de A agora é:", a)
print('')

#Criando string
print('Criando string:')
print("c = '3'")
c = "3 é uma string"
print("Printando string:", c)
print()

#Pontos de atenção
print('###### Pontos de atenção: ######')
print('')
print('- não é possivel somar string com numero')
print('- É possivel somar string com string')
print('')

#destacar uma letra dentro de uma string
print("Destacar uma letra dentro de uma string: ")
print("A letra 'b' está entre aspas simples")

#o contra barra anula o próximo caracter
print("A letra \"b\" esta entre aspas com contra barra")
print()


#por convenção escreva variaveis "grandes"  com underline (_)
print("Por convenção escreva variaveis 'grandes'  com underline (_)")
print("minha_variavel_grande = 'Dentro da convenção'")
minha_variavel_grande = 'Dentro da convenção'
print()

#tipos de variáveis
print("Tipos de variáveis:")
print("alpha = 10 -> inteiro")
print("bravo = \"uma string\"")
print("charlie = 10.2 -> float")
print("delta = True -> boolean")

alpha = 10 #inteiro
bravo = "uma string"
charlie = 10.2 #float
delta = True #boolean

print()
print()


"""
    OPERADORES ARITMÉTICOS

"""

print("###### OPERADORES ARITMÉTICOS ######")
print("+ Soma")
print("- Subtrai")
print("/ Divide")
print("* Multiplica")
print("% Resto da divisão")
print("3 ** 2 Valor ao quadrado, neste caso 3 ao quadrado")
print("3 ** 3 Valor ao cubo")
print()
print()

"""
    OPERADORES DE COMPARAÇÃO

"""
print()
print()
print("###### OPERADORES DE COMPARAÇÃO ######")
print("b == 2 --> Para comparar se é igual")
print("b != 2 --> Para comparar se é diferente")
print("b > 2 --> Para comparar se é maior")
print("b < 2 --> Para comparar se é menor")
print("b >= 2 --> Para comparar se é maior ou igual")
print("b <= 2 --> Para comparar se é menor ou igual")
print()
print()

"""
    OPERADORES LÓGICOS

"""
print("###### OPERADORES LÓGICOS ######")
A = True
B = False
print()


print("A = True")
print("B = False")
print()

print("------- A E B ---------")
print("Resultado de A and B: ", A and B)
print()
print("Como o B é false, então a condição é falsa. Para que seja verdadeira, as duas variáveis precisam ser verdadeiras")
print()


A = True
B = True
print()


print("A = True")
print("B = True")
print("Resultado de A and B: ", A and B)

print("------- A OU B ---------")

A = True
B = False
print()


print("A = True")
print("B = False")
print("O Resultado A or B:", A or B)

print()
print("Precisamos que apenas um seja verdadeiro para a condição retornar True")
print()


print("------- NOT A ---------")

A = True
B = False
print()


print("A = True")
print("B = False")
print("Resultado not A: ", not A)

print()
print("Retorna o resultado inverso!")
print()

print("------- NOT B ---------")

A = True
B = False
print()


print("A = True")
print("B = False")
print("Resultado not B: ", not B)

print()
print("Retorna o resultado inverso!")
print()
print()

"""
    MÉTODOS EM PYTHON

"""
print("###### MÉTODOS EM PYTHON ######")

metodo = """
            def meu_metodo():
                print("Olá")

        Chamando o método:
            meu_metodo()
        """

print(metodo)

def meu_metodo():
    print("Olá")

#chamando o método
meu_metodo()



#soma de dois valores

def soma_dois_valores(valor1, valor2):
    return valor1 + valor2

#chamando o método passando os valores
soma_dois_valores(5, 8)
print()
print()


"""
    MÉTODOS EM PYTHON - Built in - imbutidas

"""

print("###### MÉTODOS EM PYTHON - Built in - imbutidas ######")
print()

print("print() é um método")
print()

print("Para transformar um número em um inteiro 'int(10.3)': ")
int(10.3) # Para transformar um número em um inteiro
print(int(10.3))
print()

print("Para transformar um número em um float 'float(10)': ")
float(10) # Para transformar um número em um float
print(float(10))
print()

print("Retorna quantas letras tem (o espaço da string também contam)")
len("Olá") #Retorna quantas letras tem (o espaço da string também contam)
print(len("Olá"))
print()

print("abs que seria o módulo em português, ou seja, o valor absoluto: ")
x = -10
print("x = -10")
print("abs(x)")
print("resultado: ", abs(x)) # Que seria o módulo, o valor absoluto
print()


print("lista = [1, 2, 3, 4, 5, 6]")
lista = [1, 2, 3, 4, 5, 6]
print()

print("sum(lista), soma os valores, neste caso o da listas: ")
print(sum(lista)) #Soma os valores, neste caso o da Listas
print()

print("min(lista),retorna o menor valor da lista: ")
print(min(lista)) #Retorna o menor valor da lista
print()

print("max(lista), retorna o maior valor da lista: ")
print(max(lista)) #Retorna o maior valor da lista
print()

print("round(10.9876), arredonda os valores: ")
print(round(10.9876)) #Arredonda os valores
print()

print("round(10.9876), arredonda os valores determinando quantas casas decimais: ")
print(round(10.98763, 2)) #Arredonda os valores
print()
print()

"""
    LISTAS TUPLAS E SETS

"""

print("###### LISTAS TUPLAS E SETS ######")
print()

print("###### LISTAS ######")
print()
print("notas = [3, 5, 8, 9, 10]")
notas = [3, 5, 8, 9, 10]

print()
print("--- Acrescentar mais uma nota na lista usando append. 'notas.append(2)' ---")
notas.append(2)
print(notas)

print()
print("--- Para tirar a média das notas usando len e sum. 'sum(notas)/len(notas)' ---")
print(sum(notas)/len(notas))

print()
print("--- Consultar um item da lista com index ---")
print(notas[0])

print()
print("--- Consultar o último item da lista ---")
print(notas[len(notas)-1])
print()


print("###### Tuplas ######")
print()

print("O valor da tupla não pode ser modificado!!! Uma tupla é feita para ser única e não modificada")
print()
tupla = (2,5,6)
print(tupla)

print("Podemos adicionar um valor a tupla, porém é criada uma nova. 'tupla += (4,)'")
tupla += (4,)
print(tupla)

print()
print("###### Sets ######")
print()

print("set_notas = {9, 8, 8, 7, 1}")
print("São colocados entre {} e um set não pode ter valores repetidos")
set_notas = {9, 8, 8, 7, 1}

print()
print("Se o colocarmos valores repetidos eles não serão impressos: ")
print("set_notas = {9, 8, 8, 7, 1, 9, 9, 2}")
set_notas = {9, 8, 8, 7, 1, 9, 9, 2}
print("Resultado", set_notas)
print()

print("Como na lista, o set também pode adicionar valores, que com o add")
print("set_notas.add(7)")
set_notas.add(8.2)
print(set_notas)
print()

print("Set não tem ordem como uma lista, por isso não é possivel consultar como, por exemplo, 'set_notas[0]'")


"""
    IF e ELSE (Se e Senão)

"""

print("If e else")

devo_continuar = True

if devo_continuar:
    print("Continue!")

pessoas_conhecidas = ['João', 'Maria', 'Ana', 'Fábio']

pessoa = input("Entre como nome de uma pessoa:")

if pessoa in pessoas_conhecidas:
    print("Você conhece {}!".format (pessoa))
else:
     print("Você NÃO conhece {}!".format (pessoa))


print()

"""
    LOOPS EM PYTHON (Se e Senão)

"""

minha_variavel = "Ola mundo!"

len(minha_variavel)

minha_variavel[0]
minha_variavel[1]
minha_variavel[2]


print("usando o for: ")

for letra in minha_variavel:
    print(letra)

print("RANGE")
print(list(range(10))) # gera um range de 0 á 9

print(list(range(1, 11))) # gera um range de 1 á 9


numeros_pares = list(range(0, 11, 2))
print(numeros_pares)

print()
print("multiplicar número ao quadrado:")
for numero in numeros_pares:
    print(numero ** 3)

print()
print("usando o while: ")

x = 0

while x <= 10:
    print(x ** 3)
    x += 2 #incrementação para o loop parar de executar


usuario_quiser = True

while usuario_quiser == True:
    usuario_input = input("Quer continuar? (S/N) ")
    if usuario_input == 'N':
        usuario_quiser = False
