#!/usr/bin/env python3
import dlib
import cv2
import numpy as np
import argparse
import imutils
import pandas as pd
import landmarks_helper as lh
from imutils import face_utils

#dataset = pd.read_csv('train_data.csv', header=None)

#images = []
#for index, row in dataset.iterrows():
#    image = np.reshape(np.asarray(row), (48, 48))
#    images.append(image)
    #cv2.imwrite('images/img_' + str(index) + '.jpg', image)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# detect faces in the grayscale image
#image = cv2.imread("images/color_img.jpg")

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    raise IOError("Cannot open webcam.")

while True:
    ret_val, img = cam.read()

    img = cv2.flip(img, 1)
    img = imutils.resize(img, width=600, height=400)
    rects = detector(img, 1)
    lh.addLandmarksToImage(img, rects, predictor)

    cv2.imshow('Output', img)

    if cv2.waitKey(1) == 27: 
        cv2.destroyAllWindows()

#image = (image/256).astype('uint8')
#image = imutils.resize(image, width=100, height=100)
# show the output image with the face detections + facial landmarks


