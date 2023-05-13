## 闭包原理，只是外部函数的形参为一个函数
def output(func):
    def inner():
        print("瞌睡前：美滋滋")
        func()
        print("瞌睡后：爽歪歪")
    return inner

## 两种调用方法：
## 闭包原始方法调用：

## def sleeping():
##     print("瞌睡中：甜蜜蜜")
##
## fn = output(sleeping)
## fn()

## 函数方法前申明调用：

@output

def sleeping():
    print("瞌睡中：甜蜜蜜")
## @output相当于fn = output(sleeping)
sleeping()