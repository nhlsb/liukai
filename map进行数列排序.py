n=int(input())
llist=input()
l=list(map(int,llist.split()))
print(l)
l.sort()
print(l)
for i in l:
    print(i,end = " ")

