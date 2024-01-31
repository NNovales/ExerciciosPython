#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Uma distância em metros: '))
print(f'A medida de {medida}m corresponde a {medida*100:.0f}cm e {medida*1000:.0f}mm')