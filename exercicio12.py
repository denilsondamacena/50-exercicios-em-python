'''12. Crie um programa que troque os valores de duas variáveis.'''

x=input("Digite um valor para X: ")
y=input("Digite um valor para Y: ")

temp=x
x=y
y=temp

print(f"Agora X={x} e Y={y}")