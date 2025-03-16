#print输出，input输入
# 会将用户的输入全部按照字符串处理
# input会等待用户输入，没有输出就一直等待不会往下执行
# input("input waiting:")
print("input over")


# 接收输入的内容
name = input("input waiting:")
print(name, "类型是：", type(name))

# 需要数字就需要类型转换
num = int(input("input waiting:"))
print(num, type(num))