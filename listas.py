seq = []
n = int(input("Digite o tamanho da sequencia: "))
for i in range(n):
    num = int(input("Digite o %d inteiro da sequencia: "%(i+1)))
    seq.append(num)

# podemos imprimir a lista no print
print("Lista de entrada: ", end=" ")
print(seq)

# vamos imprimir a lista em ordem reversa
print("Lista reversa: ", end=" ")
for i in range(n-1, -1, -1):
    print(seq[i], end = " ")
print()
