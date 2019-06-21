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


#agora vamos praticar com multiplicação ao invés de soma

''' 
Precisamos mudar a variável e ela não pode iniciar por zero, ou o resultado sempre será zero.
exemplo: produto = 1
e a condição será o tamanho da sequência definida pelo usuário

'''
tamanho = int(input("Digite o tamanho da sequencia de números: "))
produto = 1
i = 0


while i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("A soma dos valores digitados e: ", produto)