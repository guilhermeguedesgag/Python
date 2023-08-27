from random import choice, choices, sample

repeticao=1
while (repeticao ==1):
    print("Quantos digitos você quer na senha?")
    tamanhodasenha = int(input())
    print("Quais caracteres?")
    caracteres = input()
    senha_segura = " "
    for i in range(tamanhodasenha):
        senha_segura += choice(caracteres) #choice método de sorteio

    print("Senha gerada: " ,senha_segura) #ele irá printar a escolha dos dados em caracteres

    repeticao=int(input("Deseja criar outra senha? Tecle: 1 para Sim - 2 para Não:"))
    print(" ")