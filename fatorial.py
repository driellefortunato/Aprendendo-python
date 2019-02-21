def main():
    ''' Exemplo de programa com funcoes em Python
    '''

    n = int(input("Digite um numero inteiro: "))
    if n >= 0:
       f = fatorial(n)
       print("O fatorial de (%d) = %d\n"%(n, f))
    else:
       print("Entrada invalida")

#------------------------------------------
def fatorial(n):
    ''' (int) -> int

    Recebe um inteiro n e retorna o valor do fatorial
    de n.
    '''

    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1
    return fat

#------------------------------------------
# inicio do programa: chamada da funcao main()
main()


