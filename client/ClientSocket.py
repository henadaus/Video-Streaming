#!/usr/bin/python
import socket
import cv2
import numpy as np
import Tkinter
from Tkinter import * 
from PIL import Image, ImageTk


class ClientSocket:
    """ Client Socket"""
    def __init__(self,server_addr):
        self.server_addr = server_addr
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    def send(self,data):
        print '    Sending "%s" request to Server:"%s"'%(data,self.server_addr)
        sent=self.sock.sendto(data,self.server_addr)

    def receive(self):
        print "Waiting to receive from Server...."
        data,server=self.sock.recvfrom(4096)
        return data     

    def close(self):
        self.sock.close(); 

    def receive_frame(self,c,tkk):
        print "Waiting to receive frames of video from Server...."
        data = np.empty((700,500), dtype = np.int8)
        self.sock.recv_into(data)
        
        raw=cv2.imdecode(data,cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imwrite("frame%d.jpeg" %c,raw)
        path="frame"+str(c)+".jpeg"
        print "pATH :"+path
        
        print c
        return path

    
        



