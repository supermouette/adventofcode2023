import numpy as np

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

load = 0


def north():
    for i in range(1, len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "O" and lines[i - 1][j] == ".":
                lines[i] = lines[i][:j] + "." + lines[i][j + 1 :]
                new_line = i - 1
                while lines[new_line - 1][j] == "." and new_line != 0:
                    new_line -= 1
                lines[new_line] = lines[new_line][:j] + "O" + lines[new_line][j + 1 :]


def south():
    for i in range(len(lines) - 2, -1, -1):
        for j in range(len(lines[0])):
            if lines[i][j] == "O" and lines[i + 1][j] == ".":
                lines[i] = lines[i][:j] + "." + lines[i][j + 1 :]
                new_line = i + 1
                while new_line != len(lines) - 1 and lines[new_line + 1][j] == ".":
                    new_line += 1
                lines[new_line] = lines[new_line][:j] + "O" + lines[new_line][j + 1 :]


def west():
    for j in range(1, len(lines[0])):
        for i in range(len(lines)):
            if lines[i][j] == "O" and lines[i][j - 1] == ".":
                lines[i] = lines[i][:j] + "." + lines[i][j + 1 :]
                new_line = j - 1
                while lines[i][new_line - 1] == "." and new_line != 0:
                    new_line -= 1
                lines[i] = lines[i][:new_line] + "O" + lines[i][new_line + 1 :]


def east():
    for j in range(len(lines[0]) - 2, -1, -1):
        for i in range(len(lines)):
            if lines[i][j] == "O" and lines[i][j + 1] == ".":
                lines[i] = lines[i][:j] + "." + lines[i][j + 1 :]
                new_line = j + 1
                while new_line != len(lines[0]) - 1 and lines[i][new_line + 1] == ".":
                    new_line += 1
                lines[i] = lines[i][:new_line] + "O" + lines[i][new_line + 1 :]


direction = {0: north, 1: west, 2: south, 3: east}
loads = []
for i in range(1000):
    north()
    west()
    south()
    east()
    load = sum([lines[i].count("O") * (len(lines[0]) - i) for i in range(len(lines))])
    if i == 0:
        print("part 1", load)
    loads.append(load)


print(loads[999])
load_150 = loads[150]
next_150 = loads[151:].index(load_150)

print(loads[150], loads[151 + next_150])
nb = (1000000000) % next_150
print("part2", loads[150 + nb])
