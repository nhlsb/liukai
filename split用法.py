##split()由划分标志,划分次数组成，返回一个列表
##x=input().split()
##print(x)
##print(int(x[0])+int(x[1]))
###
##x=int(input().split())
##print(x[0]+x[1])
###
y="abcdefg aaa#bbb"
z=y.split("#",1)[0].split(" ",-1)[1]###划分次数为-1表示划分全部
print(z)

