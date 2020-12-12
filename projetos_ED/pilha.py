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


class Pilha:
  def __init__(self,no=None):
      self._topo=no

  def add(self,no):
      no.set_proximo(self._topo)
      self._topo=no

  def remove(self):
      if self._topo==None:
        return '\033[1;31mPilha Vazia!\033[m'
      else:
        self._topo=self._topo.get_proximo()
        return '\033[1;31mJogo removido com sucesso!\033[m'
  def exibir(self):
      if self._topo==None:
        return '\033[1;31mPilha Vazia!\033[m'
      else:
        return self._topo.get_dado()

  def tamanho(self):
    cont=0
    p=self._topo
    while p!=None:
        cont+=1
        p=p.get_proximo()
    if cont==0:
      print(f'Quantidade de jogo(s): \033[1;31m{cont}\033[m')
    else:
      print(f'Quantidade de jogo(s): \033[1;32m{cont}\033[m')
  def vazio(self):
    res=self._topo==None
    if self._topo==None:
      return f'\033[1;32m{res}\033[m'
    else:
      return f'\033[1;31m{res}\033[m'
  def caminhar(self):
    if self._topo==None:
      print('---------------------------')
      print('\033[1;31mA Pilha está Vazia!\033[m')
      print('---------------------------')
    else:  
      p=self._topo
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


pilha=Pilha(No(Game('lol',2009,'MOBA')))
print('---------------------------')
print('''==> Menu de Opções <==
1) Adicionar Jogo
2) Remover Jogo
3) Mostrar o primeiro elemento da Pilha
4) Mostrar o tamanho da Pilha
5) Verificar se a Pilha está vazia
6) Mostrar todos os jogos da Pilha
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
    
    pilha.add(No(game))
    print('----------------------------')
    print('\033[1;32mJogo adicionado com sucesso!\033[m')
    print('----------------------------')

  elif op=='2':
    print('---------------------------')
    print(pilha.remove())
    print('---------------------------')

  elif op=='3':
    print('---------------------------')
    print(pilha.exibir())
    print('---------------------------')

  elif op=='4':
    print('---------------------------')
    pilha.tamanho()
    print('---------------------------')

  elif op=='5':
    print('---------------------------')
    print(pilha.vazio())
    print('---------------------------')
  
  elif op=='6':
    pilha.caminhar()

  elif op=='0':
    break

  else:
    print('----------------------------------------')
    print('\033[1;31mOperação desconhecida. Tente novamente!\033[m')
    print('----------------------------------------')
print('Operação finalizada')