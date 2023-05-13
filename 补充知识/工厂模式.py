## 大批量创建对象的时候有统一的入口，当发生修改时，仅需要修改工厂类的创建方法即可
class All:
    pass
class Worker(All):
    pass
class Teacher(All):
    pass
class Student(All):
    pass

class Factory:
    def get(self,class_type):
        if class_type == "w":
            return Worker()
        elif class_type == "t":
            return Teacher()
        elif class_type == "s":
            return Student()

factory = Factory()
object1 = factory.get("w")
object2 = factory.get("t")
object3 = factory.get("s")

print(object1)
print(object2)
print(object3)