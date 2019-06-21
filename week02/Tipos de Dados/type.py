#Tipos de dados

10
#qual é o tipo desse valor type(10)

print (type(10))
#Tipos de dados

10
#10

print(type(10))

'''var = input("Digite algo: ")

tipo=(type(var))

print("O tipo de " ,var, "é " ,tipo, ".")'''

print(type(50.50))



print(type("tudo bem?"))

#eu posso ter obj interio e String

5 / 2
print(type(5/2))
#float (fracionado)

10 / 3
print(10 / 3)
#sabe o resultado da / inteira
print(10 // 3)
#o resto da divisão %
print(10 % 3)

peso = 78
altura = 1.83

IMC = peso /(altura ** 2)
print(IMC)
print(type(IMC))

#conversão entre tipos float para inteiro

IMCInteiro = int(IMC)
print(IMCInteiro
)

#string 
tx = "Bom dia, tudo bem?"

#tamanho do tx
print (len(tx))

#tamanho de um número

#len(IMC)
#erro

#pode converter para string 

temp = str(IMC)

print(len(temp))

print (len(str(IMC)))

#entrada de dados

#Fahrenheit para Celsius

temperaturaFahrenheit = 78

temperaturaCelsius = int((temperaturaFahrenheit - 32) * 5 / 9 )

print("A temperatura em Celcius é ", temperaturaCelsius)

#perguntar a temperatura

#entrada do usuário função input

temperaturaFahrenheit = input("Digite uma temperatura em Fahrenheit: ")
#temf = float(temperaturaFahrenhe38
temperaturaCelsius = (float(temperaturaFahrenheit)- 32) * 5 / 9 

print("A temperatura em Celcius é ", temperaturaCelsius)

cidade = input("Qual o nome da sua cidade? ")
estado = input("Qual é o seu estado? ")

print("Você é da cidade de ", cidade, "e do estado de ", estado, ".")


segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")
