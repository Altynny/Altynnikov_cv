import matplotlib.colors as clrs
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import regionprops, label
from collections import defaultdict

image = plt.imread('balls_and_rects.png')
hue = clrs.rgb_to_hsv(image)[:, :, 0]

figures = {'rect':{'all':0, 'colors':{}}, 'ball':{'all':0, 'colors':{}}}

def addFigure(figure_name: str, color):
    global figures
    figures[figure_name]['all'] += 1

    color = round(color, 2)
    has_match = False
    for dict_clr in figures[figure_name]['colors']:
        if color == dict_clr:
            has_match = True
            break
    
    if not has_match:
        figures[figure_name]['colors'][color] = 0

    figures[figure_name]['colors'][color] += 1

gray = image.mean(2)
gray[gray>0] = 1
labeled = label(gray)
regions = regionprops(labeled)

for region in regions:
    x, y = region.centroid
    color = hue[int(x), int(y)]
    if np.all(region.image == 1): 
        figure = 'ball'
    else: figure = 'rect'
    addFigure(figure, color)

print(figures)
# plt.subplot(121)
# plt.imshow(hue)
# plt.subplot(122)
# plt.imshow(image)
# plt.show()
# np.all
h = sorted(np.unique(hue.flatten()))
print(len(h))
plt.plot(h, 'o')
plt.show()