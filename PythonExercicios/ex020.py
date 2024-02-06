#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

lista = []
for c in range(1, 5):
    lista.append(input(f'Digite o nome do {c}° aluno: '))
shuffle(lista)
print(f'A ordem de apresentação será {lista}')