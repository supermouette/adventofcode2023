import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

south = (1, 0)
north = (-1, 0)
east = (0, 1)
west = (0, -1)

directions = {"south": south, "north": north, "east": east, "west": west}
opposite_dir = {"south": "north", "north": "south", "east": "west", "west": "east"}
pipes = {
    "|": ["north", "south"],
    "-": ["east", "west"],
    "L": ["north", "east"],
    "J": ["north", "west"],
    "7": ["south", "west"],
    "F": ["south", "east"],
}

S = -1
for i, l in enumerate(lines):
    if (pos := l.find("S")) != -1:
        S = [i, pos]
        print(S)
        break

nest_map = np.zeros((len(lines) * 2, len(lines[0] * 2)), dtype=np.int8)


def part1():
    for starting_dir in directions.keys():
        path_len = 0
        pos = S[:]
        d = starting_dir
        print("starting new starting dir", d)
        while True:
            d_coord = directions[d]
            prev_pos = pos[:]
            pos = [pos[0] + d_coord[0], pos[1] + d_coord[1]]
            if prev_pos[0] == pos[0]:
                nest_map[
                    pos[0] * 2,
                    min(prev_pos[1], pos[1]) * 2 : max(prev_pos[1], pos[1]) * 2 + 1,
                ] = 1
            else:
                nest_map[
                    min(prev_pos[0], pos[0]) * 2 : max(prev_pos[0], pos[0]) * 2 + 1,
                    pos[1] * 2,
                ] = 1

            new_pipe = lines[pos[0]][pos[1]]
            coming_from = opposite_dir[d]
            if new_pipe == "S":
                print("finished", path_len // 2 + 1)
                return path_len // 2 + 1
            if new_pipe == ".":
                print("found .")
                break
            new_pipe_connect = pipes[new_pipe][:]
            if coming_from in new_pipe_connect:
                path_len += 1
                aaaa = new_pipe_connect
                aaaa.remove(coming_from)
                d = aaaa[0]
            else:
                print("path not connecting")
                break


part1()


plt.imshow(nest_map)
plt.show()

label_img = label(nest_map, connectivity=1, background=1)

plt.imshow(label_img)
plt.show()

small_label_img = label_img[::2, ::2]
plt.imshow(small_label_img)
plt.show()

small_label_img[small_label_img == 1] = 0
plt.imshow(small_label_img)
plt.show()

print(len(np.nonzero(small_label_img)[0]))
