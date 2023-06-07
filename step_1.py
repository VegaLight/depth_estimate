# -*- coding: utf-8 -*-
# @Time: 2023/6/2 16:48
# Author: Steve Shaw
# E-mail: stevezmm11@gmail.com

import cv2
import os
cap = cv2.VideoCapture('original.mp4')
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(width, height)

size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 30, size)

frame_count = 0
while True:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, size, interpolation=cv2.INTER_CUBIC)
        image_name = os.path.join('videoToPictures/' + str(frame_count) + '.png')

        frame_count = frame_count+1
        cv2.imwrite(image_name, frame)

        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


