'''23. Escreva um programa que converta uma quantia em reais para dólares.'''

real=float(input("Digite o valor em reais: "))
cotacao=5.39
dolar=real/cotacao
print(f"O valor de R${real} é igual a ${dolar:.2f}.")