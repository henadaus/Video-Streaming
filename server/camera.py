
import cv2
import pickle

class VideoCamera(object):
        
    def __init__(self):
       
        #self.video = cv2.VideoCapture(0)
       
        self.video = cv2.VideoCapture('OnTheFloor.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self,count):
        
       
        if(self.video.isOpened()):
            
            success, image = self.video.read()
               
            ret, jpeg = cv2.imencode('.jpeg', image)     
            print type(jpeg.tobytes())
            return jpeg
        else:
            return "No"   
            
            
            
            
                
            
        
        
            
            

