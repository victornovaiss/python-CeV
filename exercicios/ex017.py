from math import hypot

c1 = float(input('Informe o cateto oposto: '))
c2 = float(input('Informe o cateto adjacente: '))

print('A hipotenusa é {}'.format(hypot(c1,c2)))