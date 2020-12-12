from random import randint
class Registro:
    def __init__(self,id,nome,ano):
        self._id=id
        self._nome=nome
        self._ano=ano
    def get_nome(self):
        return self._nome
    def set_nome(self,novoNome):
        self._nome=novoNome
    def get_ano(self):
        return self._ano
    def set_ano(self,novoAno):
        self._ano=novoAno
    def get_id(self):
        return self._id
    def __str__(self):
        return f'Nome:{self._nome} {self._ano}'

class No:
    def __init__(self,dado,left=None,right=None):
        self._dado=dado
        self._left=left
        self._right=right
        
    def get_dado(self):
        return self._dado

    def set_dado(self,novadado):
        self._dado=novadado

    def get_left(self):
        return self._left

    def set_left(self,newLeft):
        self._left=newLeft

    def get_right(self):
        return self._right

    def set_right(self,newRight):
        self._right=newRight

class Tree:
    def __init__(self,root=None):
        self._root=root
    
    def get_root(self):
        return self._root

    def add(self,no):
        if self._root==None:
            self._root=no
        else:
            p=self._root
            q=p
            while q!=None:
                if no.get_dado().get_nome()>p.get_dado().get_nome():
                    p=q
                    q=q.get_right()
                else:
                    p=q
                    q=q.get_left()
            if no.get_dado().get_nome()>p.get_dado().get_nome():
                p.set_right(no)
            else:
                p.set_left(no)
    

    def print_date(self,no):
        print(f'Nome: {no.get_dado().get_nome()}\nAno: {no.get_dado().get_ano()}\nID: {no.get_dado().get_id()}\n')

    def print_tree(self,no):
        p=no
        if p!=None:
            self.print_tree(p.get_left())

            self.print_date(p)
            
            self.print_tree(p.get_right())
    
    def find_id(self,id,no):
        p=no
        if p!=None:      
            self.find_id(id,p.get_left())  
            if id==p.get_dado().get_id():
                print(f'Nome: {p.get_dado().get_nome()}\nAno: {p.get_dado().get_ano()}')   
            self.find_id(id,p.get_right())

    def find_year(self,ano,no):
        p=no
        if p!=None:
            self.find_year(ano,p.get_left())
            if ano==p.get_dado().get_ano():
                print(p.get_dado().get_nome())
            self.find_year(ano,p.get_right())

    def height(self,no):
        p=no
        if p == None or p.get_left() == None and p.get_right() == None:
            return 0
        else:
            if self.height(p.get_left()) > self.height(p.get_right()):
                return  1 + self.height(p.get_left())  
            else:
                return  1 + self.height(p.get_right())

    def in_order(self,no):
        p=no
        if p !=None:
            self.print_date(p)
            self.in_order(p.get_left())
            self.in_order(p.get_right())    

filme=Tree()
chaves=[]

print('''==> Menu de Opções <==
1) Adicionar Filme
2) Buscar pelo ID
3) Buscar pelo ANO
4) Lista em ordem Alfabetica
5) Altura da Árvore
6) Exibir Arvore
7) Sair
''')
while True:
    op=str(input('=> '))
    print('=================================================')
    if op == '1':
        id=randint(1,99)
        while id in chaves:
            id=randint(1,99)
        nome=str(input('Digite o nome do Filme: ')).capitalize()
        ano=int(input('Digite o ano de lançamento: '))
        filme.add(No(Registro(id,nome,ano)))
        chaves.append(id)
        print('=================================================')
    elif op=='2':
        i=int(input('id: '))
        if i in chaves:
            filme.find_id(i,filme.get_root())
        else:
            print('Essa chave não existe no catálogo')
        print('=================================================')
    elif op=='3':
        ano=int(input('ano: '))
        filme.find_year(ano,filme.get_root())
        print('=================================================')
    elif op=='4':
        filme.print_tree(filme.get_root())
        print('=================================================')
    elif op=='5':
        print(f'Altura da Arvore =',end=' ')
        print(filme.height(filme.get_root()))
        print('=================================================')
    elif op=='6':
        filme.in_order(filme.get_root())
        print('=================================================')
    elif op=='7':
        print('========== Encerrando ==========')
        break
