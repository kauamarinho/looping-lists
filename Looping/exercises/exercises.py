# Exercise 1

ANO_2_DIGITOS = 4

VALOR_TRANSACAO = 1500
TIPO_TRANSACAO = "saque"
CODIGO_CLIENTE = 1234

LIMITE_TRANSACAO = 1000 * ANO_2_DIGITOS

if VALOR_TRANSACAO > LIMITE_TRANSACAO and TIPO_TRANSACAO == "transferência":
    print("Alerta: verificar origem da transferência")

elif TIPO_TRANSACAO == "saque":
    print("Alerta: confirmar com o cliente")

else:
    print("Transação normal")


# Exercise 2

tempo_empresa_anos = 4
nota_avaliacao = 8.5
carga_horaria = 40

if tempo_empresa_anos > 2 and nota_avaliacao >= 8.0:
    print("Elegível para promoção")

else:
    print("Aguardando próxima avaliação")


# Exercise 3

distancia_km = 350
clima = "chuva"
zona_entrega = "rural"

if (distancia_km > 300 and clima == "chuva") or zona_entrega == "rural":
    print("Risco alto de atraso")

else:
    print("Entrega dentro do previsto")


# Exercise 4

CODIGO_SENSOR = "F1"
TEMPERATURA = 25

if CODIGO_SENSOR == "F1" and TEMPERATURA < 40:
    print("Reiniciar máquina")

elif CODIGO_SENSOR == "F2" and TEMPERATURA > 60:
    print("Verificar conexão elétrica e sistema de refrigeração")

elif CODIGO_SENSOR == "F3" and 45 <= TEMPERATURA <= 55:
    print("Ajustar temperatura da esteira")

elif CODIGO_SENSOR == "F4":
    print("Realizar diagnóstico dos sensores ópticos")

else:
    print("Falha não reconhecida pelo sistema de alarme. Acionar o engenheiro responsável")


# Exercise 5

notas_avaliacao = [5, 8, 10, 6, 9, 4]

for nota in notas_avaliacao:
    if nota > 7:
        print(nota)


# Exercise 6

valores_comissao = list(range(0, 51, 5))

print(valores_comissao)


# Exercise 7

tentativas_conexao = [False, False, False, True, True]

tentativas = 0
limite_tentativas = 3

while tentativas < len(tentativas_conexao):
    print("Tentando conectar...")

    sucesso = tentativas_conexao[tentativas]
    tentativas += 1

    if sucesso:
        print("Conexão realizada com sucesso")
        break

    if tentativas >= limite_tentativas:
        print("Conexão interrompida após limite de tentativas")
        break


# Exercise 8

# Cenário A - Pedido urgente

pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = True
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)

else:
    if pedido_a_substituir in pedidos:
        posicao = pedidos.index(pedido_a_substituir)
        pedidos[posicao] = pedido_urgente

    else:
        print("Pedido a substituir não encontrado.")

print("Fila final:", pedidos)


# Cenário B - Não urgente e pedido existente

pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = False
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)

else:
    if pedido_a_substituir in pedidos:
        posicao = pedidos.index(pedido_a_substituir)
        pedidos[posicao] = pedido_urgente

    else:
        print("Pedido a substituir não encontrado.")

print("Fila final:", pedidos)


# Cenário C - Não urgente e pedido inexistente

pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P111"
prioridade_urgente = False
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)

else:
    if pedido_a_substituir in pedidos:
        posicao = pedidos.index(pedido_a_substituir)
        pedidos[posicao] = pedido_urgente

    else:
        print("Pedido a substituir não encontrado. A fila será mantida.")

print("Fila final:", pedidos)