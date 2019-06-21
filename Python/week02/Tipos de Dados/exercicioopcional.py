'''
Nesta lista de exercícios vamos praticar os conceitos vistos até agora. Cada exercício deve ser resolvido em um arquivo separado e a seguir enviado através da web. A correção automática pode demorar alguns minutos. Você pode submeter a mesma resposta mais de uma vez.

Note que a correção verifica se o resultado corresponde exatamente ao que foi pedido no enunciado. Letras maiúsculas ou minúsculas, número de espaços e pontuação diferentes do pedido são tratados como erro.

Exercício 1
Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:


Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
'''

nomeCliente = input("Digite o nome do cliente: ")
diaVencimento = int(input("Digite o dia do vencimento: "))
mesVencimento = input("Digite o mês do vencimento: ")
valor = float(input("Digite o valor da fatura: "))

nome = nomeCliente.title()
mes = mesVencimento.title()

print("\n Olá, ", nome, "\n A sua fatura com vencimento em ", diaVencimento, "de ", mes, "no valor de R$ ", valor, "está fechada.")

#Utilizei title() para deixar a primeira letra maiúscula, mesmo colocando menúscula.
#E \n quebra de linha