#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem na carteira? R$: '))
print(f'Com R${real} você pode comprar US${real/4.97:.2f} doláres') 
