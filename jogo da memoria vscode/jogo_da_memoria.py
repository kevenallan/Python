import os
from time import sleep
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
      
      #sleep(1)
    #os.system("cls")
    return x

def fim_jogo(partida,chutes):
  if partida==tabela:
    exibir_jogo()
    print('Você Venceu!')
    return 'encerrar'

  elif chutes==20:
    exibir_jogo()
    print('Você Perdeu!')
    return 'encerrar'
  return ''

while p!='encerrar':
  x=exibir_jogo()
  print(x)
  jogador=str(input('Digite sua jogada: ')) 
  numero_tentativas+=1
  y=jogada(jogador)
  print(y)
  p=fim_jogo(jogo,numero_tentativas)
