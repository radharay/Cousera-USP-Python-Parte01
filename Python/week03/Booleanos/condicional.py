'''
if condição:
    comando

ex
'''
temp = 102

if temp > 100:
   aguaFerve = True

print(aguaFerve)
#True

if temp > 100:
   aguaFerve = True
   evaporação = "Muito rápida"

print(evaporação)
#'Muito rápida'

#condição verdadeira e false if...else

tempoDeJogo = int(input("Quanto tempo temos já jogado? "))

if tempoDeJogo <= 90:
  print("Ainda tem jogo pela frente")
  print("Que bom, eu adoro jogar The Sims")
else:
  print("Putz, o jogo está acabando!")



'''
fazer programa que calcula as raízes de uma equação de segundo grau.

Receber três valores a, b e c

e delta é menor que zero você vai dizer que não tem raízes reais, 
se delta igual a zero você vai dizer que tem uma raiz real que é tal, 
se delta for maior que zero, você vai dizer que tem duasraízes reais que são: tal e tal.


'''
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - (4* a* c)

if delta == 0:
  raiz1 = (- b + math.sqrt(delta)) / (2 * a)
  print("A unica raiz é ", raiz1)
else:
    if delta < 0:
      print("Essa esquação não possui raízes reais.")
    else:
      raiz1 = (- b + math.sqrt(delta)) / (2 * a)
      raiz2 = (- b - math.sqrt(delta)) / (2 * a)
      print("A primeira raíz é : ", raiz1)
      print("A segunda raíz é : ", raiz2)

   

  