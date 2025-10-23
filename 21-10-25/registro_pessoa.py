"""
3. Registro de Pessoa: 
Peça ao usuário para inserir o nome, idade e cidade dele. 
Armazene essas três informações em uma tupla e depois crie um dicionário onde as chaves são "nome", "idade" e "cidade", e os valores são os da tupla. 
Imprima o dicionário completo.
"""

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
cidade = input("Informe sua cidade: ")

informacoes = (nome, idade , cidade)

dados_pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

print(dados_pessoa)

