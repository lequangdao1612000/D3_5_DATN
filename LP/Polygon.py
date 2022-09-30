import numpy as np

detect_zone = []

with open('C:/Users/ASUS/Desktop/daoquang1612/parking_project/datn/LP/detect_zone.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        x, y = line.split(' ')
        detect_zone.append((int(x), int(y)))

detect_zone = np.array(detect_zone, dtype=np.int32)
detect_zone = detect_zone.reshape((-1, 1, 2))
