a=[1,1,2,3,2]
print(a.count(1))
b=(1,1,2,[3,2])
b[3][1]="asdfghj"
del b[3][0]
b[3].append("bbb")
print(b)
c=a.pop(0)
print(a)
d={"aa":1,"bb":2,"cc":3}
print(d)
