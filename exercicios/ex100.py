from random import randint
from time import sleep

def sorteio():
    i = 0
    while i<5:
        num.append(randint(1,100))
        print(num[i],flush=True,end=' ')
        sleep(0.5)
        i+=1

    print('Fim do sorteio')

def somaPar(lista):
    s = 0
    for el in lista:
        if el%2 == 0:
            s+=el
    print(f'A soma dos elementos pares é {s}')

num = []
sorteio()
somaPar(num)