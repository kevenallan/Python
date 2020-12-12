class No:
    def __init__(self, dado=None, proximo=None):
      self._dado=dado
      self._proximo=proximo

    def get_dado(self):
      return self._dado

    def set_dado(self,novoDado):
      self._dado=novoDado

    def get_proximo(self):
      return self._proximo

    def set_proximo(self,outro):
      self._proximo=outro

    def __str__(self):
      return '{}'.format(self._dado)


class Game:
  def __init__(self,nome,ano,genero):
    self._nome=nome
    self._genero=genero
    self._ano=ano

  def get_nome(self):
    return self._nome
  
  def set_nome(self,novoNome):
    self._nome=novoNome

  def get_genero(self):
    return self._genero
  
  def set_genero(self,novoGenero):
    self._genero=novoGenero

  def get_ano(self): 
    return self._ano
  
  def set_ano(self,novoAno):
    self._ano=novoAno

  def __str__(self):
    return 'Jogo: {}\nAno de Lançamento: {}\nGenero: {}'.format(self._nome,self._ano,self._genero)


class Lista:
  def __init__(self,no=None):
      self._head=no

  def add_default(self,no):
    no.set_proximo(self._head)
    self._head=no
    return '\033[1;32mJogo adicionado com sucesso!\033[m'

  def add_pos(self,no,posição):
    p=self._head
    cont=0
    if posição>self.tamanho():
      return '\033[1;31mPosição invalida!\033[m \033[4;31mJOGO NÃO ADICIONADO!\033[m'
    else:
      while cont!=posição-1:
        p=p.get_proximo()
        cont+=1
      no.set_proximo(p.get_proximo())
      p.set_proximo(no)
      return '\033[1;32mJogo adicionado com sucesso!\033[m'
  
  def remove_default(self):
      p=self._head
      if self.tamanho()==0:
        return '\033[1;31mA lista já está vazia!\033[m'
      elif self.tamanho()==1:
        self._head=None
        return '\033[1;31mJogo removido com sucesso!\033[m'
      else:
        while p.get_proximo().get_proximo()!=None:
          p=p.get_proximo()
        p.set_proximo(None)
        return '\033[1;31mJogo removido com sucesso!\033[m'

  def remove_pos(self,pos):
    p=self._head
    cont=0
    if self._head==None:
      return '\033[1;31mA Lista já está Vazia!\033[m'
    elif pos==0:
      self._head=self._head.get_proximo()
      return '\033[1;31mJogo removido com sucesso!\033[m'
    elif pos >= int(self.tamanho()):
      return '\033[1;31mPosição Inexistente!\033[m'
    else:
      while cont!=pos-1:
        p=p.get_proximo()
        cont+=1
      new=p.get_proximo().get_proximo()
      p.set_proximo(new)
      return '\033[1;31mJogo removido com sucesso!\033[m'

  def exibir(self):
      if self._head==None:
        return '\033[1;31mA Lista está Vazia!\033[m'
      else:
        return self._head.get_dado()

  def caminhar(self):
      if self._head==None:
        print('\033[1;31mA Lista está Vazia!\033[m')
      else:
        p=self._head
        while p!=None:
            print('---------------------------')  
            print(p)
            p=p.get_proximo()
        print('---------------------------')      
        
  def tamanho(self):
    p=self._head
    cont=0
    while p!=None:
      cont+=1
      p=p.get_proximo()
    return cont 

  def vazio(self):
    res=self._head==None     
    if res ==True:
      return f'\033[1;32m{res}\033[m'
    return f'\033[1;31m{res}\033[m'

  
  
  def ordenar(self):
    contador=0
    tamanho=self.tamanho()
    while contador!=tamanho:
      p=self._head
      q=p.get_proximo()
      posição=0
      while q!=None:
        if p.get_dado().get_ano()>q.get_dado().get_ano():
          
          new=No(Game(p.get_dado().get_nome(),p.get_dado().get_ano(),p.get_dado().get_genero()))
          
          self.add_pos(new,posição+2)
          self.remove_pos(posição)
        
        p=p.get_proximo()
        q=q.get_proximo()
        posição+=1
      contador+=1





#Lista de jogos
lista=Lista()
lista.add_default(No(Game('Counter Strike','2000','FPS')))
lista.add_default(No(Game('LOL','2009','Moba')))
#lista.add_default(No(Game('Gran Turismo','1997','Corrida')))
#lista.add_default(No(Game('GTA V','2013','Ação')))
#lista.add_default(No(Game('FIFA','2020','Futebol')))
#lista.add_default(No(Game('KOF','2002','Luta')))



print('''==> Menu de Opções <==
1) Adicionar Jogo
2) Remover Jogo
3) Mostrar 1º Elemento da Lista
4) Mostrar Todos os Elementos 
5) Mostrar o Tamanho da Lista
6) Verificar se está vazia
7) Ordenar Lista
0) Sair
''')
while True:
  op=input('=> ')
  if op=='1':
    nome=input('Nome do jogo: ').capitalize()
    ano=input('Ano de lançamento: ')
    while len(ano)!=4:
      ano=str(input('Ano Inválido! Informe outro: '))
    genero=str(input('Gênero do jogo: ')).capitalize()
    addpos=input('Deseja adicionar em uma posição específica? ').upper()
    game=Game(nome,ano,genero)

    while True:
      if addpos=='SIM' or addpos=='NAO' or addpos=='NÃO':
        break
      addpos=str(input('Deseja adicionar em uma posição específica [sim/não]? ')).upper()

    if addpos=='NAO' or addpos=='NÃO':
      print('----------------------------')
      print(lista.add_default(No(game)))
      print('----------------------------')
    else:
        pos=int(input('Digite a posição: '))
        if pos == 0:
          print('----------------------------')
          print(lista.add_default(No(game)))
          print('----------------------------')
        else:
          tamanho_lista=lista.tamanho()
          print('----------------------------')
          print(lista.add_pos(No(game),pos))
          print('----------------------------')
  
  elif op=='2':
    addpos=str(input('Deseja remover de uma posição especifica? ')).upper()
    while True:
      if addpos=='SIM' or addpos=='NAO' or addpos=='NÃO':
        break
      addpos=str(input('Deseja remover de uma posição específica [sim/não]? ')).upper()
    if addpos=='NAO' or addpos=='NÃO':
      print('---------------------------')
      print(lista.remove_default())
      print('---------------------------')
    else:
      pos=int(input('De que posição deseja remover? '))
      print('---------------------------')
      print(lista.remove_pos(pos))
      print('---------------------------')
  
  elif op=='3':
    print('---------------------------')
    print(lista.exibir())
    print('---------------------------')

  elif op=='4':  
    print('---------------------------')
    lista.caminhar()
    print('---------------------------')

  elif op=='5':  
    print('---------------------------')
    if lista.tamanho()==0:
      print(f'Quantidade de jogo(s): \033[1;31m{lista.tamanho()}\033[m')
    else:
      print(f'Quantidade de jogo(s): \033[1;32m{lista.tamanho()}\033[m')
    print('---------------------------')
  
  elif op=='6':
    print('---------------------------')
    print(lista.vazio())
    print('---------------------------')
  
  elif op=='7':
    lista.ordenar()

  elif op=='0':
    break

  else:
    print('---------------------------------------')
    print('\033[1;31mOperação desconhecida. Tente novamente!\033[m')
    print('---------------------------------------')
print('Operação finalizada')