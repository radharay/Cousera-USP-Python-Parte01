# par ou ímpar

num = int(input("Por favor, digite um número: "))

resto = num % 2

if resto == 0:
  print("O número", num, "é par.")
else:
  print("O número", num, "é ímpar.")
  


'''
Exercícios 2 - 
Fizz

se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

num2 = int(input("Digite um número: "))

if num2 % 3 == 0 :
   print("Fizz")
else:
   print(num2)

'''
Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

num3 = int(input("Digite um número: "))

if num3 % 5 == 0 :
   print("Buzz")
else:
   print(num3)
   

'''
Exercícios 4 - FizzBuzz parcial, parte 3
Receba um número inteiro na entrada e imprima

FizzBuzz

na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

num4 = int(input("Digite um número: "))

if num4 % 3 == 0 and num4 % 5 == 0:
   print("FizzBuzz")
else:
   print(num4) 

'''
Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente
    
'''

a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))

if a <= b <= c:
  print ('crescente')

else:
  print ('não está em ordem crescente')

  