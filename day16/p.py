with open("input.txt") as f:
    contraption = [l.strip("\n") for l in f.readlines()]

energized_map = []

for i in range(len(contraption)):
    contraption[i] = [*contraption[i]]
    energized_map.append([0] * len(contraption[0]))


def check_bound(x, y, contraption):
    return 0 <= x < len(contraption) and 0 <= y < len(contraption[0])


beam_array = {}


def beam(x, y, direction, contraption, energized_map):
    if direction not in beam_array.get((x, y), []):
        beam_array[(x, y)] = [direction]
    else:
        return
    energized_map[x][y] = 1
    while contraption[x][y] == ".":
        x, y = x + direction[0], y + direction[1]
        if not check_bound(x, y, contraption):
            return
        energized_map[x][y] = 1
    if contraption[x][y] == "/":
        direction = [direction[1] * -1, direction[0] * -1]
        x, y = x + direction[0], y + direction[1]
        if check_bound(x, y, contraption):
            beam(x, y, direction, contraption, energized_map)
    elif contraption[x][y] == "\\":
        direction = [direction[1], direction[0]]
        x, y = x + direction[0], y + direction[1]
        if check_bound(x, y, contraption):
            beam(x, y, direction, contraption, energized_map)
    elif contraption[x][y] == "-":
        if direction[0] == 0:
            x, y = x + direction[0], y + direction[1]
            if check_bound(x, y, contraption):
                beam(x, y, direction, contraption, energized_map)
        else:
            dir1 = [0, 1]
            x1, y1 = x + dir1[0], y + dir1[1]
            if check_bound(x1, y1, contraption):
                beam(x1, y1, dir1, contraption, energized_map)
            dir2 = [0, -1]
            x2, y2 = x + dir2[0], y + dir2[1]
            if check_bound(x2, y2, contraption):
                beam(x2, y2, dir2, contraption, energized_map)
    elif contraption[x][y] == "|":
        if direction[1] == 0:
            x, y = x + direction[0], y + direction[1]
            if check_bound(x, y, contraption):
                beam(x, y, direction, contraption, energized_map)
        else:
            dir1 = [1, 0]
            x1, y1 = x + dir1[0], y + dir1[1]
            if check_bound(x1, y1, contraption):
                beam(x1, y1, dir1, contraption, energized_map)
            dir2 = [-1, 0]
            x2, y2 = x + dir2[0], y + dir2[1]
            if check_bound(x2, y2, contraption):
                beam(x2, y2, dir2, contraption, energized_map)


beam(0, 0, [0, 1], contraption, energized_map)
print("part1", sum([sum(e) for e in energized_map]))


def init_energize_map():
    energized_map = []
    for i in range(len(contraption)):
        energized_map.append([0] * len(contraption[0]))
    return energized_map


max_energy = 0
for i in range(len(contraption)):
    energized_map = init_energize_map()
    beam_array = {}
    beam(i, 0, [0, 1], contraption, energized_map)
    max_energy = max(max_energy, sum([sum(e) for e in energized_map]))
    energized_map = init_energize_map()
    beam_array = {}
    beam(i, len(contraption[0]) - 1, [0, -1], contraption, energized_map)
    max_energy = max(max_energy, sum([sum(e) for e in energized_map]))

for j in range(len(contraption[0])):
    energized_map = init_energize_map()
    beam_array = {}
    beam(0, j, [1, 0], contraption, energized_map)
    max_energy = max(max_energy, sum([sum(e) for e in energized_map]))
    energized_map = init_energize_map()
    beam_array = {}
    beam(len(contraption) - 1, j, [0, 1], contraption, energized_map)
    max_energy = max(max_energy, sum([sum(e) for e in energized_map]))

print(max_energy)
