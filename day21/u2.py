import matplotlib.pyplot as plt

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
plot_x = [1]
for step_left in range(1, 1000 + 1):
    if step_left % 1000 == 0:
        print(step_left, step_left / (26501365 + 1))
    pos_to_explore = new_pos_to_explore
    new_pos_to_explore = []
    for i, j in pos_to_explore:
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            i2, j2 = (len(lines) + i + x) % len(lines), (len(lines[0]) + j + y) % len(
                lines[0]
            )

            if lines[i2][j2] != "#":  # check invalid pos
                if (i + x, j + y, step_left % 2) not in possible_pos:
                    possible_pos.add((i + x, j + y, step_left % 2))
                    new_pos_to_explore.append((i + x, j + y))

    cpt = 0
    for i, j, mod in possible_pos:
        if mod == step_left % 2:
            cpt += 1
    plot_x.append(cpt)

print(cpt)

print(plot_x)

plt.plot(list(range(1001)), plot_x)
plt.show()
