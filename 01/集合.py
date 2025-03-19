# {}包裹，但是没有键值对的概念，就是一个一个的元素
# 集合是没有顺序，不重复的

a={1,2,3}
print(a)
print(type(a))

# set 将内容拆分为集合
a = set("abded")
# 这里也可以看到集合内元素不可重复，就是每个元素只有一个
print(a)


# 定义空集合
a = set()
print(a)

# add只能添加一个元素
a={1,3,2,4}
a.add(6)
print(a)

# 追加，必须可迭代才行，列表、元组、集合都可以
a={1,3,2,4}
b=[6,7,8]
a.update(b)
print(a)
# 追加一个字典，只添加key
a={1,3,2,4}
b={"a":1,"b":2}
a.update(b)
print(a)

# 可以利用update的机制，对元素进行去重，给出例子
a={1,2,3,4,5,6,7,8,9,10}
b={7,8,9,10,11,12,13,14,15,16}
a.update(b)
print(a)

# remove删除元素，如果元素不存在，会报错
a={1,2,3,4,5,6,7,8,9,10}
a.remove(1)
print(a)

# discard删除元素，如果元素不存在，不会报错，和remove不一样
a={1,2,3,4,5,6,7,8,9,10}
a.discard(1)
print(a)

# pop 删除一个元素，随机删除，返回删除的元素
a={1,2,3,4,5,6,7,8,9,10}
print(a.pop())
print(a.pop())
print(a.pop())

# 交集
a={1,2,3,4,5,6,7,8,9,10}
b={7,8,9,10,11,12,13,14,15,16}
print(a&b)

# 并集
a={1,2,3,4,5,6,7,8,9,10}
b={7,8,9,10,11,12,13,14,15,16}
print(a|b)

# 求最大值
a={1,2,3,4,5,6,7,8,9,10}
print(max(a))
# 求最小值
a={1,2,3,4,5,6,7,8,9,10}
print(min(a))

# enumerate 方法举例
# 可以遍历拿到每个元素的索引和值
a=["a","b", "c"]
for i,j in enumerate(a):
    print(i,j)

# 列表推导式
# 意思是：遍历i，i的范围是0-9，然后将i的平方放到列表中
a=[i ** 2 for i in range(10)]
print(a)
# 同理，元组也可以
a=(i ** 2 for i in range(10))
# tuple可以从对象的地址中获取到值
print(tuple(a))

# 同理，字典也有推导式
a={i:i ** 2 for i in range(10)}
print(a)

# 同理，集合也可以
a={i ** 2 for i in range(10)}
print(a)
# 不过，集合会自动去重
a=[1,1,3]
b={i ** 2 for i in a}
print(b)


