import random 

pcN = random.randint(0,5)

n = int(input('Qual número (entre 0 e 5) o PC pensou? '))

if pcN == n:
    print('\nVocê acertou!!!')
else:
    print('\nVocê errou :(')

print('\nO computador pensou no número {}'.format(pcN))