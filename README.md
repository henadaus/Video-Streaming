<h1>Video-Streaming</h1>
This project aims to stream the video stored at server end to the client as per its request.

<b>The entire process takes place as follows:</b>

1.Client first sends a <b>SETUP</b> request to the server to establish a  connection.The server records the address of the client.

2.The client sends <b>PLAY</b> request to the server.Server streams video to the client using Motion JPEG,which just sends JPEG frames successively.

3.Client can send a <b>TEARDOWN</b> request to close the connection.

It can also stream live video to the client.Just replace the line "self.video = cv2.VideoCapture('video.mp4')"" to "self.video = cv2.VideoCapture(0)".THe video captured by your webcam will be streamed to the client.

This application has been made using :
<ul>
<li>PIL</li>

<li>OpenCV</li>

<li>Tkinter</li>

<li>Python 2.7.6</li>
</ul>
<br><br>
<h3>Execution:</h3>
<ul>
<li>SERVER END:On terminal, execute --> python server.py</li>

<li>CLIENT END:On terminal ,execute --> python client.py serverAddress serverPortNo</li>
</ul>

<h6>Tested on Ubuntu 14.04 LTS</h6>
