'''39. Crie um programa que simule um sistema de login.'''

usuario_correto="admin"
senha_correta="1234"

print("=== Sistema de Login ===")
usuario= input("Digite o usuário: ")
senha= input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")
