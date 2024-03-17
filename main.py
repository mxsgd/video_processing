import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt

video_path = 'videos/birds1.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print('couldnt open video')
    exit()

while True:
    ret, frame  = cap.read()

    if not ret:
        break

    cv2.imshow('Video', frame)

    if cv2.waitKey(25) &0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()