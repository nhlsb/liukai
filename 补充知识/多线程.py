## 未采用多线程
# import time
# def sing():
#     while True:
#         print("我会唱歌")
#         time.sleep(1)
# def dance():
#     while True:
#         print("我会跳舞")
#         time.sleep(1)
# sing()
# dance()


## 采用多线程
# import time
# import threading
# def sing():
#     while True:
#         print("我会唱歌")
#         time.sleep(1)
# def dance():
#     while True:
#         print("我会跳舞")
#         time.sleep(1)
#
#
# xiancheng1 = threading.Thread(target=sing)
# xiancheng2 = threading.Thread(target=dance)
# xiancheng1.start()
# xiancheng2.start()


import time
import threading
def sing(arr1):
    while True:
        print(arr1)
        time.sleep(1)
def dance(arr2):
    while True:
        print(arr2)
        time.sleep(1)

## 以元组的形式传给形参
xiancheng1 = threading.Thread(target=sing,args=("我会唱歌",))
## 以字典的形式传给形参
xiancheng2 = threading.Thread(target=dance,kwargs={"arr2":"我会跳舞"})
xiancheng1.start()
xiancheng2.start()