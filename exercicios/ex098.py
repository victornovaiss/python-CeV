from time import sleep

def contagem(i,f,p):
    print('-='*15)
    print(f'Sua contagem vai de {i} até {f} com passo de {p}')
    if i>f:
        for c in range(i,f-1,-abs(p)):
            print(c,end=' ',flush=True)
            sleep(0.3)       
    elif i<f:
        for c in range(i,f+1,abs(p)):
            print(c,end=' ',flush=True)
            sleep(0.3)
    print('Fim da contagem')
    
    


contagem(1,10,1)
sleep(1)
contagem(10,0,2)
sleep(1)
inicio = int(input('Início da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo da contagem: '))

contagem(inicio,fim,passo)
