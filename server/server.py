#!/usr/bin/python
import socket
from ServerSocket import ServerSocket


host=socket.gethostname()
print host
port=12345
server=ServerSocket('localhost',port)


while True:
    rcvd,client_addr=server.receive()
    print '    Received request "%s" from:%s'%(rcvd,client_addr)
    
    
    if rcvd=="setup" and server.status=='INIT':
        print "CONNECTION ESTABLISHED"
        server.status="READY"
        server.send("OK",client_addr)
        
    elif rcvd=="teardown":
        print "CLOSING CONNECTION...GOODBYE!!!"
        server.status="INIT"
        break

    elif rcvd=="play" and server.status=="READY":
        print "Started sending frames.."
        server.status="PLAYING"
        server.video_feed(client_addr)

    elif rcvd=="pause" and server.status=="PLAYING":
        print "Sending of frames has been paused for a while..."
        server.status="READY"
        print server.count