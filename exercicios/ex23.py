n = int(input('Digite um número entre 0 e 9999: '))

print("""
unidade: {}
dezena: {}
centena: {}
milhar: {}
""".format((n//1%10),(n//10%10),(n//100%10),(n//1000%10)))