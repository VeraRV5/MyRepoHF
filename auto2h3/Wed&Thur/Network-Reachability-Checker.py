import socket



#Make a simple socket, that handle IPV4 with .AF_INET, and use connection TCp with SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
GoogleIP = socket.gethostbyname("gooogle.com")


try:
    s.settimeout(15)
    s.connect((GoogleIP, 80))
    print ("Reachable!")

    s.sendall(b"Hello")
    Reply = s.recv(1024)
    print (Reply.decode())

except Exception as e:
    print ("error occured:", e)

finally:
    s.close()
    



