# texto= " OI"
# # print(texto)
# len(texto)
#*********************************SEgue abaixo o conteúdo da 2 semana
# temperaturaFahrenheit = 40
#
# temperaturaCelsius = (temperaturaFahrenheit - 32)* 5 // 9
#
# print("A temperatura em Celsius é ", temperaturaCelsius)

#*********************************Como colocar o input( ou seja a entrada de dados#####
# temperaturaFahrenheit = input("Digite uma temperatura em fahrenheit: ")
# temp = int(temperaturaFahrenheit) # Aqui coloquei  a "temp= "para guardar o dado que coloquei no INPUT  e
# coloquei "float" para dar um dado com número quebrado)

# temperaturaCelsius = (temp - 32)* 5 // 9
# # print("Sua temperatura em Celsius é ,",temperaturaCelsius)
# x=input("Qual é a idade?")

#*************************************PROGRAMA QUAL É O VALOR######
# a = int(input("Qual o valor de a? "))
# b = int(input("Qual o valor de b? "))
# aux = a
# a = b
# # b = aux
# # print(a)
# print(b)

#*************************************Exercício 1

# valordoladodoquadrado = int(input("Digite o valor correspondente ao lado de um quadrado: "))
# temp = (valordoladodoquadrado)
# perimetro = temp * 4
# area = temp * temp
#
# print("perímetro : ", perimetro, "- área: ",area,)

#***********************************Exercício 2
# primeiranota = float(input("Digite a primeira nota? "))
# segundanota = float(input("Digite a segunda nota? "))
# terceiranota = float(input("Digite a terceira nota? "))
# quartanota = float(input("Digite a quarta nota? "))
# media = (primeiranota + segundanota + terceiranota + quartanota) / 4
# print("A média aritmética é ",media)

#******************************* Exécicios Opcionais : Exercício 1


# nomedocliente = input("Nome do cliente: ")
# diadevencimento = int(input("O dia de vencimento: "))
# mesdevencimento = input("O mês de vencimento: ")
# valordafatura = str(input("Valor da fatura: "))
# print("Olá,", nomedocliente)
# print("A sua fatura com vencimento em", diadevencimento,"de", mesdevencimento,"no valor de R$", valordafatura,"está ")
# print("fechada.")

#**************************************Exercício 2
# numerodesegundos = int(input("Por favor, entre com o número de segundos
#                        que deseja converter: "))  # entrada deve ser str
# dias = numerodesegundos//86400  # Aqui o resultado foi 2,06730324
# segundosrestan = numerodesegundos % 86400  # o
# # símbolo % : significa pegar o resto
# horas = segundosrestan // 3600  # Aqui pegou
# # o resto 0,06730324 e dividiu por 3600
# segundrestodossegun = segundosrestan % 3600  # Aqui o resultado foi 0,0000187
# minutos = segundrestodossegun // 60  # Pegou o 0,0000187 e dividiu por 60
# restsegunfinal = segundrestodossegun % 60
# print(dias, "dias,", horas, "horas,", minutos, "minutos e",
#       restsegunfinal, "segundos.")
#
#
# #************************************************************************************************
# #  EXERCICO 3 FEITO : Faça um programa em Python que recebe um número inteiro e
# #  imprime seu dígito das dezenas. Observe o exemplo abaixo:
#
# numerointeiro = int(input("Digite um número inteiro: "))  # testar 178615
# dezena = int(numerointeiro % 2)
# print("O dígito das dezenas é", dezena)
# numerointeirooo = int(input("Digite um número inteiro: "))
# digitouonumerointeiro = numerointeiro
# dezenhadd = int(digitouonumerointeiro % 1)
# print("O digito das dezenas é:", dezenhadd)



