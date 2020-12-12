def adicionar(nome,cpf,email):
    arq=open('registros.txt','a')
    arq.write(f'{nome};{cpf};{email}\n')
    arq.close()

def pesquisar(cpf):
    arq=open('registros.txt','r')
    conteudo=arq.read()
    conteudo=conteudo.replace('\n',';')
    clientes=conteudo.split(';')
    for c in range(len(clientes)):
        if cpf == clientes[c]:
            dados=f'Nome: {clientes[c-1]}\nCPF: {clientes[c]}\nE-mail: {clientes[c+1]}'
            break
        else:
            dados='Esse CPF não foi cadastrado!'
    arq.close()
    return dados
    
def alterar(cpf):
    arq=open('registros.txt','r')
    conteudo=arq.read()
    conteudo=conteudo.replace('\n',';')
    clientes=conteudo.split(';')
    if '' in clientes:
        index=clientes.index('')
        clientes.pop(index)
    alterar=False
    for c in range(len(clientes)):
        if cpf == clientes[c]:
            novo_nome=str(input('Digite o novo nome: '))
            clientes[c-1]=novo_nome
            alterar=True
            break
        else:
            alterar=False
    if alterar == False:
        return 'Esse CPF não foi cadastrado!'
    arq.close()
    texto=''
    contador=1
    for c in clientes:
        if contador%3!=0:
            texto+=c+';'
        else:
            texto+=c+'\n'    
        contador+=1    
    arq=open('registros.txt','w')
    arq.write(f'{texto}')
    arq.close()
    return 'Nome alterado com sucesso!'

def excluir(cpf):
    arq=open('registros.txt','r')
    conteudo=arq.read()
    conteudo=conteudo.replace('\n',';')
    clientes=conteudo.split(';')
    if '' in clientes:
        index=clientes.index('')
        clientes.pop(index)
    
    apagar=False
    for c in range(len(clientes)):
        if cpf == clientes[c]:
            indice=c-1
            apagar=True
            break
        else:
            apagar=False
    if apagar==False:
        return 'Esse CPF não foi cadastrado!'
    for c in range(3):
        clientes.pop(indice)
    texto=''
    contador=1
    for c in clientes:
        if contador%3!=0:
            texto+=c+';'
        else:
            texto+=c+'\n'    
        contador+=1    
    arq=open('registros.txt','w')
    arq.write(f'{texto}')
    arq.close()
    return 'Cliente apagado com sucesso!'

print('''=========================
     Menu de Opções
=========================
1) Cadastrar usuário
2) Pesquisar usuário
3) Alterar usuário
4) Excluir usuário
5) Sair''')
while True:
    opção=str(input('Opção escolhida: '))
    if opção=='1':
        opções_email=[]
        dominio='@ifnet.com.br'
        nome=str(input('Digite seu nome: '))
        cpf=str(input('Digite seu cpf: '))
        #OP1
        opção1=cpf.replace('.','')
        opção1=opção1.replace('-','')
        opção1+=dominio
        opções_email.append(opção1)
        #OP2
        vetor_nome=nome.split(' ')
        opção2=f'{vetor_nome[0]}.{vetor_nome[-1]}{dominio}'
        opções_email.append(opção2)
        #OP3
        opção3=f'{vetor_nome[0]}{cpf[0:3]}{dominio}'
        opções_email.append(opção3)
        #OPÇÕES:
        print()
        print('Escolha uma das Opções de e-mail')
        for c in range(len(opções_email)):
            print(f'    {c+1}. {opções_email[c]}')
        opção_escolhida=int(input('Opção de e-mail escolhida: '))
        email=opções_email[opção_escolhida-1]
        
        #VERIFICAR SE CPF E E-MAIL SÃO PERMITIDOS
        arq=open('registros.txt','r')
        clientes=arq.readlines()
        cadastrado=False
        for c in range(len(clientes)):
            if cpf in clientes[c]:
                msg='Esse CPF já foi Cadastrado! Tente Novamente...'
                cadastrado=True
                break
            if email in clientes[c]:
                msg='Esse E-MAIL já foi Cadastrado! Tente Novamente...'
                cadastrado=True
                break
        if cadastrado==False:
            adicionar(nome,cpf,email)
        
        else:
            print(msg)
        arq.close()
    
    elif opção=='2':
        cpf=str(input('Digite o CPF do cliente que deseja pesquisar: '))
        print(pesquisar(cpf))
    
    elif opção=='3':
        cpf=str(input('Digite o CPF do cliente que deseja alterar o nome: '))
        print(alterar(cpf))

    elif opção=='4':
        cpf=str(input('Digite o CPF do cliente que deseja apagar: '))
        print(excluir(cpf))
    elif opção=='5':
        print('Encerrando a execução do programa...')
        break
    else:
        print('OPÇÂO INVÁLIDA!')