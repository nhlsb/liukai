## 一个类只有一个实例对象
class Clone:
    
    pass
clone = Clone()
clone1 = Clone()
clone2 = Clone()

print(clone1)
print(clone2)

s1 = clone
s2 = clone

print(s1)
print(s2)


