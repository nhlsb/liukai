'''九九乘法表'''
a=1
while a<=9:
    b=1
    while b<=a:
        print(f"{a}*{b}={a*b}",end='\t')
        b+=1
    print()
    a+=1
'''九九乘法表'''
print()
for i in range(1,10,1):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end='\t')
    print()
