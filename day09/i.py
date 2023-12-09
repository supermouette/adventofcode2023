with open("input.txt") as f:
    lines = [[int(i) for i in l.strip("\n").split(" ")] for l in f.readlines()]

last_numbers = []
first_numbers = []
for line in lines:
    diff_lines = [line]
    while len([i for i in diff_lines[-1] if i != 0]) != 0:
        diff_lines.append(
            [
                diff_lines[-1][i + 1] - diff_lines[-1][i]
                for i in range(len(diff_lines[-1]) - 1)
            ]
        )
    for i in range(len(diff_lines) - 2, -1, -1):
        diff_lines[i].append(diff_lines[i][-1] + diff_lines[i + 1][-1])
        diff_lines[i].insert(0, diff_lines[i][0] - diff_lines[i + 1][0])

    print(diff_lines)

    last_numbers.append(diff_lines[0][-1])
    first_numbers.append(diff_lines[0][0])

print(last_numbers)
print(sum(last_numbers))
print(sum(first_numbers))
