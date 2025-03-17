# 字符串

# 编码：所谓编码，就是二进制数和语言文字的一种对应关系
# 字符，通过编码，来翻译成二进制，反过来同理

"""
ASCII 一个字节一个字符
Unicode 兼容所有语言，两个字节标识一个字符
UTF-8 对不同的字符用不同的长度来表示，节约空间，但是每个字符都是特殊的，转换时间慢，中文使用了三个字节
GBK 专门解决中文，双字节
"""
# 编解码
"""
编码 encode：就是将字符转成字节流
解码 decode：反过来
"""
a="hello"
b=b"hello"
print(a)
print(b)
# <class 'bytes'>
print(type(a))
print(type(b))

# 编解码
print("=========编解码=========")
a="hello"
# 编码，转字节
b=a.encode()
print(b)
# 还原，转字符
print(b.decode())

print("=========索引============")
"""
索引从0开始
"""
a="hello"
print(a[0])
print(a[1])
# 超出范围会报错
# python不仅支持顺序索引，还支持倒序索引，用负数倒序
print(a[-1])
print(a[-2])

# a[start, end, step]
# 切片，顾头不顾尾，左闭右开，超过长度不会报错，
# 切片前的顺序要和步长的顺序一致，比如2:5:-1就有问题，2到5从左往后，-1是从右往左
a="123456789"
print(a[0:5:1])
print(a[0:5:2])
print(a[5:9:1])
print(a[5:100:2])
# 倒序也可以切片，倒序的话步长也是负数
print(a[-1:2:-2])
print(a[-2:-100:-1])

print("=========常用操作============")
a="hello wor ld"
# 查看是否存在字符（有返回1，没有返回0），待查找字符、开始位置、结束位置
print(a.find("el"))
print(a.find("lo", 1, 10))
# 查看字符在哪个位置（返回索引号），查看字符、开始位置、结束位置
print(a.index("el"))
print(a.index("ll"))
print(a.index("ll", 1, 10))
# 返回字符出现的次数
print("个数有：", a.count("l"))
print("个数有：", a.count("l", 1, 10))
# 替换字符，后面是替换的个数
a="lllll"
print(a.replace("l", "o", 2))
# 分割字符，返回数组，后面代表切的次数，看需要切几次
a="hello world !!!"
a = a.split(" ")
for i in a:
    print(i)
b="hello world !!!"
b = b.split(" ", 1)
for i in b:
    print(i)

## 其他操作
# 第一个字符大写
a="hello world !!!"
print(a.capitalize())
# 大写转小写
a="HELLO"
print(a.lower())
# 转小写
a="hello"
print(a.upper())
# 查看是否已某个字符开头
a="hello world"
print(a.startswith("hello"))
a="nihao hello world"
print(a.startswith("hello", 5, 10))
# 是否以某个字符结束，后面不能用负数，因为默认步长是正
a="nihao hello world"
print(a.endswith("world"))
print(a.endswith("ello", 2, 10))
# 将每个单词的首字母大写
a="hello world"
print(a.title())
# 判断是否都是大小写
print(a.islower())
print(a.isupper())
# 判断是否是数字
print(a.isdigit())
a="hello world123"
count=0
for i in a:
    if i.isdigit():
       count=count+1
print(count)

# 增
a="hello"
b="o"
print(a + b)
# 中间插入*
print("*".join(a))

# 删除左空白
a="   hello"
print(a.lstrip())


