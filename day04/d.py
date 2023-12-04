with open("input.txt") as f:
    cards = [l.strip("\n").split(":")[1].split("|") for l in f.readlines()]

cards = [[nbs.strip().replace("  ", " ").split(" ") for nbs in c] for c in cards]

win_points = []
win = []
for winnings_numbers, my_numbers in cards:
    card_points = 0
    for nb in winnings_numbers:
        if nb in my_numbers:
            card_points += 1
    if card_points != 0:
        win_points.append(2 ** (card_points - 1))
        win.append(card_points)
    else:
        win.append(0)

print("part 1", sum(win_points))

cards_numbers = {i: 1 for i in range(len(win))}
for i, card in enumerate(win):
    if card != 0:
        for j in range(1, card + 1):
            cards_numbers[i + j] += cards_numbers[i]

print("part 2", sum(cards_numbers.values()))
