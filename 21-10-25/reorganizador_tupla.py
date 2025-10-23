""" 
5. Reorganizador de Tupla: 
Crie uma tupla com 5 nomes. 
Converta essa tupla para uma lista, peça ao usuário para inserir um nome na posição que ele desejar (índice), e então converta a lista de volta para uma tupla. 
Imprima a tupla final.
"""

tupla = ('Ana', 'bruno', 'carlos', 'diego', 'elaine')

lista = list(tupla)

valor = input("Informe o nome a inserir: ")
indice = int(input("Informe a posição desejada para inserir: "))

lista.insert(indice, valor)

tupla = tuple(lista)

print(tupla)
