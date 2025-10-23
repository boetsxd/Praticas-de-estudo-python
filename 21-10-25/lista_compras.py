"""
2. Lista de Compras Interativa: 
Comece com uma lista de 3 itens de compra. 
Usando um loop while, pergunte ao usuário se ele quer adicionar um item, remover um item ou visualizar a lista. 
O loop só deve parar quando ele digitar "sair".
"""

lista_compra = ["pão", "presunto", "queijo"] 

while True:      # o .lower(para trazer todo texto par aminúsculo) .strip(p/ limpar espaços) vem para ajustar as entradas às posibilidades do usuário
    menu = """
    Digite 'adicionar' para inserir itens 
    Digite 'remover' para remover itens 
    Digite 'visualizar' para Listar itens 
    Digite 'sair' para encerrar
    """
    opcao = input(menu).lower().strip()
    
    if(opcao == 'adicionar'):
        lista_compra.append(input("informe um item para adicionar à lista: \n"))
    
    elif(opcao == 'visualizar'):
        print(f'{lista_compra}\n')
        
    elif(opcao == 'remover'): #O método .remove() é sensível, caso o iem solicitado não esteja na lista pode gerar erro. Um if/else pode ajudar
        item_remover = input("Informe o item a ser removido: \n")
        
        if item_remover in lista_compra:
            lista_compra.remove(item_remover)
        else:
            print(f"Erro: '{item_remover}' não está na lista.")
    
    elif(opcao == 'sair'):
        break
   
    else:
        print("Opção inválida!")