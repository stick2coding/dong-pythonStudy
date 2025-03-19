# 必填参数、默认参数、可变参数、关键字参数/命名关键字参数

def func(a, b, c=0, *args, **kwargs):
    print(a, b, c, args, kwargs)

func(1,2,3,4,5)
func(1,2,3,4,5,6, name="zhangsan")

# 可以从代码编辑器中的提示，看到具体哪些参数给了谁
def func(a, b=0, *args, d=10):
    print(a, b, args, d)
func(1,2,3,4,5)
func(1,2,3,4,5,6, d=20)