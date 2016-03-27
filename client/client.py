#!/usr/bin/python
import socket
import sys
import os
from ClientSocket import ClientSocket
import Tkinter as tk
from PIL import Image,ImageTk
class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        self.setup=tk.Button(self,text="Setup",command=self.setupFunc)
        self.setup.pack()

        self.play=tk.Button(self,text="Play",command=self.playFunc)
        self.play.pack()

        self.pause=tk.Button(self,text="Pause",command=self.pauseFunc)
        self.pause.pack()

        self.teardown=tk.Button(self,text="Teardown",command=self.teardownFunc)
        self.teardown.pack()

        self.img=ImageTk.PhotoImage(Image.open('tuned.jpg'))
        self.video=tk.Label(self,image=self.img)
        self.video.pack()

        self.status="INIT"
        
        self.c=0
        self.initialize()
    
    def initialize(self):
        self.s_addr=sys.argv[1]
        self.s_port=sys.argv[2]
        self.server_address=(self.s_addr,int(self.s_port))
        self.client=ClientSocket(self.server_address)

    def setupFunc(self):
        if self.status=="INIT":
            self.status="READY"
            self.client.send("setup")
            
            rcvd=self.client.receive()
            print "     Response received from server:"+rcvd

    def teardownFunc(self):
        self.status="INIT"
        self.client.send("teardown")
        self.client.close()
        print "     Connection closed successfully"


    def playFunc(self):
        
        print "Started receiving frame..."
        self.status="PLAYING"
        self.client.send("play")
        self.playUtil();    
        
    def playUtil(self):
            
        path=self.client.receive_frame(self.c,self)
            
        self.img=ImageTk.PhotoImage(Image.open(path))
        self.video.configure(image=self.img)
        self.c+=1
        os.remove(path)
        self.after(50, self.playUtil)
                
                
                   

    def pauseFunc(self):
        if self.status=="PLAYING":
            print "     Video paused for a while...."
            self.status="READY"
            self.client.send("pause")

if __name__=="__main__":
    app=App()
    app.mainloop()
