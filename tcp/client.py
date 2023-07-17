import socket

# 서버 설정
host = '127.0.0.1'  # 서버 IP 주소
port = 12345  # 포트 번호

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((host, port))

# 서버로 데이터 전송
message = '클라이언트에서 보내는 메시지입니다.'
client_socket.send(message.encode())

# 서버로부터 데이터 수신
data = client_socket.recv(1024).decode()
print('수신한 데이터:', data)

# 연결 종료
client_socket.close()
