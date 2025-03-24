
# 异常的处理
# 异常默认是基类

try:
    print(a)
except:
    print("出现异常")
print("world")

try:
    print(a)
except NameError as e:
    print("出现异常", e)
print("world")

# 捕获所有异常
try:
    print(a)
except Exception as e:
    print("出现异常", e)
print("world")

# 多分支
try:
    print(a)
except IndexError as e:
    print("出现异常", e)
except NameError as e:
    print("出现异常", e)
print("world")

# try else
try:
    print(a)
except IndexError as e:
    print("出现异常", e)
except NameError as e:
    print("出现异常", e)
else:# 没有异常执行
    print("没有异常")
print("world")


try:
    print(a)
except Exception as e:
    print("出现异常", e)
finally:# 有异常也会执行
    print("有异常也会执行")
print("world")


try:
    a = int(input("请输入一个数字:"))
    print(10/a)
except IndexError:
    print("出现异常")
except ValueError:
    print("ValueError")
except Exception as e:
    print("Exception", e)
else:
    print("没有异常")
finally:
    print("有异常也会执行")

# 主动抛出异常
raise NameError("主动抛出异常")