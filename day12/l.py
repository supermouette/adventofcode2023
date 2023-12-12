from time import time

t = time()
from itertools import groupby

with open("input.txt") as f:
    lines = [l.strip("\n").split(" ") for l in f.readlines()]

arrangements = []

for l in lines:
    question_count = l[0].count("?")
    line_count = [int(c) for c in l[1].split(",")]
    match_count = 0
    for i in range(2**question_count):
        copy = l[0][:]
        for j in range(question_count):
            copy = copy.replace("?", "." if (i // 2**j) % 2 == 0 else "#", 1)
        if [
            len(list(group)) for key, group in groupby(copy) if key == "#"
        ] == line_count:
            match_count += 1
    arrangements.append(match_count)


print(sum(arrangements))
print(time() - t)
