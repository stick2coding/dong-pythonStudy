# 不可变对象指的是内存空间中内容不可被修改的对象
# 内容不可变，但是地址可以变化

"""
常见的不可变对象
数值：int bool float complex
字符串：String
元组：tuple
"""
# 下面这个例子可以看到，i的值不变，但是地址发生了变化，也就是1这个值所在的内存空间内容没有变化，但是i在修改后指向了新的内存空间
# 如图：picture/01/img_9.png
i = 1
print("赋值前", id(i))
i += 2
print("计算后", id(i))

# 可变对象，就是内容可以发生变化，但是地址却不变
"""
常见的可变类型
list
set
dict
"""

# 如图 picture/01/img_10.png
# 修改并不会改变地址
l = [1, 2, 3]
print("赋值前", id(l))
l.append(4)
print("计算后", id(l))
l[1]=9
print("调整后", id(l))