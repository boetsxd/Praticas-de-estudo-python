soma = 0

for i in range(1, 51):
    if (i % 2 == 0):
        soma = soma + i
        print (f'nº par atual: {i}')
        print(f'acumulado de nº par: {soma}\n')