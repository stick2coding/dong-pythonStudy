# 函数的嵌套：
# 1、就是在一个函数内部再调用一个函数


def func1():
    print('func1')

def func2():
    print('func2')
    func1()

print("qian tao...")
func2()
print("函数中在定义函数》。。。")
# 2、在函数中再定义函数
def func3():
    def func4():
        print('func4')

    print('func3')
    func4()

func3()