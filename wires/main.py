from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

def count_pieces(image):
    labeled = label(image)

    for n in range(1, labeled.max()+1):
        count = 0
        wire = labeled == n
        pieces = (label(binary_erosion(wire))).max()
        count += pieces
        match count:
            case 0: print(f' Провод {n} АННИГИЛИРОВАН')
            case 1: print(f' Провод {n} не порван')
            case _: print(f' Провод {n} разделён на {count} частей')

for file_num in range(1, 7):
    image = np.load(f'wires{file_num}npy.txt')
    print(f'\nВ файле wires{file_num}npy.txt...\n')
    count_pieces(image)