# 模块就是 .py 文件，模块名就是文件名
# 通过pip 安装的包，比如 requests，都是模块
# 内置模块：Python解释器提供
# 查看内置模块
import builtins
print(dir(builtins))

# 库 第三方模块：pip install xxx

# 自定义模块


"""
模块使用
创建模块
导入模块import
使用 模块名.变量
"""
# from 模块名 import 模块中的变量

# py文件的两种功能
"""
1、脚本方式，一个文件就是整个程序，表示代码是直接运行在当前文件
__name__ == "main"

2、做为模块导入时
__name__== "模块名"
"""

print(__name__)