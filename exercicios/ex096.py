def area(l,c):
    a = l*c
    print(f'O seu terreno tem uma área de {a}m²')

largura = float(input('Escreva a largura do seu terreno em metros: '))
comprimento = float(input('Escreva o comprimento do seu terreno em metros: '))

area(largura,comprimento)