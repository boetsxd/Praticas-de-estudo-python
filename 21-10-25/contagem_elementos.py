"""
4. Contagem de Elementos: Crie uma lista com 10 números, onde alguns se repetem. 
Use um loop for para contar quantas vezes cada número aparece e armazene essa contagem em um dicionário.
"""

lista_num = [1, 5, 2, 1, 5, 3, 1, 4, 5, 2]
contagem = {}

for numero in lista_num:
    if (numero in contagem):
       contagem[numero] += 1
    else:
        contagem[numero] = 1
        
print(contagem)
