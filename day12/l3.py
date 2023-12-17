from itertools import combinations
from itertools import groupby
from functools import cache
from time import time
import re

t = time()
with open("input.txt") as f:
    lines = [l.strip("\n").split(" ") for l in f.readlines()]

arrangements = []
pattern = re.compile("(#+)")


@cache
def count_possible(candidate, match):
    if candidate.count("#") > sum(match) or candidate.count("#") + candidate.count(
        "?"
    ) < sum(match):
        return 0

    first_q = candidate.find("?")
    if first_q == -1:
        return (
            1
            if [len(a) for a in pattern.findall("".join(candidate))] == list(match)
            else 0
        )
    else:
        old_part = candidate[:first_q]
        match_old = [len(a) for a in pattern.findall("".join(old_part))]
        match_copy = list(match)[:]

        for i, mo in enumerate(match_old):
            if i == len(match_old) - 1:
                if old_part[-1] == "#":
                    if match_copy[0] == mo:
                        count = count_possible(
                            "." + candidate[first_q + 1 :], tuple(match_copy[1:])
                        )
                        return count
                    else:
                        diff_match = match_copy[0] - match_old[-1]
                        if diff_match < 0:
                            return 0
                        else:
                            match_copy[0] = diff_match
                            count = count_possible(
                                "#" + candidate[first_q + 1 :], tuple(match_copy)
                            )
                            return count
                elif match_copy[0] != mo:
                    return 0
                elif match_copy[0] == mo:
                    match_copy = match_copy[1:]

            elif match_copy[0] == mo:
                match_copy = match_copy[1:]
            else:
                return 0

        count = 0
        new_candidate_1 = "." + candidate[first_q + 1 :]
        count += count_possible(new_candidate_1, tuple(match_copy))
        new_candidate_2 = "#" + candidate[first_q + 1 :]
        count += count_possible(new_candidate_2, tuple(match_copy))
        return count


power = 5
for debug_count, l in enumerate(lines):
    l[0] = "?".join([l[0]] * power)
    line_count = [int(c) for c in l[1].split(",")]
    line_count = tuple(line_count * power)
    match_count = 0
    question_indexes = [index for index, char in enumerate(l[0]) if char == "?"]

    match_count += count_possible(l[0], line_count)
    arrangements.append(match_count)

# print(arrangements)
print(sum(arrangements))
print(time() - t)
