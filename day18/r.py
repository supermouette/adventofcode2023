import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

with open("test.txt") as f:
    lines = [
        l.strip("\n").replace("(", "").replace(")", "").split(" ")
        for l in f.readlines()
    ]

directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}

rr, cc = [], []
current_coord = [0, 0]
for l in lines:
    direction = directions[l[0]]
    for i in range(int(l[1])):
        current_coord[0] += direction[0]
        current_coord[1] += direction[1]
        rr.append(current_coord[0])
        cc.append(current_coord[1])

print(min(rr), max(rr), min(cc), max(cc))

min_rr = min(rr)

if min_rr < 0:
    for i in range(len(rr)):
        rr[i] -= min_rr


rr = np.array(rr)
cc = np.array(cc)


img = np.zeros((max(rr) + 2, max(cc) + 2, 3), np.uint8)


print(cc)


img[rr, cc] = [255, 255, 255]

label_img = label(img[:, :, 0], connectivity=1, background=1)

regions = regionprops(label_img)


for r in regions:
    print(r.label, int(r.area_filled))


plt.imshow(img)
plt.show()

plt.imshow(label_img)
plt.show()
