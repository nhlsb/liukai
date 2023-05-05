import os
'''
os.listdir() ## 列出指定目录下的内容
os.path.isdir() ## 验证指定路径是否为文件夹，返回布尔值
os.path.exists() ## 验证指定路径是否存在，返回布尔值
'''
def func(n):
    if n>=2:
        return func(n-1) + n
    else :
        return n
func(100)
print(func(100))