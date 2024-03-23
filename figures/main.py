from skimage.measure import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def match(figure, masks):
    for mask_id, mask in enumerate(masks):
        if np.all(figure.shape == mask.shape):
            if np.all(figure == mask):
                return mask_id
    return None

image = np.load('ps.npy.txt')
labeled = label(image)
l_max = labeled.max()
result = defaultdict(lambda: 0)
masks = []
for region in regionprops(labeled):
    mask_id = match(region.image, masks)
    if not mask_id is None:
        result[mask_id] += 1
    else: 
        masks.append(region.image)
        result[len(masks)-1] += 1

if l_max == sum(result.values()):
    for mask_id, mask in enumerate(masks):
        plt.title(f'Встречаются следующие фигуры...\n\n{mask_id})')
        plt.imshow(mask)
        plt.show()
    plt.title(f'Всего фигур - {l_max}\n{dict(result)}')
    print(result)
else: print('Ошибка при подсчете фигур!')
plt.imshow(image)
plt.show()