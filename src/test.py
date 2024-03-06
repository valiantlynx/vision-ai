import cv2
import numpy as np
from object_detection import ObjectDetection

cap = cv2.VideoCapture("src/los_angeles.mp4")

_, frame = cap.read()

cv2.imshow("Frame", frame)
cv2.waitKey(0)