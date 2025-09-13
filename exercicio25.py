'''25. Escreva um programa que calcule a hipotenusa de um triângulo retângulo.'''

cateto1=int(input("Digite o valor do primeiro cateto: "))
cateto2=int(input("Digite o valor do segundo cateto: "))
hipotenusa=(cateto1**2 + cateto2**2) ** 0.5
print(f"O valor da hipotenusa é {hipotenusa:.2f}")
