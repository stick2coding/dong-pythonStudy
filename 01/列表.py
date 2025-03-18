# 一次存储多个元素
# 列表是有顺序的，先添加的在前面，可以随时添加
li = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# 同一个数组内部是可以存储不同的数据类型
li = ["a", 1, 1.1]
# 可以通过索引访问，从前往后为正，从后往前为负
print(li[1])
print(li[-1])
# 循环读取
for i in li:
    print(i)

# while
i = 0
while i > len(li):
    print(i)
    i += 1

# 相关操作
print("列表相关操作：。。。")
# +
a = ["a", "b", "c"]
b = [1, 2, 3]
print(a + b)

# insert，在指定的位置插入。在下标的前面插入元素
a.insert(2, "string")
print(a)

# append 末尾
a.append("end")
print(a)

# extend 会将待添加的内容进行拆分，下面两个例子可以看到
# 用append是将b单独做为一个元素，extend是将b的三个元素拆分后放到a中
a = ["a", "b", "c"]
b = [1, 2, 3]
a.append(b)
print(a)
a = ["a", "b", "c"]
b = [1, 2, 3]
a.extend(b)
print(a)

# 修改
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
a[1] = "d"
print(a)

# 修改一组元素
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print("元素修改", a)
# 这里就是把元素下标2,3,4替换成了后面的数据
a[2:5] = ["1", "2", "3"]
print("元素修改", a)
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
a[2:6] = ["1", "2", "3"]
print("元素修改", a)
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
a[2:5] = ["1", "2", "3", "4"]
print("元素修改", a)

# 对空切片
print(a[4:4])
# 此时我们如果对这个值进行复制，就是在索引4这个位置拆入，注意是在索引3的后面，索引4的前面
# 这里有个关键问题，就是此时对空切片的赋值只能是可迭代的对象，如果不可迭代就会报错
a[4:4]=["1", "2", "3"]
print(a)
# 比如
try:
    a[4:4] = 1
except Exception as e:
    print("a[4:4] = 1出现了错误")

# 如果加上步长
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print("元素修改", a)
# 这里是把2,4，6位置的数据c,e,g依次替换为了1,2,3
a[2:7:2] = ["1", "2", "3"]
print("元素修改", a)

# del 可以删除列表
# del a
# 也可以通过索引删除对应位置的元素
del a[2:7:2]
print("元素删除", a)
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
del a[1]
print("元素删除", a)

# pop删除，效果同上
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
del a[2:7:2]
print("pop删除", a)

# remove移出一个具体的值
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
a.remove("a")
print("remove", a)

# clear 清空
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
a.clear()
print("clear", a)

# 查找，返回索引
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print("index", a.index("c", 1, 10))

# in not in
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print("in", "a" in a)
print("not in", "z" not in a)

# count
a = ["a", "a", "c", "d", "e", "f", "a", "h", "i", "j"]
print("count", a.count("a"))

# sort
a = [1, 7, 0, 4, 2, 1,  2, 3]
# 默认升序
a.sort()
print("sort", a)
# 降序
a.sort(reverse=True)
print("sort", a)

# reverse
a = ["a", "a", "c", "d", "e", "f", "a", "h", "i", "j"]
a.reverse()
print("reverse", a)

# sorted 不对原列表操作和sort区分开，原列表顺序不变
a = [1, 7, 0, 4, 2, 1,  2, 3]
# 默认升序
b = sorted(a)
print("sorted a", a)
print("sorted b", b)

# 推导式
a = [1, 7, 0, 4, 2, 1,  2, 3]
# 意思就是遍历a的元素，当元素大于2的时候，给元素乘2
print("推导式", [i*2 for i in a if i > 2])

