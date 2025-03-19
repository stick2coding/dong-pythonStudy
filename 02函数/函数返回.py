# 返回值是返回给函数的调用者
# 多个return 只执行第一个
# 一个函数没有return，默认是返回None
def func():
    print(1)
print(func())

def func():
    return 123
func()
print(func())
a=func()
print(a)

# 返回多个值
# 返回值本质上是只能返回一个值，但是这个值可以是一个元组，一个列表，字典或者集合都可以
# 把return后面的当成一个整体返回
def func():
    return 123,456
def func1():
    return 123,"string"
def func2():
    return 123, {"name":"zhangsan"}

def func3():
    return {"name":"zhangsan"},{"age":1}
print("=================")
a,b=func()
print(type(func()))
print(a,b)
print(type(a), type(b))
print("=================")
a,b=func1()
print(type(func1()))
print(a,b)
print(type(a), type(b))
print("=================")
a,b=func2()
print(type(func2()))
print(a,b)
print(type(a), type(b))
print("=================")
a,b=func3()
print(type(func3()))
print(a,b)
print(type(a), type(b))