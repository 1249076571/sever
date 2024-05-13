import socket  
  
PORT = 80  # 服务器监听的端口号  
BUFFER_SIZE = 1024  # 读取缓冲区大小  
  
# 创建TCP socket对象  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  
# 允许地址重用  
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
  
# 绑定到地址和端口  
server_address = ('', PORT)  
server_socket.bind(server_address)  
  
# 开始监听  
server_socket.listen(3)  
print(f"Listening on port {PORT}")  
  
while True:  
    # 接受客户端连接  
    client_socket, client_address = server_socket.accept()  
    print(f"Accepted connection from {client_address}")  
  
    try:  
        # 接收数据  
        data = client_socket.recv(BUFFER_SIZE)  
        if data:  
            print(f"Received {len(data)} bytes of data")  
            # 将字节转换为字符串（假设是UTF-8编码）  
            received_data = data.decode('utf-8')  
            print(f"Received: {received_data}")  
        else:  
            print("No data received.")  
  
    finally:  
        # 关闭客户端连接  
        client_socket.close()  
  
# 注意：在实际应用中，你可能想要添加异常处理、多线程或异步处理来同时处理多个客户端连接。
