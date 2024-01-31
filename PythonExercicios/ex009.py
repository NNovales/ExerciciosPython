#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para ver sua tabuada: '))
for n in range(0, 11):
    print(f'{num} x {n:2} = {num*n}')