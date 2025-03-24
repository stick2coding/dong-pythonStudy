"""
必须有一个明确的结束条件
每次进入更深一层递归的时候，规模应该更小
相邻两次必须有紧密的联系
递归效率不高，层次过多会导致栈溢出
定义简单，逻辑清晰

递推：递归的每一次都是基于上一次进行下一次
回溯：遇到终止条件之前，从最后往前一级一级返回
"""

# 递归求N项的和
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

a = sum(10)
print(a)

# 递归求斐波那契数
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(10))