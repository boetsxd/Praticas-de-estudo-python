import random

numero_secreto = random.randint(0,100)
tentativa = -1 # Inicializando a variável fora do range, para iniciar o loop while

while (tentativa != numero_secreto):
    tentativa = int(input("Informe um número: "))
    if(tentativa < numero_secreto):
        print("Número baixo, tente um valor maior!\n")
    elif (tentativa > numero_secreto):
        print("Número alto, tente um valor menor!\n")
    else:
        print("Acertô miserávi!")
        print(f'número aleatório era: {numero_secreto}')
