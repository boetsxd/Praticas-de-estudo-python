""" 
6. Gerenciador de Estoque: 
Crie um dicionário que represente o estoque de uma loja (chave: produto, valor: quantidade). 
Usando o input() e if/else, pergunte ao usuário qual produto ele quer comprar e, se houver no estoque (quantidade $> 0$), diminua 1 da quantidade. 
Se não houver, imprima uma mensagem.
"""

estoque = {'cafe':50, 
           'acucar':18, 
           'oleo':25, 
           'arroz':15, 
           'feijao':17, 
           'macarrao':20}

compra = input("Qual produto deseja hoje?: ").lower().strip()

if (compra in estoque and estoque[compra] > 0):
    quantidade = int(input("E qual a quantidade desejada?: "))
    if (quantidade <= estoque[compra]):    
        estoque[compra] -= quantidade
        print("Compra realizada com sucesso!")
        print(f'Estoque atual: {estoque[compra]}')
    else:
        print(f"Quantidade excede o estoque, tente {estoque[compra]}")
else:
    print("item sem estoque!")
