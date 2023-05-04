num=10000

def show(n):
    if n:
        print("------------------------")
    print(num)

def saving(money):
    show(False)
    global num
    num+=money
    
    return num
    
print(saving(1))
