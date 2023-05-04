class Student:
    def __init__(self,name,age,adrr):
        self.name = name
        self.age = age
        self.adrr = adrr

for i in range(10):
##    a = input("请输入姓名:")
##    b = input("请输入年龄:")
##    c = input("请输入地址:")
    a,b,c = input("请输入姓名: " "请输入年龄: " "请输入地址: ").split()
##    print(m,n,h)
    stu = Student(a,b,c)
    print(f"第{i+1}个学生的姓名是{stu.name},年龄是{stu.age},地址是{stu.adrr}.")
