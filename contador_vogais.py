#criar um programa que recebe uma frase do usuário e conta quantas vogais (a, e, i, o, u) existem nela, ignorando a diferença entre maiúsculas e minúsculas.

frase = input("Digite uma frase: ").lower()

letras = len(frase)

vogais = ["a", "e", "i", "o", "u"]

contador = 0

for caractere in frase:

    if caractere in vogais:
        contador += 1

print(f'O número de vogais encontradas é: ', contador)
print("Número total de letras: ", letras)