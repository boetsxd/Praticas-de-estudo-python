"""
2. Lista de Compras Interativa: 
Comece com uma lista de 3 itens de compra. 
Usando um loop while, pergunte ao usuário se ele quer adicionar um item, remover um item ou visualizar a lista. 
O loop só deve parar quando ele digitar "sair".
"""

lista_compra = ["pão", "presunto", "queijo"] 

while True:    
    opcao = input(" Digite 'adicionar' para inserir itens\n Digite 'remover' para remover itens\n Digite 'visualizar' para Listar itens\n Digite 'sair' para encerrar\n").lower().strip()
    
    if(opcao == 'adicionar'):
        lista_compra.append(input("informe um item para adicionar à lista: \n"))
    elif(opcao == 'visualizar'):
        print(f'{lista_compra}\n')
    elif(opcao == 'remover'):
        lista_compra.remove(input("Informe o item a ser removido: \n"))
    elif(opcao == 'sair'):
        break
    else:
        print("Opção inválida!")