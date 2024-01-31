#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

num = int(input('Digite um número: '))
raiz_quadrada = math.sqrt(num)
print(f'O dobro de {num} vale {num*2}. \nO triplo de {num} vale {num*3}. \nA raiz quadrada de {num} vale {raiz_quadrada:.2f}.')





