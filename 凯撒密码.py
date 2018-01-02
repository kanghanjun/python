L1=list(range(65,91))
L2=list(range(97,123))
Str = input('')
k = 3
s=[]
LL=s.append
for x in Str:
    a=ord(x)
    if a in L1:
        LL(chr(L1[(a-91+k)%26]))
    elif a in L2:
        LL(chr(L2[(a-123+k)%26]))
    else:
        LL(x)
print(''.join(s))
