# 引用传递

# id是查看变量的内存地址
a = 10
b = 10
c = a
print(id(a))
print(id(b))
print(id(c))
# 当两个变量的数值相同的时候，他们共用一个内存空间，b没有重新分配内存，直接用了a的内存地址


# 列表同理，如果值相同，那么地址也相同

"""
下面讲拷贝
"""
# 通过拷贝，拷贝出来的变量，是两个不同的变量，但是值相同
import copy
a = [1,2,3]
b = copy.copy(a)
print(a==b)
print(id(a))
print(id(b))