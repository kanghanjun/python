n = int(input(''))
x,y=0,1
z = 0
while z<=n:
    x,y=x+y,x
    z += 1
print(x)
