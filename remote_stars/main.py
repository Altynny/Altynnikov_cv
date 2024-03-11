import numpy as np
import matplotlib.pyplot as plt
import socket

host = '84.237.21.36'
port = 5152

def recvall(sock, n):
    data = bytearray()
    while len(data)<n:
        packet = sock.recv(n-len(data))
        if not packet:
            return
        data.extend(packet)
    return data

def extrem(image):
    extrems = []
    for y in range(1, image.shape[0]-1):
        for x in range(1, image.shape[1]-1):
            if image[y, x] > image[y-1, x] and image[y, x] > image[y, x-1] and image[y, x] > image[y, x+1] and image[y, x] > image[y+1, x]:
                    extrems.append((y,x))
    return extrems


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    
    for _ in range(10):
        sock.send(b"get")
        bts = recvall(sock, 40002)

        im = np.frombuffer(bts[2:40002], dtype='uint8').reshape(bts[0], bts[1])

        pos = extrem(im)
        pos1 = pos[0]
        pos2 = pos[1]

        res = round(((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**0.5, 1)

        sock.send(f'{res}'.encode())
        print(sock.recv(20))
    
    plt.subplot(111)
    plt.title(f'{pos1} | {pos2}')
    plt.imshow(im)
    plt.show()