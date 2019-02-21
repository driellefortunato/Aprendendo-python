def seg_maxR(v, ini, fim):
   ''' (list, int, int) -> int, int, int
   Recebe uma lista v e um intervalo ini,fim e retorna
   e, d e smax onde v[e:d] eh fatia de soma maxima, com soma smax
   '''

   if ini >= fim:  # zero elementos
      return 0
   if ini+1 == fim: # um elemento
      return v[ini]
   meio = (ini + fim)//2

   # soma maxima cruzada a esquerda
   emax = s = 0
   e = m-1
   for i in range(m-1, ini-1, -1):
       s += v[i]
       if s > lmax:
           emax, e = s, i

   # soma maxima cruzada a direita
   dmax = s = 0
   d = m
   for i in range(m, fim):
      s += v[i]
      if s > lmax:
         lmax, d = s, i


   maxc = emax + dmax
   maxe = seg_maxR(v, ini, m)
   maxd = seg_maxR(v, m, fim)

# teste da funcao
v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print(seg_maxR(v))
