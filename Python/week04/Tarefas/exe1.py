'''
Escreva um programa que receba um número natural nn na entrada e imprima n!n! (fatorial)
na saída.

Exemplo:

Digite o valor de n: 5
120

'''

numero = int(input('Digite o valor de n: '))

fatorial = 1

while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1

print(fatorial)