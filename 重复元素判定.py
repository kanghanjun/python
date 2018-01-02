L = eval(input(''))
L1 = [i for i in L if L.count(i)>1]
if L1:
    print(True)

else:
    print(False)
