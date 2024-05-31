import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops 
from collections import defaultdict
from pathlib import Path

def count_holes(region):
    holes = 0
    labeled = label(np.logical_not(region.image))
    regions = regionprops(labeled)
    for region in regions:
        not_bound = True
        coords = np.where(labeled == region.label)
        for y, x in zip(*coords):
            if y == 0 or x == 0 or y == labeled.shape[0] - 1 or x == labeled.shape[1] - 1:
                not_bound = False
        holes += not_bound
    return holes

def recognize(region):
    if count_holes(region):
            ny = region.centroid_local[0]/region.image.shape[0]
            if ny >= 0.46:
                return 'D'
            else:
                return 'R'
            
    inv = np.logical_not(region.image)
    labeled = label(inv)
    holes = np.max(labeled)
    if holes == 3:
        return 'K'
    
    nx = region.centroid_local[1]/region.image.shape[1]
    if nx >= 0.6:
        return 'J'
    else:
        return 'L'
    return '_'

alphabet = plt.imread('task3.png').mean(2)
alphabet[alphabet>0.25] = 1
alphabet[alphabet!=1] = 0
labeled = label(alphabet)
regions = regionprops(labeled)

result = defaultdict(lambda: 0)
for i, region in enumerate(regionprops(labeled)):
    symbol = recognize(region)
    result[symbol] += 1

print(np.max(labeled),dict(result))