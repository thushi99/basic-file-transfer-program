import socket

s=socket.socket()
host=socket. gethostname()
port=8080
s.bind((host,port));
s.listen(1)
print(host)
print("Waiting for incoming connections.....");
conn,addr=s.accept()
print(addr,"has connected to the server")

filename=input(str("Enter the file name of the file : "))
file=open(filename,'rb')
file_data=file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully")