def fatR(n):
    ''' (int) -> int '''
    if n == 0:
        return 1
    else:
        return n * fatR(n-1)

# testes
print("Fatorial de 0: ", fatR(0))
print("Fatorial de 1: ", fatR(1))
print("Fatorial de 3: ", fatR(3))
print("Fatorial de 100: ", fatR(100))


