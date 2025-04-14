while True:

    numero = int(input("Digite um numero positivo: "))

    if numero < 0:
        print('O numero não é positivo, tente novamente.')
        continue
    else:
        print('Parabens o numero é positivo.')
        break