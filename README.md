# Video-Streaming
This project aims to stream the video stored at server end to the client as per its request.
The entire process takes place as follows:
1.Client first sends a SETUP request to the server to establish a  connection.
  The server records the address of the client.
2.The client sends PLAY request to the server.Server streams video to the client using Motion JPEG,which just sends JPEG frames successively.
3.Client can send a TEARDOWN request to close the connection.

It can also stream live video to the client.Just replace the line "self.video = cv2.VideoCapture('video.mp4')"" to "self.video = cv2.VideoCapture(0)".THe video captured by your webcam will be streamed to the client.

This project has been made using :
1.PIL

2.Opencv

3.Tkinter

4.Python 2.7.6
