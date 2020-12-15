ips_usados=[]
nome=str(input('Nome do computador: ')).upper()
prioritario=str(input(f'O computador {nome} é prioritario [s/n]? ')).lower()
while True:
    if prioritario=='n' or prioritario=='s':
        break
    prioritario=str(input(f'O computador {nome} é prioritario? Digite apenas [s/n]: ')).lower()
ip='192.168.30.'+str(randint(0,9))+str(randint(0,9))

while ip in ips_usados:
    ip='192.168.30.'+str(randint(0,9))+str(randint(0,9))
ips_usados.append(ip)
pc=Computador(nome,ip,prioritario)
pc_cadastrado=roteador.cadastrar_pc(pc)