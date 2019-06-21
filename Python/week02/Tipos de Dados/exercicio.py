'''
Exercício 1
Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:
perímetro: 12 - área: 9

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez
'''
quadrado = int(input("Digite o valor correspondente ao lado de um quadrado: "))

perimetro = quadrado * 4
area = quadrado * quadrado


print("perímetro:",perimetro,"- área:",area)

#Exercicio 02

'''
Exercício 2
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

Entrada de Dados:
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

Saída de Dados:
A média aritmética é 5.5
'''
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))

media = (n1 + n2 + n3 + n4) / 4

print("A média aritmética é ", media)