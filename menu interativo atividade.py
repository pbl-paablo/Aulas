while True:
    operacao = input('Digite uma operação: + - * /')
    if operacao == '+':
       numero1 = int(input("Digite o numero que voce deseja somar"))
       numero2 = int(input("Digite o numero que voce deseja somar"))
       print(f"O resultado da sua operação é: {numero1 + numero2}")
       continue

    elif operacao == '-':
       numero1 = int(input("Digite o numero que voce deseja subtrair"))
       numero2 = int(input("Digite o numero que voce deseja subtrair"))
       print(f"O resultado da sua operação é: {numero1 - numero2}")
       continue

    elif operacao == '*':
       numero1 = int(input("Digite o numero que voce deseja multiplicar"))
       numero2 = int(input("Digite o numero que voce deseja multipicar"))
       print(f"O resultado da sua operação é: {numero1 * numero2}")
       continue

    elif operacao == "/":
       numero1 = int(input("Digite o numero que voce deseja dividir"))
       numero2 = int(input("Digite o numero que voce deseja dividir"))
       print(f"O resultado da sua operação é: {numero1 / numero2}")
       continue
       break