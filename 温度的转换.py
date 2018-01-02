#TempConvert.py
for i in range (3):

    val = input("请输入带温度表示符号的温度值（例如： 32c): ")
    if val[-1] in ['C','C']:
        f = 1.8 * float(val[0:-1]) +32
        print("转换后的温度为：%.2fF"%f)
    elif val[-1] in ['F','f']:
        c = (float(val[0:-1]) -32) / 1.8
        print("转换后的温度为：%.2fc"%c)
    else:
        print("输入有误")
    
