a = 3
def func(a):
    a = 4
    print(a)
func(a)
print(a)

a = {"key":"value"}
print(a)
def func1(b):
    b["key"] = "value2"
    print(b)
func1(a)
print(a)


"""
如果函数收到的是可变对象，就能够修改对象的原始值
如果是不可变对象，比如元组、数字、字符，那么对值的修改不会影响原来的值
"""


def test():
    print("test")

res = test()

print(test())
print(res)

print(id(test))
print(id(res))