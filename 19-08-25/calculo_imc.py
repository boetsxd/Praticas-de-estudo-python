#criar um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa e classifique o resultado.
import math

peso = int(input("Informe seu peso em KG: "))
altura = float(input("Informe sua altura: "))

imc = peso / math.pow(altura,2)

if imc < 18.5:
    print("Abaixo do peso")
elif (imc >= 18.5) and(imc < 25):
    print("Peso normal")
elif (imc >= 25) and(imc < 30):
    print("Sobrepeso")
elif imc >= 30: 
    print("Obesidade")
else:
    print("Valores inválidos!")

print(f'Índice de massa corporal: {imc:.2f}')