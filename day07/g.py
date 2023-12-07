from functools import cmp_to_key

with open("input.txt") as f:
    lines = [l.strip("\n").split(" ") for l in f.readlines()]


def power(hand, part2=False):
    histo = {}
    for card in hand:
        histo[card] = histo.get(card, 0) + 1

    sorted = list(histo.values())
    sorted.sort()

    if part2 and len(sorted) != 1:
        if histo.get("J", 0) != 0:
            sorted.remove(histo["J"])
            sorted[-1] += histo["J"]

    power = int(sorted[-1])
    if len(sorted) > 1 and sorted[-2] == 2:
        power += 0.5
    return power


# part 1
hands = []

for hand in lines:
    hands.append(
        [
            hand[0],
            power(hand[0]),
            hand[0]
            .replace("A", "E")
            .replace("K", "D")
            .replace("Q", "C")
            .replace("J", "B")
            .replace("T", "A"),
            hand[1],
        ]
    )

sorted_hands = sorted(
    hands,
    key=cmp_to_key(
        lambda x, y: x[1] - y[1] if x[1] != y[1] else (1 if x[2] > y[2] else -1)
    ),
)

print("part 1", sum([(i + 1) * int(c[-1]) for i, c in enumerate(sorted_hands)]))

# part 2
hands = []
for hand in lines:
    hands.append(
        [
            hand[0],
            power(hand[0], part2=True),
            hand[0]
            .replace("A", "E")
            .replace("K", "D")
            .replace("Q", "C")
            .replace("J", "1")  # part 2 update
            .replace("T", "A"),
            hand[1],
        ]
    )

sorted_hands = sorted(
    hands,
    key=cmp_to_key(
        lambda x, y: x[1] - y[1] if x[1] != y[1] else (1 if x[2] > y[2] else -1)
    ),
)

print("part 2", sum([(i + 1) * int(c[-1]) for i, c in enumerate(sorted_hands)]))
