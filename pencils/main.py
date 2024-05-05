import cv2

pencils = {}
for i in range(1, 13):
    image = cv2.imread(f'images\\img ({i}).jpg')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    _, thresh = cv2.threshold(hsv[:, :, 1], 50, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=3)
    cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    pencils[f'img ({i})'] = 0
    for cnt in cnts:
        if cv2.arcLength(cnt, True)<1000: continue
        (x, y), (w, h), r = cv2.minAreaRect(cnt)
        if (h/w > 9 or w/h > 9) and (w > 50 and h > 50):
            pencils[f'img ({i})'] += 1 

for pencil in pencils:
    print(f'Число карандашейНа изображении {pencil} - {pencils[pencil]}')