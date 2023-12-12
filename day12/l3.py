from itertools import combinations
from itertools import groupby
from time import time
import re

t = time()
with open("test.txt") as f:
    lines = [l.strip("\n").split(" ") for l in f.readlines()]

arrangements = []
pattern = re.compile("(#+)")


def count_possible(candidate, match, new_tag_nb):
    print("prout", candidate, match)
    findall = [len(a) for a in pattern.findall("".join(candidate))]
    """
    if max(findall) > max(match):
        return 0
    elif len(findall) < len(match):
        return 0
    """
    if nb == 0:
        # print(candidate, findall, match)
        return 1 if findall == match else 0
    else:
        cpt = 0
        cpt += count_possible(
            candidate[:i] + "#" + candidate[i + 1 :],
            match,
            nb - 1,
            q,
        )
        return cpt


for debug_count, l in enumerate(lines):
    # print(debug_count, time() - t)
    print(l)
    # l[0] = "?".join([l[0]] * 3)
    line_count = [int(c) for c in l[1].split(",")]
    # line_count = line_count * 3
    tag_count = l[0].count("#")
    new_tag_nb = sum(line_count) - tag_count
    match_count = 0
    question_indexes = [index for index, char in enumerate(l[0]) if char == "?"]

    match_count += count_possible(l[0], line_count, new_tag_nb)

    arrangements.append(match_count)
    break

print(arrangements)
print(sum(arrangements))
print(time() - t)
