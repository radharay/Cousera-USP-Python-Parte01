'''
Exercício 1
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:

Digite um número inteiro: 13
primo

Digite um número inteiro: 12
não primo
'''


#n = int(input("Digite um número inteiro: "))
#n primo só tem dois divisores. O 1 e ele mesmo.
#  que o resto será 0 ex: 5%1==0 e 5%5==0

def ePrimo (x):
  fator = 2
  while x % fator != 0 and fator <= x/2:
      fator = fator + 1 
  if x % fator == 0:
    return False
  else:
    return True

n = int(input("Digite um número inteiro: "))

while n > 0:
  if ePrimo(n):
    print('primo')
    break
  else:
    print('não primo')
    break


