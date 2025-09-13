'''21. Escreva um programa que calcule a distância entre dois pontos.'''

x1=float(input("Digite x1: "))
y1=float(input("Digite y1: "))
x2=float(input("Digite x2: "))
y2=float(input("Digite y2: "))
distancia=((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"A distância entre os pontos é: {distancia:.2f}")

