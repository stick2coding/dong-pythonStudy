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


# 可迭代对象：能通过for循环来一个个将内容取出来
# 整数无法迭代
# range(start, end, step)，范围左闭右开，默认从0开始
print("开始为1，结束为5，步长为2")
for i in range(1, 5, 2):
    print(i)
print("开始为1，结束为5，步长为1")
for i in range(1, 5, 1):
    print(i)
print("开始为2，结束为5，步长为1")
for i in range(2, 5, 1):
    print(i)
print("只有一个参数，默认开始为0，默认步长为1：")
for i in range(5):
    print(i)

# 使用for来实现99乘法表
for row in range(1, 10):
    for col in range(1, row + 1):
        # print("%d*%d=%d" % (row, col, row*col), end="\t")
        print(f"{row}*{col}={row*col}", end="\t")
    print()

# break、continue只能在循环体内使用
# break 退出当前一层的循环
for i in range(10):
    if i == 5:
        print("循环结束，跳出。。。")
        break
    print(f"执行一次：{i}")

# 使用了break，当列等于5的时候直接跳出
for row in range(1, 10):
    for col in range(1, row + 1):
        if col == 5:
            break
        # print("%d*%d=%d" % (row, col, row*col), end="\t")
        print(f"{row}*{col}={row*col}", end="\t")
    print()

# 使用了continue，这个时候当列等于5的时候，是直接跳到下一层循环，所以没有5*5,6*5,7*5
for row in range(1, 10):
    for col in range(1, row + 1):
        if col == 5:
            continue
        # print("%d*%d=%d" % (row, col, row*col), end="\t")
        print(f"{row}*{col}={row*col}", end="\t")
    print()
