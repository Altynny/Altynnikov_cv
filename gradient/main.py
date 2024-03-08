import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [139, 0, 0]
color2 = [175, 238, 238]

diag = image.diagonal().shape[1]
step = size - 1
v = np.linspace(0, 1, 2*diag-1)
n = 0

image = image.reshape(size**2, 3)
for i in range(image.shape[0]):
    if np.all(image[i]) == 0:
        r = lerp(color1[0], color2[0], v[n])
        g = lerp(color1[1], color2[1], v[n])
        b = lerp(color1[2], color2[2], v[n])
        image[i:i+step*(i%diag+1):step, :] = [r, g, b]
        n += 1
image = image.reshape(size, size, 3)

plt.figure(1)
plt.imshow(image)
plt.show()