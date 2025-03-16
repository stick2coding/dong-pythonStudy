if True:
    print("真")
else:
    print("假")
print("逻辑判断。。。")

# 任何非0，非空对象都是True
# 0，空对象，None对象都是False
# 判断的返回值要么是True,或者是False

print(True + 1)
print(not 0)

# 比较运算符
a = 1
b = 1
if a > b:
    print("a>b")
elif a < b:
    print("a<b")
else:
    print("b=a")

# 逻辑运算
print("逻辑运算...")
if True and False:
    print("True")
else:
    print("False")

if True or False:
    print("True")
else:
    print("False")

if not True:
    print("True")
else:
    print("False")
# 逻辑运算是短匹配，快速结束，
# 比如或运算，只要遇到一个true就直接结束，输出结果为true
# 比如与运算，只要遇到一个false，那么结果就是false

# 三目运算
a = 1
b = 2
print("a>b" if a > b else "a<b")

# 三大流程
# 顺序、分支（if/else）、循环（while）
a =1
while a<3:
    print(str(a) + "次")
    a += 1

# 循环嵌套
a = 1
while a<3:
    print("一级循环", a)
    b = 1
    while b<3:
        print("二级循环", b)
        b += 1
    a = a + 1

# 练习
a =1
while a<5:
    print("*" * a)
    a += 1

a = 1
while a<5:
    b = 1
    while b<a:
        print("*", end=" ")
        b += 1
    print() # 自带换行
    a += 1

# 打印9*9
print("打印9*9乘法表》》》》")
a = 1
while a <= 9:
    b = 1
    while b <= a:
        # 格式化输出
        print("%d*%d=%d" % (a, b, a*b),end="\t")
        # print(a, "*", b , "=", a*b, end=" ")
        b += 1
    print()
    a += 1