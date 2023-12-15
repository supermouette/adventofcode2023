with open("input.txt") as f:
    init_sequences = f.readline().strip("\n").split(",")

result = []


def hash(seq):
    h = 0
    for c in seq:
        h += ord(c)
        h *= 17
        h %= 256
    return h


for seq in init_sequences:
    result.append(hash(seq))

print("part1", sum(result))

boxes = [[] for i in range(256)]

for seq in init_sequences:
    if "-" in seq:
        box_id = seq[:-1]
        lense_to_remove = [
            lense for lense in boxes[hash(box_id)] if lense.startswith(box_id)
        ]
        if len(lense_to_remove) != 0:
            boxes[hash(box_id)].remove(lense_to_remove[0])
    elif "=" in seq:
        box_id, lense = seq.split("=")
        for i in range(len(boxes[hash(box_id)])):
            if boxes[hash(box_id)][i].split("=")[0] == box_id:
                boxes[hash(box_id)][i] = seq
                break
        else:
            boxes[hash(box_id)].append(seq)

result = 0
for i in range(256):
    result += sum(
        [(i + 1) * (j + 1) * int(b.split("=")[1]) for j, b in enumerate(boxes[i])]
    )

print("part 2", result)
