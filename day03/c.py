import re

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

symbol_pattern = re.compile(r"([^\.0-9])")
number_pattern = re.compile("([0-9]+)")
directions = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

parts = []
gears = 0

for i, l in enumerate(lines):
    symbols = re.finditer(symbol_pattern, l)
    for symbol in symbols:
        j = symbol.start()
        print("symbol", symbol.group(0))
        new_s = []
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            if lines[x][y].isdigit:
                part_numbers = re.finditer(number_pattern, lines[x])
                for part_number in part_numbers:
                    if part_number.start() <= y < part_number.end():
                        # parts.add(int(part_number.group(0)))
                        new_s.append(int(part_number.group(0)))
        new_s = list(set(new_s))
        print(new_s)
        parts += new_s
        if symbol.group(0) == "*" and len(new_s) == 2:
            gears += new_s[0] * new_s[1]

print(sum(parts))
print(gears)
