'''
Exercício 2
Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais.
Para a saída, siga o formato do exemplo abaixo.

Exemplo:

Digite o valor de n: 5
1
3
5
7
9

'''

n = int(input('Digite o valor de n: '))

contador = 0
#primeiro numero impar
impar = 1 

while contador < n:
    print(impar)
    contador = contador + 1
    impar = impar + 2
    
