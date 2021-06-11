def escreva():
    msg = input('Escreva uma mensagem para exibição: ')
    print('-'*(len(msg)+4))
    print(f'  {msg}')
    print('-'*(len(msg)+4))


escreva()