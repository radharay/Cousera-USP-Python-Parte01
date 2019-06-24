# Variáveis Booleanas - indicadores de passagem

# exemplo:

decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))
valor = 1

while valor != 0 and decrescente:
  valor = int(input("Digite o próximo numero da sequência: "))
  if valor > anterior:
        decrescente = False
  anterior = valor


if decrescente:
    print("A sequência está em ordem Decrescente :)")
else:
    print("A sequência não está em ordem Decrescente :(") 
