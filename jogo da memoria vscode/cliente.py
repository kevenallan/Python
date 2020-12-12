import socket
import os
from time import sleep

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Para sair use CTRL+X\n')
conectar='conectar'
#CONECTANDO COM SERVIDOR
udp.sendto(conectar.encode(),dest)

#INICIANDO JOGO
while True:
    msg,servidor=udp.recvfrom(1024)
    msg=msg.decode()
    print(msg)
    #LENDO JOGADA
    jogada=str(input('Informe sua jogada: '))
    if jogada == '\x18':
        break
    #ENVIANDO JOGADA
    msg=jogada.encode()
    udp.sendto(msg,servidor)
    #RECEBENDO RESULTADO DA JOGADA
    msg,servidor=udp.recvfrom(1024)
    msg=msg.decode()
    if msg!='':
        print(msg)
        sleep(1)
        os.system("cls")
    #RECEBENDO RESPOSTA SOBRE FINALIZAÇÃO DO JOGO
    msg,servidor=udp.recvfrom(1024)
    fim=msg.decode()
    if fim=='Você Venceu' or fim=='Você Perdeu':
        msg,servidor=udp.recvfrom(1024)
        msg=msg.decode()
        print(msg)
        print(fim)
        break