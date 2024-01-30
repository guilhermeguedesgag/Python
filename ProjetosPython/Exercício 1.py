def main():
    n = int(input("Digite o valor de n: "))
    i = 1
    n_fat = 1

    while i <= n:
        n_fat = n_fat * i
        i = i + 1

    print("%d" % n_fat)

main()