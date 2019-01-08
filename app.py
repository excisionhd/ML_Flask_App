
#!/usr/bin/env python3

#Import Dependencies, flask
from flask import Flask, render_template, Response, url_for
import cv2
import sys
import numpy
import landmarks_helper as lh
import dlib
import imutils

#Declare Flask App
app = Flask(__name__)

#Prepare DLib facial recogition
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/facial_recognition')
def face():
    return render_template('face_rec.html')

@app.route ('/projects')
def projects():
    return "Find all available projects here:"

@app.route('/projects/hair_segmentation')
def hair():
	return "Hair segmentation project"

def gen():
    i=1
    while i<10:
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+str(i)+b'\r\n')
        i+=1

def get_frame():

    camera_port=0
    ramp_frames=100
    camera=cv2.VideoCapture(camera_port) #this makes a web cam object

    i=1
    while True:
        retval, im = camera.read()
        im = imutils.resize(im, width=400, height=400)
        rects = detector(im, 1)
        lh.addLandmarksToImage(im, rects, predictor)
        imgencode=cv2.imencode('.jpg',im)[1]
        stringData=imgencode.tostring()
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
        i+=1
    del(camera)

@app.route('/calc')
def calc():
     return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)
