#Praticando com while

'''
soma de uma sequência de números dado pelo usuário:
variável soma, que vai lendo todos os números e somando: soma

pegar o valor e colocar dentro de um while;
Condição: sequência de valores terminada por zero;
Precisa definir o valor inicial de soma, que será o elemento neutro 0


print("Olá. Por favor digite uma sequência de valores terminado por zero.")

soma = 0

while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores digitados e: ", soma)

em while o valor não foi definido, só após a condição ela é definido e isso gera um erro.

Solução: uma forma é definido um valor maior que zero, por ex: valor = 1


'''

print("Olá. Por favor digite uma sequência de valores terminado por zero.")

soma = 0
valor = 1


while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores digitados e: ", soma)
