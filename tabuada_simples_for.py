numero = int(input("Informe um número de 1 a 10: "))
operador = input("Informe o operador a ser utilizado: +, -, *, / ou % )")

if operador == '+':
    for valor in range(1, 11):
        print(f'{valor} + {numero} = ', valor + numero)
elif operador == '-':
    for valor in range(1, 11):
        print(f'{valor} - {numero} = ', valor - numero)
elif operador == '*':
    for valor in range(1, 11):
        print(f'{valor} * {numero} = ', valor * numero)
elif operador == '/':
    for valor in range(1, 11):
        print(f'{valor} / {numero} = ', valor / numero)
elif operador == '%':
    for valor in range(1, 11):
        print(f'{valor} % {numero} = ', valor % numero)
else:
    print("Opção inválida!")