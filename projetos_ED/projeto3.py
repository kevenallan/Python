import time
from random import randint

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
    return lista

def insertion_sort(array): 
    for i in range(1, len(array)): 
        key = array[i] 
        posição = i-1
        while posição >=0 and key < array[posição] : 
                array[posição+1] = array[posição] 
                posição -= 1
        array[posição+1] = key 
    return array

def raiz(lista, n, i): 
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and lista[i] < lista[l]: 
        maior = l 
    if r < n and lista[maior] < lista[r]: 
        maior = r 
    if maior != i: 
        lista[i],lista[maior] = lista[maior],lista[i]
        raiz(lista, n, maior) 
def heap_sort(lista): 
    n = len(lista) 
    for i in range(n, -1, -1): 
        raiz(lista, n, i) 
    for i in range(n-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i] 
        raiz(lista, i, 0) 
    return lista

def comb_sort(lista):
    gap = len(lista)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(lista) - gap):
            j = i+gap
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                swaps = True
    return lista

def shell_sort(lista): 
    n = len(lista) 
    gap = n//2
    while gap > 0: 
  
        for i in range(gap,n): 
            elemento = lista[i] 
            indice = i 
            while  indice >= gap and lista[indice-gap] >elemento: 
                lista[indice] = lista[indice-gap] 
                indice -= gap 
            lista[indice] = elemento 
        gap //= 2
    return lista

def partição(lista,menor,maior): 
    i = ( menor-1 )
    pivot = lista[maior]
    for j in range(menor , maior): 
        if   lista[j] <= pivot: 
            i = i+1 
            lista[i],lista[j] = lista[j],lista[i] 
    lista[i+1],lista[maior] = lista[maior],lista[i+1] 
    return ( i+1 ) 
def quick_sort(lista,menor,maior): 
    if menor < maior: 
        pi = partição(lista,menor,maior) 
        quick_sort(lista, menor, pi-1) 
        quick_sort(lista, pi+1, maior) 
    return lista 

def merge_sort(lista): 
    if len(lista) >1: 
        mid = len(lista)//2
        L = lista[:mid]
        R = lista[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                lista[k] = L[i] 
                i+=1
            else: 
                lista[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            lista[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            lista[k] = R[j] 
            j+=1
            k+=1
    return lista


vetor=[]
for c in range(20000):
    vetor.append(randint(1,5000))

#BUBBLE_SORT
bubble=vetor.copy()
inicio_bubble=time.time()
bubble=bubble_sort(bubble)
fim_bubble=time.time()
tempo_bubble=fim_bubble-inicio_bubble


#INSERTION_SORT
insertion=vetor.copy()
inicio_insertion=time.time()
insertion=insertion_sort(insertion)
fim_insertion=time.time()
tempo_insertion=fim_insertion-inicio_insertion


#HEAP_SORT
heap=vetor.copy()
inicio_heap=time.time()
heap=heap_sort(heap)
fim_heap=time.time()
tempo_heap=fim_heap-inicio_heap


#COMB_SORT
comb=vetor.copy()
inicio_comb=time.time()
comb=comb_sort(comb)
fim_comb=time.time()
tempo_comb=fim_comb-inicio_comb


#SHELL_SORT
shell=vetor.copy()
inicio_shell=time.time()
shell=shell_sort(shell)
fim_shell=time.time()
tempo_shell=fim_shell-inicio_shell


#QUICK_SORT
quick=vetor.copy()
inicio_quick=time.time()
quick=quick_sort(quick,0,len(quick)-1)
fim_quick=time.time()
tempo_quick=fim_quick-inicio_quick


#MERGE_SORT
merge=vetor.copy()
inicio_merge=time.time()
merge=merge_sort(merge)
fim_merge=time.time()
tempo_merge=fim_merge-inicio_merge

print(f'''======================================
BubbleSort = {tempo_bubble}
InsertionSort = {tempo_insertion}
HeapSort = {tempo_heap}
CombSort = {tempo_comb}
ShellSort = {tempo_shell}
QuickSort = {tempo_quick}
MergeSort = {tempo_merge}
======================================''')

