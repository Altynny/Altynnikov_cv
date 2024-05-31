import cv2

cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)
image = cv2.imread('task1.png')
gray = cv2.imread('task1.png', 0)
gray[gray==51] = 0

cnts, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area_max = 0
for cnt in cnts:
    area = cv2.contourArea(cnt) - cv2.arcLength(cnt, True)
    if area > area_max:
        area_max = area
        c_max = cnt 
cv2.putText(image, f'Max area - {area_max}', (20, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255, 1), 1)
cv2.drawContours(image, [c_max], -1, (0, 255, 0, 1), 1)
cv2.imshow('Image', image)
cv2.waitKey(0)