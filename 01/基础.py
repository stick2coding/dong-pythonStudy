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
str = 'hello world'
str1 = "hello world1"
str2 = """hello world2"""
str3 = '''hello world'''
print(str)
print(type(str))

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