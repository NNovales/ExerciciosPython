#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Qual é o salário do funcionário? R$'))
print(f'Um funcionário que ganhava R${salary:.2f}, com 15% de aumento, passa a receber R${salary+(salary*0.15):.2f}')