#!/usr/bin/python
import socket
import cv2
from camera import VideoCamera
import sys


class ServerSocket:
    status="INIT"
    count=0
    def __init__(self,hostname,port):
        self.hostname=hostname
        self.port=port
        ServerSocket.count=0
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((hostname,port))
    
    def send(self,data,client_addr):
        #print '    Sending "%s" response to Client:%s'%(data,client_addr)
        self.sock.sendto(data,client_addr)

    def receive(self):
        print "Waiting for request from Client...."
        data,address=self.sock.recvfrom(4096)
        return (data,address)
        
    def close(self):
        self.sock.close()

    def gen(self,camera,client_addr):
        while (True):
            a=camera.get_frame(ServerSocket.count)
            
            ServerSocket.send(self,a,client_addr)
            
            ServerSocket.count+=1
            yield a

    def video_feed(self,client_addr):
        jpeg=ServerSocket.gen(self,VideoCamera(),client_addr)
        [jpeg.next() for i in range(600)]
