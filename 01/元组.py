# 元组和列表最大的区别就是元组无法被修改，元组就是tuple
a = (1,2,3)
print(a)
# 元素不能被修改，也不能被删除
# 权限只读
# a和b是一样的，c才是元组
a=(10)
print(type(a))
b=10
print(type(b))
c=(10,)
print(type(c))

# index 和 count 和列表一样