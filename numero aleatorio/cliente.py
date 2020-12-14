import socket
HOST = 'LocalHost'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está

# abre um socket UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

#ENVIANDO MENSAGEM DE CONEXÃO
msg='conectar'
udp.sendto(msg.encode(), dest)
#RECEBENDO A MESMA MENSAGEM DE CONEXÃO DO SERVIDOR
msg,servidor=udp.recvfrom(1024)

print('Para sair use CTRL+X\n')
print()

print('Chute um numero entre 0 e 10.')

while True:    
    num=str(input('Digite um numero: '))
    #ENVIANDO CHUTE
    udp.sendto(num.encode(),servidor)
    #REBENDO RESPOSTA DO CHUTE
    msg,servidor=udp.recvfrom(1024)
    if msg.decode()=='Voce Acertou!':
        print(msg.decode())
        break
    else:
        print(msg.decode())
    #RECEBENDO MENSAGEM RELACIONADA AO NUMERO DE CHUTES
    msg,servidor=udp.recvfrom(1024)
    if msg.decode()!='Você antingiu o número maixmo de chutes..':
        print(msg.decode())
    else:
        print(msg.decode())
        break
    #RECEBENDO DICA DE PARA O CHUTE
    msg,servidor=udp.recvfrom(1024)
    print(msg.decode())
udp.close()
