#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

days = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

print(f'O total a pagar é de R${(days*60)+km*0.15:.2f}')