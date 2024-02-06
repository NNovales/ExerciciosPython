#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan 
angulo = radians(float(input("Digite o ângulo que você deseja: ")))

print(f"O ângulo de {angulo} tem o SENO de {sin(angulo):.2f} \nO ângulo de {angulo} tem o COSSENO de {cos(angulo):.2f} \nO ângulo de {angulo} tem a TANGENTE de {tan(angulo):.2f}")