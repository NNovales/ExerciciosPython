# DESAFIO 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print(f'''
    O tipo primitivo desse valor é: {type(n)}
    Só tem espaços? {"Sim" if n.isspace() else "Não"}
    É um numéro? {"Sim" if n.isnumeric() else "Não"}
    É alfabético? {"Sim" if n.isalpha() else "não" }     
    É alfanúmerico? {"Sim" if n.isalnum() else "Não"}
    Está em maiúsculas? {"Sim" if n.isupper() else "Não"}
    Está em Minúsculas? {"Sim" if n.islower() else "Não"}
    Está capitalizada? {"Sim" if n.istitle() else "Não"}
''')