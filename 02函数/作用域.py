# 内置名称空间：随着python启动而创建，停止而回收，如一些内置函数

# 全局名称空间：随着所在执行文件的执行开始而创建，执行结束而回收

# 局部名称空间：函数中的内容，如函数的参数等

# 全局作用域：包含内置名称空间和全局名称空间
# 局部作用域：局部名称空间

# python查找变量的顺序：局部、全局、内置

a=200
def func():
    a=100
    print(a)
def func2():
    print(a)
func()
func2()
# 方法中的局部变量如果和全局变量重名，那么方法中使用的只是局部变量，不会修改全局变量
# 如果变量是不可变变量，如果想要修改全局变量，需要使用global关键字，如下面这个例子
a=200
def func():
    global a
    a=100
    print(a)
def func2():
    print(a)
func()
func2()
# 如果是不可变对象，就不需要

print("-------------")
# nonlocal
a=300
def func():
    a=200
    def func2():
        # 这里使用了nonlocal关键字，表示使用外层函数的a变量
        nonlocal a
        a=100
        print("three", a)
    func2()
    print("two", a)
func()
print("one", a)

# 匿名函数：lambda 变量：函数体
def func(a,b):
    return a+b
print(func(1,2))
#修改为匿名函数
func = lambda a,b:a+b
print(func(1,2))

# 内置函数
import builtins
print(dir(builtins))

# list tuple
a="123"
print(list(a))
print(type(list(a)))
print(tuple(a))
print(type(tuple(a)))

# abs
print(abs(-1))

# set
a={1,2,3,4,2,3,8,9,10}
print(set(a))
print(type(set(a)))

# zip 拉链，将两个列表拉链成一个列表，一一对应
a=[1,2,3,4]
b=[5,6,7,8]
print(list(zip(a,b)))

# 当拉链的对象个数不一致的时候，按最短的计算
a=[1,2,3,4]
b=[5,6,7]
c=["a","b","c","d"]
print(list(zip(a,b,c)))

# map(函数，可迭代对象) 就是将可迭代对象中的每个对象执行对应的函数，并返回一个迭代器
a=[1,2,3,4]
def func(x):
    return x*x
# 对a中的每个元素执行func函数，最后返回一个迭代器
print(list(map(func,a)))

# 将上面的例子再用lambda函数来写
print(list(map(lambda x:x*x,a)))

# reduce 累计函数，将可迭代对象中的前某对象执行对应的函数生成一个值，然后继续和下某几个对象执行对应的函数，直到遍历完所有对象

from functools import reduce
a=[1,2,3,4]
def func(x,y):
    return x+y
print(reduce(func,a))
# 将上面的例子再用lambda函数来写
print(reduce(lambda x,y:x+y,a))

# enumerate 方法举例
# 可以遍历拿到每个元素的索引和值
a=["a","b", "c"]
for i,j in enumerate(a):
    print(i,j)
print(list(enumerate(a)))
print(dict(enumerate(a)))


# 函数的拆包
#
def func():
    return 1,2,3
a,b,c=func()
# 不拆包就是返回一个元组，拆包后返回到对应为止
print(a,b,c)
print(func())

# 再举一个复杂的
def func():
    return 1,[1,2],{"name":"zhangsan"}
a,b,c=func()
print(a,b,c)
print(func())

# 拆包
# 根据可以确定长度的先赋值，然后不确定的都给b
li = [1,2,3,4,5,6,7,8,9]
a,*b,c=li
print(a,b,c)

# 字典拆包，只赋值了key
d={"name":"zhangsan","age":18,"sex":"male"}
a,b,c=d
print(a,b,c)