#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

lista = [ ]
for c in range(1, 5):
    lista.append(input(f'Digite o nome do {c}° aluno: '))
print(f'O aluno escolhido foi {choice(lista)}')

