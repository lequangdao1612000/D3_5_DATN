import numpy as np

detect_zone = []
plate_d3_zone = []
with open('D3/detect_zone.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        x, y = line.split(' ')
        detect_zone.append((int(x), int(y)))

with open('D3/plate_D3_zone.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        x, y = line.split(' ')
        plate_d3_zone.append((int(x), int(y)))

detect_zone = np.array(detect_zone, dtype=np.int32)
detect_zone = detect_zone.reshape((-1, 1, 2))

plate_d3_zone = np.array(plate_d3_zone, dtype=np.int32)
plate_d3_zone = plate_d3_zone.reshape((-1, 1, 2))

########################################################################################################################

polygon_dict_d3 = {}
point_dict_d3 = {}

with open("spot_file/d3_polygon.txt", "r") as f:
    count = 0
    points = []
    for line in f.readlines():
        line = line.strip()
        line = line.split(",")
        points.append([int(line[0]), int(line[1])])
        count += 1
        if count % 4 == 0:
            polygon_dict_d3[int(count / 4)] = points
            points = []

with open("spot_file/d3.txt", "r") as f:
    count = 0
    points = []
    for index, line in enumerate(f.readlines()):
        line = line.strip()
        line = line.split(",")
        x, y, w, h = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        point_dict_d3[index] = [x, y, w, h]
