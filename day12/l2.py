from itertools import combinations
from time import time
import re

t = time()
with open("test.txt") as f:
    lines = [l.strip("\n").split(" ") for l in f.readlines()]

arrangements = []
pattern = re.compile("(#+)")

for debug_count, l in enumerate(lines):
    # print(debug_count, time() - t)
    # l[0] = "?".join([l[0]] * 3)
    line_count = [int(c) for c in l[1].split(",")]
    len_line_count = len(line_count)
    # line_count = line_count * 3
    tag_count = l[0].count("#")
    new_tag_nb = sum(line_count) - tag_count
    match_count = 0
    question_indexes = [index for index, char in enumerate(l[0]) if char == "?"]
    # can I remove some question_indexes ??
    print(len(list(combinations(question_indexes, new_tag_nb))))
    for i in combinations(question_indexes, new_tag_nb):
        copy = list(l[0])
        for j in i:
            copy[j] = "#"
        findall = pattern.findall("".join(copy))
        if len(findall) == len_line_count:
            copy_tab = [len(a) for a in findall]

            if copy_tab == line_count:
                match_count += 1

    arrangements.append(match_count)

print(arrangements)
print(sum(arrangements))
print(time() - t)
