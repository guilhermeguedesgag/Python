#              Comando DEF
# Comando DEF serve para definir um novo parâmetro

# def soma (x, y, z) : # Lembrando que aki no lugar de x e y poderia ser qualquer valor
#     return x+y+z      # Ou seja aqui ela irá(return) devolder o valor de : x + Y
#
# print(soma(10, 20, 30))
# print(soma(-20, 100, 200))
#
# print(soma(2, 5, 8))
#
# def nome_do_seu_time () :
#     return "SPFC"
#
# print(nome_do_seu_time())
#
# def quieta () :
#     x = 10 + 20
#     print("O valor calculado é ", x)
#
# print(quieta)
#
# print(x)

###Parei em 14:21 (video funções)
### como calcular um calculo fatorial

#--------------------- RESOLUÇÃO DOS TESTES

def fatorial (n) :  # definir o nome da função , que aqui no caso é " fatorial'
    fat = 1 # " fat" é o nome da variável
    while(n > 1 ) : # 1 : Enquanto "n"(nº q vc colocou acima) for maior do que 1...
        fat = fat * n # 2 :... fat( 1 ) será  = fat (1 )x n( número q vc colocou lá em cima)
        n = n - 1 # 3 :... e "n"(nº q vc colocou acima) será = n(nº q vc colocou acima) - 1
    return fat # ... e irá retornar(return) o valor de "fat"


                  # P L A N O    A $$$$
# print(fatorial(5))  # podemos observar aqui q foi printado na tela o fatorial
                    # e também pediu para eu digitar um valor.
                    # ou seja ele gravou na memoria, que uma determinada palavra irá executar uma determinada função

def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))



                     # P L A N O    B $$$$
#  ======== SEGUE ABAIXO UMA FÓRMULA PARA TESTAR A FÓMULA FATORIAL FEITA RECENTEMENTE ***
def testa_fatorial():  # PARTE 1 : definindo(def) a fórmula testa_fatorial( QUE ESTÁ NO PLANO A)
    if fatorial(1) == 1:  # PARTE 2 : Se(if) a fórmula fatorial O DIGITO FOR 1 E O resultado igual a 1
        print("Funciona para 1") # PARTE 3 : ...então deverá "printar" na tela funciona para  1
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        "Funciona para 5"
    else:
        print("Não funciona para 2")




#     QUAL É A DIFERENÇA ENTRE ERROS DE SINTAXE E ERROS DE LÓGICA?
# A - ERROS DE SINTAXE : Ou seja, erros de sintaxe são erros de escrita.
# B - Erros de Lógica : São erros que acontecem na escrita de um código que por consequencia
#acabam ficando com códigos ilógicos. '''
print(numero_binomial(5, 3))