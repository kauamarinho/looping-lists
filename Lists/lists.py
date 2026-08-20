"""
LISTAS

Listas são estruturas mutáveis, ou seja, podem ser alteradas
depois de sua criação.

São estruturas muito utilizadas em Python e podem armazenar
diferentes tipos de dados.

As listas são identificadas por colchetes [].
"""

# Criando listas vazias

lista1 = []
lista2 = list()

print(lista1)
print(lista2)


"""
ORDENAÇÃO DE LISTAS

O método sort() organiza os elementos da lista.

A alteração acontece "in-place", ou seja, a própria lista
original é modificada.
"""

lista_para_ordenar = [32, 23, 56, 16, 87, 45, 90]

lista_para_ordenar.sort()

print(lista_para_ordenar)


"""
FATIAMENTO DE LISTAS

Podemos selecionar apenas uma parte da lista utilizando:

lista[início:fim]

O índice final não é incluído no resultado.
"""

print(lista_para_ordenar)
print(lista_para_ordenar[3:5])


"""
ADICIONANDO ELEMENTOS

O método append() adiciona um novo elemento
ao final da lista.
"""

carros = ['Nissan', 'Ford', 'Volkswagen', 'Fiat']

carros.append('GM')

print(carros)


"""
ALTERANDO ELEMENTOS

Como listas são mutáveis, podemos alterar um elemento
acessando diretamente sua posição.
"""

carros[1] = 'Toyota'

print(carros)


"""
TAMANHO DA LISTA

A função len() retorna a quantidade de elementos
existentes em uma lista.
"""

quantidade = len(carros)

print('Quantidade de carros:', quantidade)


"""
VERIFICANDO ELEMENTOS

O operador "in" verifica se determinado elemento
está presente em uma lista.
"""

if 'Toyota' in carros:
    print('Toyota está na lista!')
else:
    print('Toyota não está na lista!')


"""
LOCALIZANDO UM ELEMENTO

O método index() retorna a posição de determinado
elemento dentro da lista.
"""

posicao = carros.index('Volkswagen')

print('Volkswagen está na posição:', posicao)


"""
REMOVENDO ELEMENTOS COM POP()

O método pop() remove um elemento utilizando seu índice.

O elemento removido também pode ser armazenado
em uma variável.
"""

carros = ['Nissan', 'Ford', 'Volkswagen', 'Fiat']

print(carros)

removido = carros.pop(1)

print(carros)
print('Marca removida:', removido)


"""
REMOVENDO O ÚLTIMO ELEMENTO

Quando usamos pop() sem informar um índice,
o último elemento da lista é removido.
"""

removido = carros.pop()

print(carros)
print('Marca removida:', removido)


"""
REMOVENDO PELO VALOR

O método remove() procura um valor específico
e remove esse valor da lista.

Diferente de pop(), não precisamos informar
a posição do elemento.
"""

carros = ['Nissan', 'Ford', 'Volkswagen', 'Fiat']

carros.remove('Ford')

print(carros)


"""
ITERAÇÃO SIMPLES

O for permite percorrer cada elemento de uma lista.

A variável "carro" recebe um elemento da lista
a cada repetição.
"""

for carro in carros:
    print(carro)


"""
ITERAÇÃO COM ENUMERATE()

A função enumerate() permite acessar ao mesmo tempo
o índice e o valor de cada elemento.
"""

for idx, carro in enumerate(carros):
    print('A marca na posição', idx, 'é', carro)


"""
ITERAÇÃO SEM UTILIZAR O VALOR

O caractere "_" é utilizado quando precisamos repetir
uma ação, mas não precisamos utilizar o valor
do elemento durante a repetição.
"""

for _ in carros:
    print('Não sei dirigir!')


"""
CRIANDO UMA LISTA COM INPUT

Podemos utilizar input() para receber informações
do usuário e adicioná-las a uma lista.

Neste exemplo serão cadastradas três marcas de carros.
"""

carros_cadastrados = []

for _ in range(3):
    marca = input('Digite uma marca de carro: ')
    carros_cadastrados.append(marca)

print('Marcas cadastradas:')

for carro in carros_cadastrados:
    print(carro)