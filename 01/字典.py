# 键值对，一一绑定，key唯一
dic = {"name":"sunbin", "age":10}
# 空字典
a = dict()
a = {}
# 字典嵌套
a = {"student":[{"name":"sunbin", "age":10},{"name":"sunbin", "age":10}]}
# 修改
a = {"name":"sunbin", "age":10}
a["name"]="dongdong"
print(a)
# 添加，有则添加，无则覆盖
a["grade"]="A"
print(a)
# 删除
del a["grade"]
print(a)
# 清空
a.clear()
print(a)

# 长度，就是键值对的个数
a = {"name":"sunbin", "age":10}
print(len(a))
# keys 返回所有key
a = {"name":"sunbin", "age":10}
print(a.keys())
# values 返回所有values
print(a.values())
# 遍历
for key in a.keys():
    print(key)
# 项，就是遍历所有的键值对，每一个都是一个键值对
print(a.items())
for item in a.items():
    print(item)
for key,value in a.items():
    print(key,value)
# 循环 和上面差不对