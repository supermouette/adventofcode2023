input = [[53, 275], [71, 1181], [78, 1215], [80, 1524]]
test = [[7, 9], [15, 40], [30, 200]]

p1_result = 1

for t, d in input:
    possible_win = 0
    for x in range(t + 1):
        if (t - x) * x > d:
            possible_win += 1
    p1_result *= possible_win

print(p1_result)


p2_input = [[53717880, 275118112151524]]
p2_test = [[71530, 940200]]


possible_win = 0

for t, d in p2_input:
    for x in range(t + 1):
        if (t - x) * x > d:
            possible_win += 1

print(possible_win)

# best way : -x**2 + tx -d = 0 is a 2nd degree polynomial, so roots are
# delta = t**2 - 4 * d
# x1 = 0.5 * (t - (delta) ** 0.5)
# x2 = 0.5 * (t + (delta) ** 0.5)
# possible_win = int(x2 - x1)
# print(possible_win)
