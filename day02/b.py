# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

with open("input.txt") as f:
    lines = [l.strip("\n").split(":")[1].split(";") for l in f.readlines()]

ok = 0
power_sum = 0
for i in range(len(lines)):
    l = lines[i]
    possible = True
    min_set = {"blue": 0, "red": 0, "green": 0}

    for game_sets in l:
        print(game_sets)
        g_set = {"blue": 0, "red": 0, "green": 0}
        for draw in game_sets.split(","):
            _, nb, color = draw.split(" ")
            if color in g_set:
                g_set[color] += int(nb)
            else:
                possible = False
        possible = possible and (
            g_set["blue"] <= 14 and g_set["red"] <= 12 and g_set["green"] <= 13
        )
        min_set["blue"] = max(min_set["blue"], g_set["blue"])
        min_set["green"] = max(min_set["green"], g_set["green"])
        min_set["red"] = max(min_set["red"], g_set["red"])
        print(min_set)
        print(g_set, possible)
    if possible:
        ok += i + 1
    power_sum += min_set["blue"] * min_set["green"] * min_set["red"]


print(ok)
print(power_sum)
