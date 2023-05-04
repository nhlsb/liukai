a=(3,2,1)
print(type(a))
print(a[0])
def yuanzu(*args):
    print(args)
yuanzu("a","b",3)
def zidian(**kwargs):
    print(kwargs)
zidian(name="Tom",age=18)
print("...........................")
def chouxiang(xiangcheng,xiangchu,xiangjia):
    a=xiangcheng(9,9,9)
    b=xiangchu(9,3,3)
    c=xiangjia(1,2,3)
    print(a)
    print(b)
    print(c)
    
def xiangcheng(x,y,z):
    return x*y*z
def xiangchu(x,y,z):
    return x/y/z
chouxiang(xiangcheng,xiangchu,lambda x,y,z : x+y+z)###匿名函数可以充当未定义的函数


    
