L = []
for a in range(0,10):
 for b in range(0,10):
  for c in range(0,10):
   if a**3+b**3+c**3==a*100+b*10+c:
    if a>0:
     L.append(str(a)+str(b)+str(c))
print(','.join(L))
