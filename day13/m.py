import numpy as np

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

patterns = [[]]

for l in lines:
    if l == "":
        patterns.append([])
    else:
        patterns[-1].append([1 if c == "#" else 0 for c in l])

patterns = [np.array(p) for p in patterns]


a = 0
b = 0
for i in range(len(patterns)):
    for j in range(patterns[i].shape[0] - 1):
        for k in range(min(j + 1, patterns[i].shape[0] - j - 1)):
            if list(patterns[i][j - k, :]) != list(patterns[i][j + 1 + k, :]):
                break
        else:
            if len(range(min(j + 1, patterns[i].shape[0] - j - 1))) > 0:
                a += j + 1
                break
    for j in range(patterns[i].shape[1] - 1):
        for k in range(min(j + 1, patterns[i].shape[1] - j - 1)):
            if list(patterns[i][:, j - k]) != list(patterns[i][:, j + 1 + k]):
                break
        else:
            if len(range(min(j + 1, patterns[i].shape[1] - j - 1))) > 0:
                b += j + 1
                break

print(a * 100 + b)


def diff(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff


a = 0
b = 0
for i in range(len(patterns)):
    for j in range(patterns[i].shape[0] - 1):
        smudge = False
        for k in range(min(j + 1, patterns[i].shape[0] - j - 1)):
            if list(patterns[i][j - k, :]) != list(patterns[i][j + 1 + k, :]):
                if (
                    not smudge
                    and diff(
                        list(patterns[i][j - k, :]), list(patterns[i][j + 1 + k, :])
                    )
                    == 1
                ):
                    smudge = True
                    print(smudge)
                else:
                    break
        else:
            if len(range(min(j + 1, patterns[i].shape[0] - j - 1))) > 0 and smudge:
                a += j + 1
                break
    for j in range(patterns[i].shape[1] - 1):
        smudge = False
        for k in range(min(j + 1, patterns[i].shape[1] - j - 1)):
            if list(patterns[i][:, j - k]) != list(patterns[i][:, j + 1 + k]):
                if (
                    not smudge
                    and diff(
                        list(patterns[i][:, j - k]), list(patterns[i][:, j + 1 + k])
                    )
                    == 1
                ):
                    smudge = True
                    print(smudge)
                else:
                    break
        else:
            if len(range(min(j + 1, patterns[i].shape[1] - j - 1))) > 0 and smudge:
                b += j + 1
                break

print(a * 100 + b)
