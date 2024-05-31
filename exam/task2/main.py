import cv2

cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow('Max sat', cv2.WINDOW_GUI_NORMAL)

image = cv2.imread('task2.png')
bgr = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

max_saturation = max(hsv[:, :, 1].flatten())
hsv [hsv[:, :, 1] < max_saturation] = (0, 0, 0)
max_saturation_circles = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
max_saturation_circles = cv2.cvtColor(max_saturation_circles, cv2.COLOR_BGR2BGRA)

cv2.imshow('Image', image)
cv2.imshow('Max sat', max_saturation_circles)
cv2.waitKey(0)