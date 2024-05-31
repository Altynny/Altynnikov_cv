import cv2
import matplotlib.pyplot as plt

cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)

nominal = 1.05714 # ppmm

image = cv2.imread('task4.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
_, thresh = cv2.threshold(hsv[:, :, 2], 200, 255, cv2.THRESH_BINARY)

cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_cnt = max(cnts, key=cv2.contourArea)
(x, y), r = cv2.minEnclosingCircle(max_cnt)
cv2.circle(image, (int(x), int(y)), int(r), (0, 0, 255), 2)
cv2.line(image, (int(x), int(y)), (int(x+r), int(y)), (0, 0, 255), 2)
d = r * 2 # pixels
print(f'{d} - p\n{d/nominal} - mm') # mm

cv2.imshow('Image', image)
cv2.waitKey(0)