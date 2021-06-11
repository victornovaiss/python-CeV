v = int(input('Velocidade registrada de: '))

multa = (v-80)*7

if v>80:
    print("""
    Velocidade acima do permitido por lei
                    MULTA
    +------------------------------------+
    |               R$ {}                |
    |                                    |
    +------------------------------------+
    """.format(multa))
