import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

with open("input.txt") as f:
    lines = [
        l.strip("\n").replace("(", "").replace(")", "").split(" ")
        for l in f.readlines()
    ]

directions = {"3": [-1, 0], "1": [1, 0], "2": [0, -1], "0": [0, 1]}

points = [[0, 0]]
perimeter = 0
for l in lines:
    direction = directions[l[2][-1]]
    dist = int(l[2][1:-1], base=16)
    # direction = directions[l[0]]
    # dist = int(l[1])
    points.append(
        (points[-1][0] + direction[0] * dist, points[-1][1] + direction[1] * dist)
    )
    perimeter += 0.5 * dist

area = int(
    0.5
    * sum(
        [
            points[i][0] * points[i - 1][1] - points[i - 1][0] * points[i][1]
            for i in range(1, len(points))
        ]
    )
)

print(area + perimeter + 1)
plt.plot([y for x, y in points], [x for x, y in points])
plt.show()
