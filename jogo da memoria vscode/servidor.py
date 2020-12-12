import socket

tabela=[
['\033[31;41m r \033[m','\033[32;42m v \033[m','\033[37;47m b \033[m','\033[34;44m a \033[m'],
['\033[34;44m a \033[m','\033[33;43m l \033[m','\033[31;41m r \033[m','\033[30;40m p \033[m'],
['\033[32;42m v \033[m','\033[37;47m b \033[m','\033[30;40m p \033[m','\033[33;43m l \033[m']
]

jogo=[['0,0','0,1','0,2','0,3'],['1,0','1,1','1,2','1,3'],['2,0','2,1','2,2','2,3']]

p='inicializar'
tentativa=[]
numero_tentativas=0

def exibir_jogo():
  exibição_jogo = ''
  for linha in range(3):
        for coluna in range(4):
          exibição_jogo+=jogo[linha][coluna]+' '

        exibição_jogo+='\n\n'
  return exibição_jogo
  

def jogada(jogada):
    jogo[int(jogada[0])][int(jogada[2])]=tabela[int(jogada[0])][int(jogada[2])]
    tentativa.append(jogada)
    tentativa.append(tabela[int(jogada[0])][int(jogada[2])][9])
    if len(tentativa)==4:
        if tentativa[1]==tentativa[3]:
            tentativa.clear()
            x=exibir_jogo()
        else:
            x=exibir_jogo()
            jogo[int(tentativa[0][0])][int(tentativa[0][2])]=tentativa[0]
            jogo[int(tentativa[2][0])][int(tentativa[2][2])]=tentativa[2]
            tentativa.clear()
        return x
    
    return ''

def fim_jogo(partida,chutes):
  if partida==tabela:
    return 'Você Venceu'
  elif chutes==20:
    return 'Você Perdeu'
  return ' '

HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Servidor no ar ..')
#ESPERANDO CONEXÃO DO CLIENTE
while True:
    msg, cliente = udp.recvfrom(1024)
    if msg.decode()=='conectar':
        break
print('Concetado por', cliente)
numero_tentativas=0
#INICIANDO JOGO
while True:
    #
    msg=exibir_jogo()
    msg=msg.encode()
    udp.sendto(msg,cliente)
    #RECEBENDO JOGADA
    msg,cliente=udp.recvfrom(1024)
    numero_tentativas+=1
    jogada_cliente=msg.decode()
    msg=jogada(jogada_cliente)
    msg=msg.encode()
    #ENVIANDO RESULTADO DA JOGADA
    udp.sendto(msg,cliente)
    #TESTANDO CONDIÇÕES PARA FINALIZAR JOGO
    msg=fim_jogo(jogo,numero_tentativas)
    msg=msg.encode()
    udp.sendto(msg,cliente)
    if msg.decode()=='Você Venceu' or msg.decode()=='Você Perdeu':
        msg=exibir_jogo()
        msg=msg.encode()
        udp.sendto(msg,cliente)
        break