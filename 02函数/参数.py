# 给形参
# 调用的是传实参
"""
对于形参和实参，如果原本是不可变对象，那就是传递的值
如果原本是可变对象，那么传递的就是地址
"""
a = 1
b = 2
# 注意在函数内部，对形参的改变，不会影响实参，因为这些都是值传递
def add(a, b):
    a + 1
    return (a + b)

c = add(a, b)
print(a, b, c)

# 注意这里，a和c都是同一个对象，传递的是地址
a=[1,2,3]
def update(a):
    a.append(4)
    return a
c = update(a)
print(a, c)


# 参数
# 必选参数：定义了几个参数，调用的时候必须传几个参数
# 默认参数：可以在定义函数的时候，给参数一个默认值，调用的时候可以不传这个参数，默认使用这个默认值，有则更新，没有则使用默认值
def add(a, b=4):
    return a + b
print(add(1))
print(add(1, 2))
# 可变参数，可变个数，然后将元素放在元组中
def add(*args):
    return sum(args)
print(add(1,2,3,4,5))
# 命名关键字参数，这里需要在调用的时候，在实参中传入一组键值对的形式的数据，如图
def add(a, b, **kwargs):
    print(kwargs)
add(1, 2, c=3, d=4)
# 只有一个，可以看到打印的类型就是一个字典
def add(**kwargs):
    print(type(kwargs))
    print(kwargs)
add(name="zhangsan", age=18)

# 可以在定义的时候，命名关键字
# 这样调用的时候必须要用定义的名字进行传数据
def add(grade, *, name = "lisi", age=12):
    print(name, age)
add("grade1", name="zhangsan", age=18)
add("grade1")
print("=======*args, **kwargs========")
# 关键字参数前面可以是可变长参数
def add(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
add(1,2,3,4,5,6,7,8,9,10, name="zhangsan", age=18)
add(1)
print("=============")
def add(*args, name="lisi", age=12):
    print(args, type(args))
    print(name,age)
add(1,2,3,4,5,6,7,8,9,10, name="zhangsan", age=18)
add(1)

