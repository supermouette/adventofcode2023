import re

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

lines_1 = ["".join(re.findall("[0-9]", l)) for l in lines]
print("part1", sum([int(l[0] + l[-1]) for l in lines_1]))

english_numbers = {
    "twone": "21",
    "oneigh": "18",
    "threeigh": "38",
    "fiveigh": "58",
    "sevenine": "79",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eigh": "8",
    "nine": "9",
}

number_regex = "[0-9]|" + "|".join(english_numbers.keys())

lines_2 = [
    "".join(english_numbers.get(match, match) for match in re.findall(number_regex, l))
    for l in lines
]

print("part2", sum([int(l[0] + l[-1]) for l in lines_2]))
