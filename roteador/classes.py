from random import randint
import time
class ListaException (Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Roteador:
    def __init__(self):
        self.__banda_larga=10.0 #mg
        self.__lista_pcs=[]
        self.__lista_recursos=[]
        self.__jobs=[]
        self.__ips_em_uso=[]
        self.__jobs_finalizados=[]
    #LISTANDO TODOS OS PCS CADASTRADOS
    def get_lista_pcs(self):
        if len(self.__lista_pcs)==0:
            raise ListaException('Nenhnum computador foi cadastrado!')
        try:
            for pc in self.__lista_pcs:
                print('Nome do pc: {}'.format(pc.get_nome()))
                print('IP do pc: {}'.format(pc.get_ip()))
                print('Prioritario: {}'.format(pc.get_prioritario()))
                print()
        except:
            raise
    #LISTANDO TODOS OS PCS QUE ESTAO NA LISTA DE JOBS
    def get_lista_pcs_job(self):
        if len(self.__jobs)==0:
            raise ListaException('Nenhnum job cadastrado!')
        try:
            for job in self.__jobs:
                print(job.get_computador().get_nome())
                print(job.get_computador().get_ip())
                print(job.get_banda_larga())
        except:
            raise

    def get_lista_recursos(self):
        if len(self.__lista_recursos) == 0:
            raise ListaException('Nenhnum recursos foi cadastrado!')
        try:
            for recurso in self.__lista_recursos:
                print('Nome do arquivo: {}'.format(recurso.get_nome()))
                print('Tamanho do arquivo: {} KBs'.format(recurso.get_tamanho()))
                print()
        except:
            raise 
    def get_jobs_finalizados(self):
        for job in self.__jobs_finalizados:
            print(job)

    def set_banda_larga(self,nova_banda):
        self.__banda_larga=nova_banda
        self.distribuir_banda_larga()
    
    def set_jobs_finalizados(self,novo_job):
        self.__jobs_finalizados.append(novo_job)

    def cadastrar_pc(self,pc):
        ip=pc.get_ip()
        while ip in self.__ips_em_uso:
            ip='192.168.30.'+str(randint(0,9))+str(randint(0,9))
        pc.set_ip(ip)
        self.__ips_em_uso.append(ip)
        self.__lista_pcs.append(pc)
        return '''
Computador cadastrado com sucesso!
Nome: {}
Ip: {}
Prioritário: {}'''.format(pc.get_nome(),pc.get_ip(),pc.get_prioritario())

    def cadastrar_recurso(self,recurso):
        for recurso_cadastrado in self.__lista_recursos:
            if recurso_cadastrado.get_nome()==recurso.get_nome():
                print('Esse recurso já está cadastrado!')
                return
        self.__lista_recursos.append(recurso)
        return '''
Recurso cadastrado com sucesso!
Nome: {}
Tamanho: {} KBs
'''.format(recurso.get_nome(),recurso.get_tamanho())

    def adicionar_job(self,nome_pc,nome_rec):
        job=[]
        for pc in self.__lista_pcs:
            if pc.get_nome()==nome_pc:
                job.append(pc)
        if len(job)==0:
            raise ListaException('A lista não contém o computador informado. ')
        for recurso in self.__lista_recursos:
            if recurso.get_nome()==nome_rec:
                job.append(recurso)
        if len(job)!=2:
            raise ListaException('A lista não contém o recurso informado. ')
        else:
            novo_job=Job(job[0],job[1])
            self.__jobs.append(novo_job)
            self.distribuir_banda_larga()
            print('Job adicionado com sucesso!')

    def remover_job(self,nome_pc):
        job_removido=None
        for indice,job in enumerate(self.__jobs):
            if job.get_computador().get_nome()==nome_pc:
                job_removido=indice
                self.__jobs.pop(indice)
                return 'Job retirado da lista!'
        if job_removido==None:
            raise ListaException('Dado informado não existe.')
        if len(self.__jobs)==0:
            return
        else:
            self.distribuir_banda_larga()
    ############################################################ NAO FUNCIONA #########################################################
    def distribuir_banda_larga(self):
        contador_prioritarios=0
        quantidade_pcs=len(self.__jobs)
        banda_larga_disponivel=self.__banda_larga
        mega=0
        mega_prioritario=0
        #CONTANDO PCS PRIORITARIOS
        for job in self.__jobs:
            if job.get_computador().get_prioritario()=='s':
                contador_prioritarios+=1
        #CALCULANDO MEGAS
        if quantidade_pcs==1:
            mega=mega_prioritario=banda_larga_disponivel
        elif contador_prioritarios==quantidade_pcs:
            mega_prioritario=banda_larga_disponivel/quantidade_pcs
        elif contador_prioritarios==0:
            mega=banda_larga_disponivel/quantidade_pcs
        else:
            mega_prioritario=(banda_larga_disponivel/quantidade_pcs)+(banda_larga_disponivel*0.10)
            banda_larga_disponivel-=(mega_prioritario*contador_prioritarios)
            mega=banda_larga_disponivel/(quantidade_pcs-contador_prioritarios)
        #DISTRIBUINDO MEGAS
        for job in self.__jobs:
            if job.get_computador().get_prioritario()=='s':
                job.set_banda_larga(mega_prioritario)
            else:
                job.set_banda_larga(mega)
    
    def exportar(self):
        if len(self.__lista_pcs)>0:
            arq=open('repositorio.txt','a')
            pcs=''
            for pc in self.__lista_pcs:
                pcs+=str("{},{},{}\n".format(pc.get_nome(),pc.get_ip(),pc.get_prioritario()))
            arq.write(pcs)
            print('Computadores exportados com sucesso!')
        else:
            print('Não tem nenhum computador cadastrado para ser exportado')
    def exportar_recursos (self):
        if len(self.__lista_recursos)>0:
            arq=open('repositorio2.txt', 'a')
            pcs= ''
            for rec in self.__lista_recursos:
                pcs+=str("{},{}\n".format(rec.get_nome(),rec.get_tamanho()))
            arq.write(pcs)
            print('Recursos exportados com sucesso!')
        else:
            print('Não tem nenhum recurso cadastrado para ser exportado.')
    def importar(self):
        try:
            arq=open('repositorio.txt','r')
            text=arq.read().replace('\n',';')
            text=text.split(';')
            text.pop()
            for linha in text:
                comp=linha.split(',')
                pc=Computador(comp[0],comp[1],comp[2])
                self.cadastrar_pc(pc)
            print('Importação de computadores concluida. ')
        except:
            raise ListaException('Não há nenhum computador para ser importado.')
        
    def importar_recursos (self):
        try:
            arq=open('repositorio2.txt','r')
            text=arq.read().replace('\n',';')
            text=text.split(';')
            text.pop()
            for linha in text:
                rec=linha.split(',')
                recurso=Recurso(rec[0],rec[1])
                self.cadastrar_recurso(recurso)
            print('Importação de recursos concluida.')
        except:
            raise ListaException('Não há nenhum recurso para ser importado.')

#################################################################################################################
    def inciar_simulacao(self):
        if len(self.__jobs)==0:
            raise ListaException('Não há nenhum job cadastrado para poder iniciar a simulação.')
        else:
            x=len(self.__jobs)
            while len(self.__jobs)!=0:
                for job in self.__jobs:
                    if job.get_computador().get_prioritario()=='s':
                        kbs=job.get_kbBaixados()+(job.get_banda_larga()*100)
                        job.set_kbBaixados(kbs)
                        job.set_ciclos(job.get_ciclos()+1)
                    elif job.get_computador().get_prioritario()=='n':
                        kbs=job.get_kbBaixados()+(job.get_banda_larga()*100)
                        job.set_kbBaixados(kbs)
                        job.set_ciclos(job.get_ciclos()+1)
                    
                    baixado=job.get_kbBaixados()
                    tamanho=job.get_recurso().get_tamanho()
                    baixado=int(baixado)
                    tamanho=int(tamanho)

                    if baixado>=tamanho:
                        nome_pc=job.get_computador().get_nome()
                        self.set_jobs_finalizados(job)
                        self.remover_job(nome_pc)
                        

                    print(f''' 
                    Computador: {job.get_computador().get_nome()}
                    Tamanho total do arquivo: {tamanho}
                    Progresso kBs: {baixado}
                    ciclos: {job.get_ciclos()}
                    Kb/s : {kbs}
                    ''')
    def exibir_jobs_finalizados(self):
        if len(self.__jobs_finalizados)==0:
            print('Nenhum job foi finalizado ainda.')
        else:
            for job in self.__jobs_finalizados:
                print('''
                Computador:         {}
                Ip :                {}
                Prioritario :       {}
                Recurso :           {}
                Tamanho do recurso: {}
                Numero de ciclos:   {}
                '''.format(job.get_computador().get_nome(),job.get_computador().get_ip(),job.get_computador().get_prioritario(),job.get_recurso().get_nome(),job.get_recurso().get_tamanho(),job.get_ciclos()))
class Computador:
    def __init__(self,nome,ip,prioritario):
        self.__nome=nome
        self.__ip=ip
        self.__prioritario=prioritario
    def get_nome(self):
        return self.__nome
    def get_ip(self):
        return self.__ip
    def get_prioritario(self):
        return self.__prioritario
    def set_nome(self,novo_nome):
        self.__nome=novo_nome
    def set_ip(self,novo_ip):
        self.__ip=novo_ip
    def set_prioritario(self,novo_prioritario):
        self.__prioridade=novo_prioritario

class Recurso:
    def __init__(self,nome,tamanho):
        self.__nome=nome
        self.__tamanho=tamanho
    def get_nome(self):
        return self.__nome
    def get_tamanho(self):
        return self.__tamanho
    def set_nome(self,novo_nome):
        self.__nome=novo_nome
    def set_tamanho(self,novo_tamanho):
        self.__tamanho=novo_tamanho

class Job:
    def __init__(self,computador,recurso):
        self.__computador=computador
        self.__recurso=recurso
        self.__banda_larga=0
        self.__kbBaixados=0
        self.__ciclos=0

    def get_computador(self):
        return self.__computador
    def get_recurso(self):
        return self.__recurso
    def get_banda_larga(self):
        return self.__banda_larga
    def get_kbBaixados(self):
        return self.__kbBaixados
    def get_ciclos(self):
        return self.__ciclos
    def set_computador(self,novo_computador):
        self.__computador=novo_computador
    def set_recurso(self,novo_recurso):
        self.__recurso=novo_recurso
    def set_banda_larga(self,nova_banda):
        self.__banda_larga=nova_banda
    def set_kbBaixados(self,novo_kbBaixados):
        self.__kbBaixados=novo_kbBaixados
    def set_ciclos(self,novo_ciclo):
        self.__ciclos+=1
    ###################################
    