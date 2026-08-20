"""
DICIONÁRIOS

Dicionários são estruturas mutáveis, ou seja, podem ser
alterados depois de sua criação.

Eles armazenam informações utilizando pares:

chave: valor

Exemplo:

{
    'nome': 'João',
    'idade': 20
}

As chaves são utilizadas para localizar seus respectivos valores.

Dicionários são identificados por chaves {}.
"""


"""
CRIANDO DICIONÁRIOS VAZIOS

Existem duas formas comuns de criar um dicionário vazio:

{}
dict()
"""

dicionario = {}
outro_dicionario = dict()

print(dicionario)
print(outro_dicionario)


"""
CRIANDO UM DICIONÁRIO COM DADOS

Cada informação de um dicionário é formada
por uma chave associada a um valor.
"""

numeros = {
    'um': 1,
    'dois': 2,
    'tres': 3
}

print(numeros)


"""
ACESSANDO VALORES

Podemos acessar um valor informando sua chave
entre colchetes.

Exemplo:

dicionario['nome']
"""

dicionario = {
    'nome': 'João',
    'endereco': 'Rua das Couves, 123'
}

print(dicionario['nome'])
print(dicionario['endereco'])


"""
KEYS()

O método keys() retorna todas as chaves
existentes dentro do dicionário.
"""

print(dicionario.keys())


"""
VALUES()

O método values() retorna todos os valores
armazenados dentro do dicionário.
"""

print(dicionario.values())


"""
ITEMS()

O método items() retorna os pares de
chave e valor do dicionário.

É muito utilizado junto com estruturas de repetição.
"""

print(dicionario.items())


"""
ADICIONANDO UMA NOVA CHAVE

Podemos adicionar uma nova informação ao dicionário
simplesmente criando uma nova chave e atribuindo
um valor a ela.
"""

dicionario['estado'] = 'RJ'

print(dicionario)


"""
ALTERANDO UM VALOR

Como dicionários são mutáveis, podemos alterar
o valor associado a uma chave existente.

Basta acessar a chave e atribuir um novo valor.
"""

dicionario['estado'] = 'ES'

print(dicionario)


"""
VERIFICANDO SE UMA CHAVE EXISTE

O operador "in" pode ser utilizado para verificar
se determinada chave existe dentro do dicionário.

O resultado será True ou False.
"""

print('nome' in dicionario)
print('idade' in dicionario)

if 'nome' in dicionario:
    print('A chave nome existe!')
else:
    print('A chave nome não existe!')


"""
PROCURANDO UM VALOR

Por padrão, o operador "in" procura pelas chaves.

Para procurar entre os valores, podemos utilizar:

valor in dicionario.values()
"""

print('João' in dicionario.values())

if 'João' in dicionario.values():
    print('João foi encontrado!')
else:
    print('João não foi encontrado!')


"""
GET()

O método get() permite buscar um valor através
de sua chave.

Exemplo:

dicionario.get('nome')

Uma vantagem do get() é que podemos definir
um valor padrão caso a chave não exista.
"""

nome = dicionario.get('nome')

print(nome)

idade = dicionario.get('idade', 'Idade não cadastrada')

print(idade)


"""
ACESSO DIRETO X GET()

Ao utilizar:

dicionario['idade']

Python gera um erro caso a chave não exista.

Com:

dicionario.get('idade')

podemos realizar a busca sem gerar esse erro.
"""

print(dicionario.get('nome'))

print(dicionario.get('telefone', 'Telefone não encontrado'))


"""
PERCORRENDO UM DICIONÁRIO

Podemos utilizar for para percorrer
as chaves existentes em um dicionário.
"""

for chave in dicionario:
    print(chave)


"""
PERCORRENDO CHAVES E VALORES

Podemos utilizar items() junto com for.

Dessa maneira conseguimos acessar a chave
e o valor ao mesmo tempo.
"""

for chave, valor in dicionario.items():
    print('Chave:', chave)
    print('Valor:', valor)


"""
UPDATE()

O método update() permite adicionar ou atualizar
várias informações de uma vez.

Se uma chave já existir, seu valor será atualizado.

Se não existir, uma nova chave será criada.
"""

dicionario.update({
    'idade': 25,
    'cidade': 'Vitória'
})

print(dicionario)


"""
POP()

O método pop() remove uma chave do dicionário.

Além de remover a chave, ele retorna o valor
que estava armazenado nela.
"""

