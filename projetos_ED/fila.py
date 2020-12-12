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


class Fila:
  def __init__(self,no):
      self._head=no

  def remove(self):
      if self._head==None:
        return '\033[1;31mA Fila já está Vazia!\033[m'
      else:  
        self._head=self._head.get_proximo()
        return '\033[1;31mJogo removido com sucesso!\033[m'

  def add(self,no):
    p=self._head
    if self._head==None:
      self._head=no
    else:
      while p.get_proximo()!=None:
        p=p.get_proximo()
      p.set_proximo(no)

  def exibir(self):
      if self._head==None:
        return '\033[1;31mFila Vazia!\033[m'
      else:
        return self._head.get_dado()
  
  def vazio(self):
    if self._head==None:
      res=self._head==None
      return f'\033[1;32m{res}\033[m'
    else:
      res=self._head==None
      return f'\033[1;31m{res}\033[m'
    
  def tamanho(self):
    p=self._head
    cont=0
    while p!=None:
      cont+=1
      p=p.get_proximo()
    if cont==0:
      return f'Quantidade de jogo(s): \033[1;31m{cont}\033[m'
    else:
      return f'Quantidade de jogo(s): \033[1;32m{cont}\033[m'

  def caminhar(self):
    if self._head==None:
      print('---------------------------')
      print('\033[1;31mA Pilha está Vazia!\033[m')
      print('---------------------------')
    else:  
      p=self._head
      while p!=None:
        print('---------------------------')
        print(p.get_dado())
        p=p.get_proximo()
      print('---------------------------')


class Game:
  def __init__(self,nome,ano,genero):
    self._nome=nome
    self._ano=ano
    self._genero=genero
    
  
  def get_nome(self):
    self._nome
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
    return f'''Nome: {self._nome}
Ano de lançamento: {self._ano}
Gênero: {self._genero}'''


fila=Fila(No(Game('Lol',2009,'Moba')))
print('---------------------------')
print('''==> Menu de Opções <==
1) Adicionar Jogo
2) Remover Jogo
3) Mostrar o primeiro elemento da Fila
4) Mostrar o tamanho da Fila
5) Verificar se a Fila está vazia
6) Mostrar todos os jogos da Fila
0) Sair
''')
while True:
  op=input('=> ')
  if op=='1':
    nome=str(input('Nome do jogo: ')).capitalize()
    ano=str(input('Ano de lançamento: '))
    while len(ano)!=4:
      ano=str(input('Ano Inválido! Informe outro: '))
        
    genero=str(input('Gênero do jogo: ')).capitalize()
    game=Game(nome,ano,genero)
    
    fila.add(No(game))
    print('----------------------------') 
    print('\033[1;32mJogo adicionado com sucesso!\033[m')
    print('----------------------------')

  elif op=='2':
    print('---------------------------')
    print(fila.remove())
    print('---------------------------')

  elif op=='3':
    print('---------------------------')
    print(fila.exibir())
    print('---------------------------')

  elif op=='4':
    print('---------------------------')
    print(fila.tamanho())
    print('---------------------------')

  elif op=='5':
    print('---------------------------')
    print(fila.vazio())
    print('---------------------------')
  
  elif op=='6':
    fila.caminhar()
  
  elif op=='0':
    break

  else:
    print('----------------------------------------')
    print('\033[1;31mOperação desconhecida. Tente novamente!\033[m')
    print('----------------------------------------')
print('Operação finalizada')