# 输出
print("hello world")
print("hello world", "hello world1")
print("hello world", end="....")

# 单行注释
"""
多行注释
"""
# 标识符
"""
标识符命名规范
数字、字母、下划线组成
不能由数字开头
不能是关键字
需要区分大小写
"""
# 如何查看python关键字
import keyword
print(keyword.kwlist)
# 变量名：驼峰、下划线
# 数值类型： int float bool complex
print(3.1e5)
# 查看数据类型
print(type(3.1E5))
print(True+1)

# 六大标准数据类型：
"""
数字、字符串、列表、元组、集合、字典
"""

# String
str0 = 'hello world'
str1 = "hello world1"
str2 = """hello world2"""
str3 = '''hello world'''
print(str0)
print(type(str0))

print(str1)
print(type(str1))

print(str2)
print(type(str2))

# 使用斜杠进行转义
print("hello \"world\"")
# 字符串连接
print("1" + "2")
# 重复输出
print("重复输出 "*2)
# 查看是否存在
print("hello" in "hello world")
# 查看不存在，不存在返回True
print("hello1" not in "hello world")
# 取消转义
print("换行。。。\n换行。。。")
print(r"换行。。。\n换行。。。")
# 通过索引获取字符串
print("hello"[0])
print("hello"[0:3])
# 格式化
name = "hello"
age = 111
score = 11.123456
print("%s,%d,%f,%.2f" % (name,age,score,score))
# format
print("{}，{}".format(name,age))
print("{0}，{1}，{0}".format(name,age,score))
print("{name} is {value}".format(name=name,value=age))
print(f'我的名字是 {"we + 1"}，年龄是 {20}，或者是{age}')
# 转义、特殊意义
print("换行\n换行")
print("tab\ttab")
print("取消转义\\t")
print("输出单引号\'输出双引号\"")
# 运算符 先幂运算、再乘除取模、再加减，括号提高优先级
print(1 + 1)
print(1 * 1)
# 商
print(2 / 1)
# 余数
print(2 % 2)
# 幂运算
print(2 ** 3)
# 多变量同时赋值
a,b,c = "hello", 1.1, 2
print(a,b,c)
print(type(a),type(b),type(c))
# 类型转换 使用类型包裹
# 浮点转整数，精度丢失
print(int(1.1))
print(int(True))
print(str(123))
print(type(str(123)))