cidade_removida = dicionario.pop('cidade')

print('Cidade removida:', cidade_removida)

print(dicionario)


"""
DEL

Também podemos utilizar del para remover
uma chave de um dicionário.
"""

dicionario['telefone'] = '99999-9999'

print(dicionario)

del dicionario['telefone']

print(dicionario)


"""
LEN()

A função len() informa quantos pares
chave-valor existem dentro do dicionário.
"""

quantidade = len(dicionario)

print('Quantidade de informações:', quantidade)


"""
DICIONÁRIOS PODEM ARMAZENAR DIFERENTES TIPOS

Os valores de um dicionário podem possuir
diferentes tipos de dados.

Por exemplo:

string
int
float
bool
lista
outro dicionário
"""

pessoa = {
    'nome': 'João',
    'idade': 25,
    'altura': 1.75,
    'estudante': True
}

print(pessoa)


"""
DICIONÁRIO COM LISTA

Uma lista também pode ser armazenada como
valor dentro de um dicionário.

Neste exemplo, a chave "carros" possui
uma lista como valor.
"""

cliente = {
    'nome': 'João',
    'idade': 25,
    'carros': ['Honda', 'Toyota', 'Fiat']
}

print(cliente)

print(cliente['nome'])

print(cliente['carros'])

print(cliente['carros'][0])


"""
ALTERANDO UMA LISTA DENTRO DO DICIONÁRIO

Como a chave "carros" contém uma lista,
podemos utilizar os métodos de listas normalmente.

Por exemplo, append() pode adicionar
um novo carro.
"""

cliente['carros'].append('Volkswagen')

print(cliente['carros'])


"""
DICIONÁRIO DENTRO DE DICIONÁRIO

Um dicionário também pode armazenar
outro dicionário.

Isso permite representar informações
mais complexas.
"""

cliente = {
    'nome': 'João',
    'endereco': {
        'cidade': 'Rio de Janeiro',
        'estado': 'RJ'
    }
}

print(cliente)

print(cliente['endereco'])

print(cliente['endereco']['cidade'])

print(cliente['endereco']['estado'])


"""
EXEMPLO PRÁTICO - CADASTRO

Podemos utilizar um dicionário para representar
uma entidade do nosso programa.

Neste exemplo, cada chave representa uma
informação de uma pessoa.
"""

pessoa = {}

pessoa['nome'] = input('Digite seu nome: ')

pessoa['idade'] = int(
    input('Digite sua idade: ')
)

pessoa['cidade'] = input('Digite sua cidade: ')

print('\nDados cadastrados:')

for chave, valor in pessoa.items():
    print(chave, ':', valor)


"""
EXEMPLO PRÁTICO - CONTA BANCÁRIA

Um dicionário também pode representar
informações de uma conta bancária.

Cada chave representa uma característica
da conta.
"""

conta = {
    'id': 112,
    'titular': 'Gustavo',
    'saldo': 3000.00,
    'bloqueada': False
}

print(conta)

print('Número da conta:', conta['id'])
print('Titular:', conta['titular'])
print('Saldo:', conta['saldo'])
print('Bloqueada:', conta['bloqueada'])


"""
ALTERANDO O SALDO

Como o dicionário é mutável, podemos acessar
diretamente o saldo e alterar seu valor.

Neste exemplo será realizado um depósito.
"""

deposito = 500

conta['saldo'] += deposito

print('Depósito:', deposito)
print('Novo saldo:', conta['saldo'])


"""
VERIFICANDO UMA CONDIÇÃO

Podemos combinar dicionários com estruturas
condicionais como if e else.

Aqui verificamos se a conta está bloqueada.
"""

if conta['bloqueada']:
    print('A conta está bloqueada.')
else:
    print('A conta está disponível para operações.')


"""
RESUMO DOS PRINCIPAIS RECURSOS

{}                  -> cria um dicionário

dict()              -> cria um dicionário

dicionario[chave]   -> acessa um valor

keys()              -> retorna as chaves

values()            -> retorna os valores

items()             -> retorna chaves e valores

get()               -> busca um valor com segurança

update()            -> adiciona ou atualiza dados

pop()               -> remove uma chave e retorna seu valor

del                 -> remove uma chave

len()               -> quantidade de pares chave-valor

in                  -> verifica se uma chave existe
"""