'''26. Escreva um programa que verifique se um número é positivo ou negativo.'''

num=float(input("Digite um número: "))
if num > 0:
    print(f"O número {num} é positivo.")
elif num == 0:
    print(f"O número {num} é neutro.")
else:
    print(f"O número {num} é negativo.")