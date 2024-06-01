import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    reciever_ip_address='192.168.180.72'
    PORT=8080
    target=(reciever_ip_address,PORT)
    s.bind(target)
    while True:
        message=s.recvfrom(120)
        data=message[0]
        print(data)
        # data="\n"
        # print(data.('ascii'))
except Exception as e:
    print("i've got no message from you...")
else:
    print("it's done by your side")
finally:
    print("accomplished.....")
