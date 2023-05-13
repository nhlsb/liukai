
import socket
## socket:套接字，进程之间的通信工具
socket_client = socket.socket()
socket_client.connect(("localhost",8888))
while True:
    todata = input("请输入您要发送的消息：")
    socket_client.send(todata.encode("UTF-8"))
    if todata == "exit":
        break
    redata = socket_client.recv(1024).decode('UTF-8')
    if redata == "exit":
        break
    print(f"服务端发来信息，内容为：{redata}")

socket_client.close()