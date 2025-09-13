'''11. Escreva um programa que calcule o IMC (Índice de Massa Corporal).'''

peso=float(input("Digite o peso: "))
altura=float(input("Digite a altura: "))
imc=(peso/(altura*altura))
print(f"O IMC é de {imc:.2f}")