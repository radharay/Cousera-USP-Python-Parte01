
#Expressões Booleanos

print(5>3)

print(18 == 9 * 2)

x = 123456
print(x < 0 )

print(type(False))

print(type(x > 0))

#and & os dois verdadeiros. 1 false, resultado: false
print( x > 0 and x **2 > 100)
#true

print( x < 0 and x **2 > 100)
#false

# or || verdadeiro se tiver 01 verdadeiro ou ambos

print(x < 0 or x == 123456)
#true

print(x == 124 or x == 5)
#false

#not inverte o valor 

print(not x == 123456)
#False

print(not x == 5)
#True
print(not False)
#True
print(not True)
#False

print( not not True)
#true

#combinações lógicas

fizerSol = True
forFeriado = False
vouParaPraia = fizerSol and forFeriado

print(vouParaPraia)
#False

fizerSol = True
forFeriado = True
vouParaPraia = fizerSol and forFeriado

print(vouParaPraia)
#True 

paitrocinio = False
rolarPromoção = True

vouAoShow = paitrocinio or rolarPromoção

print(vouAoShow)
#true

#Precedencia de operadores 

'''

7(Alto)  = exponenciação    **
6        = multiplicação    *,/,//,%
5        = adição           +,-
4        = relacional       ==,!=,<=,>=,>,<
3        = logico           not
2        = logico           and
1(baixo) = lógico           or

'''
y = 50
soma = x > 0 and not y == 50 or x + y == 150

print(soma)

soma2 = ((x > 0) and (not y == 50)) or (x + y == 150)

print(soma2)