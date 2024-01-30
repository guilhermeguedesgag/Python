'''Semana 4 do curso de python'''
# Imprimindo as potências de 2

# print(2**0)  # ou seja, estou mandando imprimir 2 elevado a 0 (zero)
# print(2**1)  # como todos sabem todo numero elevado  a 0 ( zero) é 1
# print(2**2)
# print(2**3)
# print(2**4)
# print(2**5)
# print(2**6)
# print(2**7)
# print(2**8)
# print(2**9)
# print(2**10)
# print(2**11)
# print(2**12)
# print(2**13)
#                                 E X P L I C A N D O   W H I L E

# while NomedaCondiçãoaserexecutad : ---# while verifica verdadeiro ou falso(boleanas)
#     EscreveAquiPrimeiraOrdem  ----# enquanto o "NomedaCondiçãoaserexecutad" for verdadeiro executa a "EscreveAquiPrimeiraOrdem"...
#     EscreveAquiaSegundaOrdem  ----#... e executa a     "EscreveAquiaSegundaOrdem "

# seFALSAexecutaessa  ---- # "NomedaCondiçãoaserexecutad" for falsa executa a  "seFALSAexecutaessa "

#                      TESTANDO WHILE NA REAL

# sequencia = 1
# while sequencia <= 10 :
#     print(sequencia + 1) #------ PASSO A : Ele somou : 1(sequencia) + 1 = 2
#     sequencia = sequencia + 1 # ----PASSO B : Aqui a (sequencia) estava valendo 2 e depois do " = " ficou : 2(sequencia) + 1 = 3...
# print("Acabou, estuda mais") #...---- PASSO C : Depois sequencia passou a valer 2 e retorna para PASSO A.

# TESTE B #

# print("Digite uma sequencia de valores terminada em zero.")
# soma = 0
#
# valor = 1
# while valor != 0: # Ou seja digite um valor diferente( != ) de 0(zero)
#     valor = int(input("Digite um valor a ser somado: ")) # o " input por padrão sempre devolce um "string"
#     soma = soma + valor # Ou seja WHILE vai guardando na memória o valor de 'soma'
#
# print( " A soma dos valores digitados é" , soma)

#TESTE C

# i = int(input(""))
# produto = 1
#
# valor = 1
# while valor != 0: #----- PARTE A : Ou seja digite um valor diferente( != ) de 0(zero)
#     valor =int(input("Digite um valor a ser somado: "))  #PARTE B : o 'input por padrão sempre devolce um 'string'
#     produto = produto * valor #----- PARTE C: Enquanto o valor digitado na "PARTE B" não for diferente de 0(zero),a fórmula...
#                               #---- ...não seguirá para a PARTE D, irá retornar para "PARTE A" e considerar o valor
#   #-------- do campo "valor"como sendo o último digitado na "PARTE B"
# print(" A soma dos valores digitados é", produto)#----- PARTE D :

# Teste D
x = 6532
print(x % 3)
print(x % 1000)
print( x// 10)



