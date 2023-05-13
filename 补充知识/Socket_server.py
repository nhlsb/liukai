
import socket
## socket:套接字，进程之间的通信工具
socket_server = socket.socket()
socket_server.bind(("localhost",8888))
socket_server.listen(1)
## accept()是阻塞方法
result : tuple = socket_server.accept()
conn = result[0]
addr = result[1]
print(f"已接收到客户端的链接，客户端信息为：{addr}")
while True:
    todata : str = conn.recv(1024).decode("UTF-8")
    if todata == "exit":
        break
    print(f"客户端发来信息，内容为：{todata}")
    redata = input("请输入您要回复的信息：")
    conn.send(redata.encode("UTF-8"))
    if redata == "exit":
        break
conn.close()
socket_server.close()