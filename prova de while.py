# x = 1
# while (x < 4):
#     x = x + 1
# print("x vale", x)


# i = 0
# while (i < 5):
#   print (i)
#   i = i + 1

# i = 2
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 2


# count = 0
# while (count < 10):
#      # Ponto A
#      print ("Olá...", count)
#      count =  count + 1
#      # Ponto B
# # Ponto C

#
# i = 6
# while (i > 0):
#     i = i - 3
#     print (i)

# count = 0
# while(count <= 10):
#     print (count, "Olá Mundo!")
#     count = count + 1

# x = 10
# while not (x == 0):
#     x = x-1
#     if x % 2 != 0:
#       print (x)
#
# i = 1
# while i < 10:
#       "iteração"
#       i = i + 1

terminou = False
p = i = 0
while (not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print ("P = ", p)
print ("I = ", i)