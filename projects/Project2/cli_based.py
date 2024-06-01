import socket 
try: 
    while True:
             s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
             ip_address='192.168.180.225'
             PORT=8080
             target= (ip_address,PORT)
             message= input("what is your message = ")
             Encripted_message=message.encode('ascii')
             s.sendto(Encripted_message,target)

except Exception as e:
    print("no need")

