def seg_max2(v):
   ''' (list) -> int, int, int
   Recebe uma lista v e retorna e, d e smax
   onde v[e:d] eh fatia de soma maxima, com soma smax
   '''
   n = len(v)
   smax = e = d = 0
   for i in range(n):
      s = 0
      for j in range(i, n):
         s += v[j]
         if s > smax:
            e, d, smax = i, j+1, s
   return e, d, smax

# teste da funcao
v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print(seg_max2(v))
 
