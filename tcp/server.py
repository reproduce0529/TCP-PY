import socket

# 서버 설정
host = '127.0.0.1'  # 서버 IP 주소
port = 12345  # 포트 번호

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 바인딩
server_socket.bind((host, port))

# 클라이언트 연결 대기
server_socket.listen(1)

print('서버가 실행되었습니다.')

# 클라이언트 연결 수락
client_socket, addr = server_socket.accept()
print('클라이언트가 연결되었습니다:', addr)

# 클라이언트로부터 데이터 수신
data = client_socket.recv(1024).decode()
print('수신한 데이터:', data)

# 클라이언트에 데이터 전송
message = '서버로부터 전송된 메시지입니다.'
client_socket.send(message.encode())

# 연결 종료
client_socket.close()
server_socket.close()
