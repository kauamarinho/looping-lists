"""
ESTRUTURAS DE REPETIÇÃO

Estruturas de repetição são utilizadas quando queremos executar
um conjunto de operações várias vezes.

Python possui duas estruturas principais:

- for
- while

FOR:
Normalmente utilizado para percorrer elementos ou quando temos
uma quantidade definida de repetições.

WHILE:
Executa um bloco de código enquanto determinada condição
for verdadeira.
"""


# 1. FUNÇÃO RANGE()

"""
RANGE()

A função range() gera uma sequência de números.

Sintaxes:

range(fim)
range(inicio, fim)
range(inicio, fim, passo)

O último número não é incluído.
"""

print(list(range(5)))
print(list(range(5, 10)))
print(list(range(0, 10, 2)))



# 2. FOR COM RANGE()

"""
FOR COM RANGE()

O for pode utilizar range() para executar uma ação
uma determinada quantidade de vezes.

Neste exemplo:
- começa em 1;
- termina antes de 10;
- avança de 2 em 2.
"""

for numero in range(1, 10, 2):
    print(numero)


# 3. FOR PERCORRENDO UMA LISTA


"""
FOR COM LISTAS

O for também pode percorrer diretamente os elementos
armazenados dentro de uma lista.
"""

numeros = [1, 3, 5, 7, 9]

for numero in numeros:
    print(numero)


# 4. FOR COM DICIONÁRIOS

"""
FOR COM DICIONÁRIOS

Quando percorremos diretamente um dicionário com for,
recebemos suas chaves.

Depois podemos utilizar cada chave para acessar
seu respectivo valor.
"""

outro_dicionario = {
    'um': 1,
    'dois': 2,
    'tres': 3
}

for chave in outro_dicionario:
    print('Chave:', chave)
    print('Valor:', outro_dicionario[chave])


# 5. VERIFICANDO NÚMEROS PARES E ÍMPARES

"""
OPERADOR %

O operador % retorna o resto de uma divisão.

Se:

numero % 2 == 0

o número é par.

Caso contrário, ele é ímpar.
"""

for numero in range(0, 10):

    if numero % 2 == 0:
        print(numero, 'é par!')
    else:
        print(numero, 'é ímpar!')



# 6. UTILIZANDO "_" NO FOR

"""
UTILIZANDO "_"

Utilizamos "_" quando precisamos repetir uma ação,
mas não precisamos utilizar o valor atual da repetição.

Neste exemplo, queremos apenas executar o print
uma vez para cada carro.
"""

carros = ['Fiat', 'Renault', 'Honda']

for _ in carros:
    print('Este é um teste')


# 7. ENUMERATE()

"""
ENUMERATE()

enumerate() permite acessar ao mesmo tempo:

- o índice;
- o valor.

É muito útil quando precisamos saber a posição
de um elemento dentro de uma lista.
"""

carros = ['Fiat', 'Renault', 'Honda']

for indice, carro in enumerate(carros):
    print('Posição:', indice, '- Carro:', carro)



# 8. WHILE BÁSICO

"""
WHILE

O while executa um bloco de código enquanto
determinada condição for verdadeira.

É importante modificar a variável utilizada na condição.

Caso contrário, podemos criar um loop infinito.
"""

i = 1

while i <= 10:
    print(i)
    i += 1



# 9. OPERADOR +=

"""
OPERADOR +=

Podemos escrever:

i = i + 1

de uma forma mais curta:

i += 1

As duas formas aumentam o valor de i em 1.
"""

i = 1

while i <= 5:
    print(i)
    i += 1


# 10. BREAK

"""
BREAK

break encerra imediatamente uma estrutura de repetição.

Mesmo que a condição do while ainda seja verdadeira,
o loop será encerrado.
"""

i = 0

while i < 10:

    print(i)

    if i == 5:
        break

    i += 1

print('Saiu do while')


# 11. CONTINUE


"""
CONTINUE

continue pula a repetição atual e retorna
para o começo do loop.

Neste exemplo, o número 3 não será mostrado.
"""

i = 0

while i < 10:

    if i == 3:
        i += 1
        continue

    print(i)

    i += 1



# 12. BREAK + CONTINUE

"""
BREAK E CONTINUE

Neste exemplo:

- continue ignora o número 3;
- break encerra o loop quando chegamos ao número 5.
"""

i = 0

while i < 10:

    if i == 3:
        i += 1
        continue

    print(i)

    if i == 5:
        break

    i += 1


# 13. EXEMPLO PRÁTICO - SOMANDO NÚMEROS

"""
ACUMULADOR

Uma variável pode armazenar resultados durante
as repetições.

Neste exemplo, "soma" acumula os números de 1 até 5.
"""

soma = 0

for numero in range(1, 6):
    soma += numero

print('Soma:', soma)


# 14. EXEMPLO PRÁTICO - PROCURANDO EM UMA LISTA

"""
PROCURANDO UM ELEMENTO

Podemos combinar:

- lista;
- for;
- if;
- break.

Quando encontramos o carro desejado,
utilizamos break porque não precisamos
continuar procurando.
"""

carros = ['Fiat', 'Renault', 'Honda', 'Toyota']

for carro in carros:

    print('Verificando:', carro)

    if carro == 'Honda':
        print('Honda encontrado!')
        break


# 15. EXEMPLO PRÁTICO - INPUT + WHILE

"""
INPUT COM WHILE

O while é muito útil quando não sabemos exatamente
quantas vezes o usuário realizará uma ação.

Neste exemplo, o programa continuará recebendo carros
até que o usuário digite "sair".
"""

carros_cadastrados = []

while True:

    marca = input('Digite uma marca ou "sair": ')

    if marca.lower() == 'sair':
        break

    carros_cadastrados.append(marca)

print('Carros cadastrados:')

for carro in carros_cadastrados:
    print(carro)