import socket
from random import randint
#PARTE DE UDP/HOST
HOST = ''  # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor está
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

def gerar_numero_aleatorio():
    numero=randint(0,10)
    return str(numero)

def verificar_vitoria(numero_sorteado,chute_do_cliente):
    if numero_sorteado==chute_do_cliente:
        return 'Voce Acertou!'
    return f'Você Errou!'

def verificar_quantidade_chutes(numero_de_chutes_cliente):
    numero_maximo_chutes=5
    if numero_de_chutes_cliente==numero_maximo_chutes:
        return 'Você antingiu o número maixmo de chutes..'
    return f'Você ainda tem: {numero_maximo_chutes-numero_de_chutes_cliente} chutes.'

def dica(numero_sorteado,chute_do_cliente):
    if int(numero_sorteado)>int(chute_do_cliente):
        dica='Maior'
    else:
        dica='Menor'
    return f'Chute um numero {dica}'


sorteado=gerar_numero_aleatorio()
chutes_cliente=0

#AGUARDANDO CONEXÃO
print('Aguardando jogador...')
msg,cliente=udp.recvfrom(1024)
#DEVOLVENDO A MENSAGEM DE CONEXÃO AO CLIENTE
udp.sendto(msg,cliente)
print("Conexão estabelecida com: ",cliente)

print(f'Numero sorteado = {sorteado}')
#INICIANDO O JOGO
while True:
    #RECEBENDO CHUTE DO CLIENTE
    msg,cliente=udp.recvfrom(1024)
    guardando_chute_cliente=msg.decode()
    chutes_cliente+=1
    print(f'{cliente} jogou: {msg.decode()}')
    #VERIFICANDO SE O CLIENTE VENCEU
    verificação=verificar_vitoria(sorteado,msg.decode())
    if verificação!='Voce Acertou!':
        udp.sendto(verificação.encode(),cliente)
    else:
        udp.sendto(verificação.encode(),cliente)
        break
    #VERFICANDO SE ATINGIU O NUMERO MAXIMO DE CHUTES
    chutes=verificar_quantidade_chutes(chutes_cliente)
    if chutes!='Você antingiu o número maixmo de chutes..':
        udp.sendto(chutes.encode(),cliente)
    else:
        udp.sendto(chutes.encode(),cliente)
        break
    #ENVIANDO DICA PARA OS PROXIMOS CHUTES
    dica_para_cliente=dica(sorteado,guardando_chute_cliente)
    udp.sendto(dica_para_cliente.encode(),cliente)
udp.close()

