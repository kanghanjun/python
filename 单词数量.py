# 初始化 处理 输入的数据
inputstr = input()
inputstr = inputstr.lower()
lst = (inputstr).split(' ')

#使用字典存储,出现的字母的次数
dit = {}
max = 0
maxkey = ""

for item in lst:
    if (dit.get(item, 0)):
        dit[item] = dit[item] + 1
    else:
        dit[item] = 1
    #每次判断寻找最大值和字母
    if (dit[item] > max):
        max = dit[item]
        maxkey = item

print(maxkey)
