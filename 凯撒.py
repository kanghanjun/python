# codinng=utf-8
x = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
y = 'n o p q r s t u v w x y z a b c d e f g h i j k l m'.split(' ')
X = map(lambda x: x.upper(), x)
Y = map(lambda x: x.upper(), y)
dict_kaisa = dict(zip(x + X, y + Y))  # 创建一个字典, 键为原字符串, 值为加密字符串
 
 
# 定义凯撒加密函数, 输入字符串, 输出凯撒加密后字符串
def kaisa(string):
    result = []
    for i in range(len(string)):
        if string[i] in dict_kaisa.keys():
            result.append(dict_kaisa[string[i]])
        else:
            result.append(string[i])
    return ''.join(result)
 
 
print(kaisa('The Zen of Python'))  # 结果为Gur Mra bs Clguba
