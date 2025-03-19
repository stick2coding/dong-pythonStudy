# 代码复用
# 独立功能的代码块
# 可以在各个地方调用
"""
函数和方法的区别
1、函数可以直接调用，但是方法只能通过对象来调用
2、函数和类无关，但是方法只能定义在类中
"""
# 查看关键字
# import keyword
# print(keyword.kwlist)
help("keywords")

# 定义，函数名的要求
# 函数名只能是字母、数字、下划线，
# 不能有空格，不能有特殊符号，不能有中文，不能有数字开头，不能有数字结尾
# 不能有关键字
# 尽量不要用下划线开头
# 规范：小写
def hello():
    print("hello")
    print("world")

# 调用
hello()

# 函数说明文档
import random
# 通过help来查看函数说明文档
# help(random)
# help(random.randint)

# 也可以通过doc来查看函数说明文档
print(random.__doc__)
print(random.randint.__doc__)