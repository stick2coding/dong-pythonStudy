# \05闭包与装饰器\闭包.py

# 闭包是函数内部定义的函数
"""
1、闭包是嵌套在函数中的函数
2、闭包必须是内层函数对外层函数变量的引用

条件：
1、函数中嵌套一个函数
2、内层嵌套函数，对外层作用域有一个非全局变量的引用
3、外层函数的返回值是内层函数的函数名
"""
# 闭包的模板
# 外层函数
def outFunc():
    # 外层的一个非全局变量
    a = 1
    # 内层函数
    def innerFunc():
        print(a)
        return a + 1
    # 外层函数返回的是内层函数的函数名
    return innerFunc

# 闭包的作用：用于保存局部信息不被销毁，保证数据的安全性
"""
 应用：
1、可以保存一些非全局变量，但是不容易被销毁改变的数据
2、装饰器
3、实现数据锁定
"""

def outer(m):
    n = 10;
    def inner():
        print("执行了inner")
        print(m + n)
    print("执行了outer")
    return inner
out = outer(20)
out()

def outer(n):
    def inner():
        # 拿到外层函数的变量n
        nonlocal n
        n = n + 1
        print("执行了inner")
        print(n)
    print("执行了outer")
    return inner
out = outer(20)
out()

# 装饰器

"""
装饰器，本质上就是个闭包函数，返回的也是一个函数对象

可以让其他函数在不改变代码的情况下，增加额外功能

功能：
1、执行时间统计
2、日志
3、事务
4、权限
5、缓存
"""

# 使用方法
"""
1、先定一个装饰函数
2、再定义业务函数
3、让后用装饰函数包装业务函数

@intro 相当于执行了 a=intro(b)
"""
# 装饰函数，函数的返回值就是参数中的函数被包装后的效果
def wrapper(func):
    def inner(*args, **kwargs):
        print("开始执行")
        func(*args, **kwargs)
        print("执行结束")
    return inner

"""
日志打印器
"""

# 定义日志装饰器
def logger(func):
    def inner(*args):
        print("开始执行", func.__name__)
        func(*args)
        print("执行结束", func.__name__)
    return inner

def loggerFunc(func):
    def inner(*args):
        print("开始执行", func.__name__)
        func(*args)
        print("执行结束", func.__name__)
    return inner

# 定义业务函数
def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

"""
第二种调用方法
使用语法糖@
"""
# 通过@对应的装饰器，来做为业务函数的包装
@loggerFunc
def mul(a, b):
    print(a * b)

# 使用装饰器装饰该函数
add = logger(add)
sub = logger(sub)
# 装饰后再执行
add(1, 2)
sub(1, 2)

mul(1, 2)


# 多层嵌套闭包
def func1(func):
    def func2(a, b):
        print("func2", a, b)
        def func3(c, d):
            print("func3", c, d)
            func(c, d)
        return func3
    return func2

@func1
def func4(a, b):
    print("func4", a, b)

# 多层的嵌套，这里调用的时候也要传多个参数
func4(1, 2)( 3, 4)

# 不定长参数
def wrapper(func):
    def inner(*args, **kwargs):
        print("开始执行")
        func(*args, **kwargs)
        print("执行结束")
    return inner

@wrapper
def func(*a, **b):
    print(a)
    print(b)

# 这里在执行的时候，前面1234是做为*a传递的，后面的a = 1, b = 2是做为**b传递的
func(1, 2, 3, 4, a = 1, b = 2)


# 回调函数

"""
将函数做为函数名传入另一个函数，然后函数执行完之后，再执行传入的函数
"""
def func1(n, func2, func3):
    if n > 0:
        func2()
    else:
        func3()

def func2():
    print("func2")

def func3():
    print("func3")

func1(1, func2, func3)



