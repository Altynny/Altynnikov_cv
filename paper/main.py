import cv2
import zmq #pip install pyzmq
import numpy as np
from skimage.measure import regionprops

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("Mask", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("Paper", cv2.WINDOW_GUI_NORMAL)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
port = 5055
socket.connect(f"tcp://192.168.0.113:{port}")
n = 0
lower = 100
upper = 200

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
text = 'This is paper'
textsize = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

while True:
    bts = socket.recv()
    n += 1

    key = cv2.waitKey(10)
    if key == ord("q"):
        break
    if key == ord('p'):
        cv2.imwrite(f'out_{n}.png', image)

    arr = np.frombuffer(bts, np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (11, 11), 0)
    mask = cv2.Canny(gray, lower, upper)
    cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # из найденных конутров берём координаты бумаги
    rect = cv2.minAreaRect(cnts[0])
    box = cv2.boxPoints(rect)
    box = np.intp(box)

    # создаём массив размером с лист бумаги для написания текста на нём
    paper = np.zeros((int(rect[1][1]), int(rect[1][0]), 3))
    rows, cols, _ = paper.shape
    textX = (cols - textsize[0]) // 2
    textY = (rows + textsize[1]) // 2
    cv2.putText(paper, text, (textX, textY), font, font_scale, (1, 1, 1), font_thickness)

    M = cv2.getPerspectiveTransform(np.float32([[0, rows], [0, 0], [cols, 0], [cols, rows]]), np.float32(box))
    paper = cv2.warpPerspective(paper, M, (image.shape[1], image.shape[0]))

    pos = np.where(paper>0)
    image[pos] = paper[pos]

    cv2.imshow("Image", image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Paper', paper)

cv2.destroyAllWindows()
