nome = input("""
==========================

Escreva seu nome completo: """)

nomeDividido = nome.split()
nomeSemEspaço = ''.join(nomeDividido)

print("""
Nome maiúsculo: {}
Nome minúsculo: {}
N° de letras sem espaço: {}
N° de letras do 1° nome: {}

===========================
""".format(nome.upper(),nome.lower(),len(nomeSemEspaço),nomeDividido[0]))