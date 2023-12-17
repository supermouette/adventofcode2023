from heapq import heappop, heappush

with open("input.txt") as f:
    city_blocks = [[int(c) for c in f.strip("\n")] for f in f.readlines()]


def neighbor_p1(x, y, dx, dy, di):
    n = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + i < len(city_blocks) and 0 <= y + j < len(city_blocks[0]):
            if dx == i and dy == j:
                if di < 2:
                    n.append((city_blocks[x + i][y + j], (x + i, y + j, i, j, di + 1)))
            elif not (dx == i * -1 and dy == j * -1):
                n.append((city_blocks[x + i][y + j], (x + i, y + j, i, j, 0)))
    return n


def neighbor_p2(x, y, dx, dy, di):
    n = []
    if di == 0:
        if 0 <= x + dx * 3 < len(city_blocks) and 0 <= y + dy * 3 < len(city_blocks[0]):
            n.append(
                (
                    sum([city_blocks[x + dx * i][y + dy * i] for i in (1, 2, 3)]),
                    (x + dx * 3, y + dy * 3, dx, dy, di + 3),
                )
            )
    else:
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + i < len(city_blocks) and 0 <= y + j < len(city_blocks[0]):
                if dx == i and dy == j:
                    if di < 9:
                        n.append(
                            (city_blocks[x + i][y + j], (x + i, y + j, i, j, di + 1))
                        )
                elif not (dx == i * -1 and dy == j * -1):
                    n.append((city_blocks[x + i][y + j], (x + i, y + j, i, j, 0)))
    return n


def dijkstra(s, t, neigbbor_func):
    # stolen from google : https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwifrKq4yfP7AhUJTKQEHXa6BOQQFnoECDMQAQ&url=https%3A%2F%2Fisn.irem.univ-mrs.fr%2F2011-2012%2Fmedia%2Fresources%2Fdijkstra.py&usg=AOvVaw0f5FtOBSHGuVpMNI0-koVU
    already_visited = set()
    already_visited_cc = set()
    d = {s: 0}
    p = {}
    suivants = [(0, s)]

    while suivants != []:
        dx, x = heappop(suivants)
        if x in already_visited:
            continue

        already_visited.add(x)
        already_visited_cc.add((x[0], x[1]))
        for w, y in neigbbor_func(*x):
            # print(x, w, y)
            if t in already_visited:
                continue
            dy = dx + w
            if y not in d or d[y] > dy:
                d[y] = dy
                heappush(suivants, (dy, y))
                p[y] = x

    return d, p


distances, p = dijkstra(
    (0, 0, 0, 0, 0), (len(city_blocks) - 1, len(city_blocks[0]) - 1), neighbor_p1
)

min_d = 99999999999999999

for coord in distances:
    if coord[0] == len(city_blocks) - 1 and coord[1] == len(city_blocks[0]) - 1:
        min_d = min(distances[coord], min_d)

print("part 1", min_d)

distances, p = dijkstra(
    (0, 0, -1, 0, 5), (len(city_blocks) - 1, len(city_blocks[0]) - 1), neighbor_p2
)

min_d = []
min_coord = None
for coord in distances:
    if coord[0] == len(city_blocks) - 1 and coord[1] == len(city_blocks[0]) - 1:
        min_d.append(distances[coord])

min_d.sort()

print("part 2 answer is in here probably", min_d)
