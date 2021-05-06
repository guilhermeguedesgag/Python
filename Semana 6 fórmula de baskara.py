import math
# O import math serve para importar a fórmula da raiz quadrada
def delta(a, b, c):  # Serão 3 valores no delta
    return b ** 2 - 4 * a * c   # B ao quadrado(**) menos 4 vezes(*) a vezes(*) c.

def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(delta(a, b, c))) / (2*a)
        print("A única raiz é: ", raiz1)
    else:
        if d < 0:
            print("Esta equação não possui raizes reais ")
        else:
            raiz1 = (-b + math.sqrt(delta(a, b, c))) / (2*a)
            raiz2 = (-b -math.sqrt(d)) / (2*a)
            print("A primeira raiz é : ", raiz1)
            print("A segunda raiz é : ", raiz2)

