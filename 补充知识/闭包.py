## (1)外部函数内部套用内部函数，外部函数的返回值为内部函数
## (2)内部函数需要使用外部函数的形参，在内部函数里用nonlocal申明外部函数形参

def atm(initname):
    def inner(mon,isbool = True):
        nonlocal initname
        if isbool:
            initname += mon
            print(f"存款{mon},余额为:{initname}")
        else:
            initname -= mon
            print(f"取款{mon},余额为:{initname}")
    return inner

fn = atm(100)
fn(300)