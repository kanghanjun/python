def main():
    input_string=input("请输入您的食材，用逗号隔开")
    input_list = input_string.split(',') 
    result = []
    for i in input_list:
        for j in input_list:
            if i != j:
                result.append(i + j)
 
    for i in result:
        print(i)
 
main()
