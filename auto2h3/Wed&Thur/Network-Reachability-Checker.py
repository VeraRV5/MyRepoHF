import socket



def ServerChecker (Host, Port):
#Make a simple socket, that handle IPV4 with .AF_INET, and use connection TCp with SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    GoogleIP = socket.gethostbyname("gooogle.com")
    H = Host
    P = Port

#Make a try and catch, try to connect to server, with timeout, and try to send a binary comment, 
    try:
      s.settimeout(5)
      s.connect((H, P))
      print ("Reachable!")

      s.sendall(b"Hello")
      Reply = s.recv(1024)
      print (Reply.decode())
# Make an exception to catch error, if timeoutoccurs, the server is not responding to packet send
    except socket.timeout:
      print ("No answer from server")
# Make an exception for any other errors, and print the error out
    except Exception as e:
      print ("Can't reach!!")
      print ("error occured:", e)
#Finally close the socket connection
    finally:
      s.close()
    



H = input("Write Hostname or IP: ")
P = int(input("Write which port to connect to: "))
ServerChecker(H, P)

