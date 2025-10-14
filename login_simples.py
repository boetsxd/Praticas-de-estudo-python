user_secret = "noname"
passw_secret = "6Teste@"

usuario = input ("Informe o nome de usuário: ")
senha = input ("Informe a senha: ")

if ((usuario == user_secret) and (senha == passw_secret)): #troquei o operador "&" pela palavra "and" pela boa pratica Pythônica.
    print("Usuário autenticado com sucesso!")
else:
    print("Usuário ou senha incorreta!")