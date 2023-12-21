from time import time

t0 = time()
with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]


for i, l in enumerate(lines):
    if (j := l.find("S")) != -1:
        print(i, j)
        S = i, j
        break

possible_pos = set([(S[0], S[1], 0)])
print(possible_pos)


new_pos_to_explore = [S]

for step_left in range(1, 64 + 1):
    pos_to_explore = new_pos_to_explore
    new_pos_to_explore = []
    for i, j in pos_to_explore:
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            i2, j2 = i + x, j + y
            if 0 <= i2 < len(lines) and 0 <= j2 < len(lines[0]):  # bound check
                if lines[i2][j2] != "#":  # check invalid pos
                    if (i2, j2, step_left % 2) not in possible_pos:
                        possible_pos.add((i2, j2, step_left % 2))
                        new_pos_to_explore.append((i2, j2))

cpt = 0
for i, j, mod in possible_pos:
    if mod == 0:
        cpt += 1
        lines[i] = lines[i][:j] + "0" + lines[i][j + 1 :]

for l in lines:
    print(l)

print(cpt)
print(time() - t0)
