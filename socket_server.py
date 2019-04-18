import socket, datetime
HOST = socket.gethostname()
PORT = 65432 # 監听的端口 
print("START")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    # port 只是用來監听，並非傳資料，所以client連線後，會產生新的socket(conn)
    # 此時，server 與client就用此socket(conn)來傳送資料
    # 原本的socket(s)就可以在監听其它的
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)          
            if not data:
                break
            conn.sendall(data)
