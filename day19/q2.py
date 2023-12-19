from time import time

t0 = time()

from functools import reduce
from copy import deepcopy

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

rules = {"R": [], "A": []}

for i, l in enumerate(lines):
    if l == "":
        first_part = i + 1
        break
    name, raw_ruleset = l.split("{")
    ruleset = []
    for raw_rule in raw_ruleset[:-1].split(","):
        splited_rule = raw_rule.split(":")
        ruleset.append(splited_rule)
    rules[name] = ruleset


xmas_range = {
    "x": {"min": 1, "max": 4000},
    "m": {"min": 1, "max": 4000},
    "a": {"min": 1, "max": 4000},
    "s": {"min": 1, "max": 4000},
}


def get_nb_accepted(xmas, rule_name):
    if rule_name == "R":
        return 0
    if rule_name == "A":
        return reduce(
            lambda x, y: x * y, [i["max"] - i["min"] + 1 for i in list(xmas.values())]
        )
    accepted = 0
    xmas_dup = deepcopy(xmas)
    for rule in rules[rule_name]:
        if len(rule) == 1:
            accepted += get_nb_accepted(xmas_dup, rule[0])
        else:
            if "<" in rule[0]:
                splited = rule[0].split("<")
                splited[1] = int(splited[1])
                if splited[1] > xmas[splited[0]]["max"]:
                    # everything go into that rule
                    accepted += get_nb_accepted(xmas_dup, rule[1])
                    break
                elif splited[1] > xmas[splited[0]]["min"]:
                    # split range
                    new_xmap = deepcopy(xmas_dup)
                    new_xmap[splited[0]]["max"] = splited[1] - 1
                    accepted += get_nb_accepted(new_xmap, rule[1])
                    xmas_dup[splited[0]]["min"] = splited[1]
            if ">" in rule[0]:
                splited = rule[0].split(">")
                splited[1] = int(splited[1])
                if splited[1] < xmas[splited[0]]["min"]:
                    # everything go into that rule
                    accepted += get_nb_accepted(xmas_dup, rule[1])
                    break
                elif splited[1] < xmas[splited[0]]["max"]:
                    # split range
                    new_xmap = deepcopy(xmas_dup)
                    new_xmap[splited[0]]["min"] = splited[1] + 1
                    accepted += get_nb_accepted(new_xmap, rule[1])
                    xmas_dup[splited[0]]["max"] = splited[1]
    return accepted


print(get_nb_accepted(xmas_range, "in"))
print(time() - t0)
