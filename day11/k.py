import numpy as np

with open("input.txt") as f:
    lines = [
        [int(c) for c in l.strip("\n").replace(".", "0").replace("#", "1")]
        for l in f.readlines()
    ]

for l in lines:
    print(l)

star_map = np.array(lines, dtype=np.uint8)

stars = list(np.nonzero(star_map))

shift = 0
for i in range(star_map.shape[0]):
    if sum(star_map[i, :]) == 0:
        stars[0] = [s + 1 if s > i + shift else s for s in stars[0]]
        shift += 1

shift = 0
for j in range(star_map.shape[1]):
    if sum(star_map[:, j]) == 0:
        stars[1] = [s + 1 if s > j + shift else s for s in stars[1]]
        shift += 1

distances = []
for i in range(len(stars[0])):
    s1 = [stars[0][i], stars[1][i]]
    for j in range(i, len(stars[0])):
        s2 = [stars[0][j], stars[1][j]]
        distances.append(abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]))

print(sum(distances))

stars = list(np.nonzero(star_map))
shift = 0
n = 1000000 - 1  # WHYYYYYY ????
for i in range(star_map.shape[0]):
    if sum(star_map[i, :]) == 0:
        stars[0] = [s + n if s > i + shift else s for s in stars[0]]
        shift += n

shift = 0
for j in range(star_map.shape[1]):
    if sum(star_map[:, j]) == 0:
        stars[1] = [s + n if s > j + shift else s for s in stars[1]]
        shift += n

distances = []
for i in range(len(stars[0])):
    s1 = [stars[0][i], stars[1][i]]
    for j in range(i, len(stars[0])):
        s2 = [stars[0][j], stars[1][j]]
        distances.append(abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]))

print(sum(distances))
