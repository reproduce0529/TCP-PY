import socket

# 서버 설정
host = '127.0.0.1'  # 서버 IP 주소
port = 12345  # 포트 번호

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 소켓 바인딩
server_socket.bind((host, port))

print('서버가 실행되었습니다.')

# 클라이언트로부터 데이터 수신
data, addr = server_socket.recvfrom(1024)
print('수신한 데이터:', data.decode())

# 클라이언트에 데이터 전송
message = '서버로부터 전송된 메시지입니다.'
server_socket.sendto(message.encode(), addr)

# 소켓 닫기
server_socket.close()
