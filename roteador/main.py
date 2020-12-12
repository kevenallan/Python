from classes import Roteador,ListaException,Computador,Recurso,Job
from random import randint
import time 

roteador=Roteador()
# computador=Computador()
# recurso=Recurso()
# job=Job()

# banda=int(input('Digite o tamanho da banda larga: '))
# roteador.set_banda_larga(banda)
while True:
    print ('''
        01. Cadastrar computadores.
        02. Exportar dados/Importar.
        03. Listar computadores.
        04. Cadastrar recursos.
        05. Listar Recursos.
        06. Inserir jobs 2 para processamento (download).
        07. Remover um job da lista de execução.
        0. Iniciar a simulação.
        0. Exibir sequência de jobs finalizados.
        10. Povoamento automático.
        00. Sair do programa.
        ''')

    op= input(' Informe a opção escolhida: ')
    if op=='01' or op=='1':
        pc=[]
        nome=str(input('Nome do computador: '))
        prioritario=str(input(f'O computador {nome} é prioritario [s/n]? ')).lower()
        while True:
            if prioritario=='n' or prioritario=='s':
                break
            prioritario=str(input(f'O computador {nome} é prioritario? Digite apenas [s/n]: ')).lower()

        ip='192.168.15.'+str(randint(0,9))+str(randint(0,9))
        #
        pc=Computador(nome,ip,prioritario)
        pc_cadastrado=roteador.cadastrar_pc(pc)
        print(pc_cadastrado)
    elif op=='02' or op=='2':
        print('''1-Exportar
2-Importar''')
        op=str(input('Escolha uma das opções: '))
        if op=='1':
            roteador.exportar()
            roteador.exportar_recursos()
        elif op=='2':
            roteador.importar()
            roteador.importar_recursos()
    elif op=='03' or op=='3':
        try:
            roteador.get_lista_pcs()
        except ListaException as li:
            print(li)
        print('pcs em job')
        try:
            roteador.get_lista_pcs_job()
        except ListaException as li:
            print(li)
    elif op=='04' or op=='4':
        recursos=[]
        nome=str(input('Nome do arquivo: ')).lower()
        tamanho=str(input('Tamanho do arquivo: '))
        #
        recurso=Recurso(nome,tamanho)
        recurso_cadastrado=roteador.cadastrar_recurso(recurso)
        print(recurso_cadastrado)
    elif op=='05' or op=='5':
        try: 
            roteador.get_lista_recursos()
        except ListaException as li:
            print (li)
    elif op=='06' or op=='6':
        try:
            nome_pc=str(input('Nome do computador: '))
            nome_recurso=str(input('Nome do arquivo: '))
            roteador.adicionar_job(nome_pc,nome_recurso)
        except ListaException as li:
            print (li)
    elif op=='07' or op=='7':
        try:
            nome_pc=str(input('Nome do computador que deseja retirar da lista de jobs: '))
            roteador.remover_job(nome_pc)
        except ListaException as li:
            print (li)

    elif op=='10':
        print('povoando automaticamente...')
        
        pc1=Computador('IFPB01','192.168.30.31','s')
        pc2=Computador('IFPB05','192.168.30.01','s')
        pc3=Computador('IFPB10','192.168.30.55','s')
        pc4=Computador('IFPB15','192.168.30.51','s')
        pc5=Computador('IFPB20','192.168.30.12','n')
        pc6=Computador('IFPB13','192.168.30.03','n')
        pc7=Computador('IFPB07','192.168.30.11','n')
        pc8=Computador('IFPB03','192.168.30.77','n')
        pc9=Computador('IFPB18','192.168.30.05','n')
        pc10=Computador('IFPB02','192.168.30.10','n')
        rec1=Recurso('documento1.doc',1500)
        rec2=Recurso('teste.py',150)
        rec3=Recurso('projeto.js',150)
        rec4=Recurso('horarios.txt',150)
        rec5=Recurso('ifpb.png',150)
        roteador.cadastrar_pc(pc1)
        roteador.cadastrar_pc(pc2)
        roteador.cadastrar_pc(pc3)
        roteador.cadastrar_pc(pc4)
        roteador.cadastrar_pc(pc5)
        roteador.cadastrar_pc(pc6)
        roteador.cadastrar_pc(pc7)
        roteador.cadastrar_pc(pc8)
        roteador.cadastrar_pc(pc9)
        roteador.cadastrar_pc(pc10)
        roteador.cadastrar_recurso(rec1)
        roteador.cadastrar_recurso(rec2)
        roteador.cadastrar_recurso(rec3)
        roteador.cadastrar_recurso(rec4)
        roteador.cadastrar_recurso(rec5)
        time.sleep(2)
        print('Povoamento completo!')
    elif op=='00' or op=='0':
        break
    
