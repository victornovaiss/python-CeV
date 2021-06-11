nome = input('Escreva seu nome: ')

indexOfA = nome.lower().index('a')
lastIndexOfA = nome.lower().rindex('a')
countA = nome.lower().count('a')

print("""
A letra A aparece: {} vezes
A primeira ocorrência dela é no índice: {}
A última ocorrencia dela é no índice: {}
""".format(countA,indexOfA,lastIndexOfA))
