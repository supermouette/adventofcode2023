import matplotlib.pyplot as plt
from time import time

with open("data.txt") as f:
    y_real = eval(f.readline())

x = list(range(len(y_real)))

# plt.plot(x, y_real)
# plt.show()
print(y_real[:5])
y_diff = [y_real[i] - y_real[i - 1] for i in range(1, len(y_real))]
print(y_diff[:5])
# plt.plot(x[:-1], y_diff)
print(y_diff[-1] / x[-2])

FIRST_COEF = y_diff[914] / x[914]
"""
plt.plot(x, [i * FIRST_COEF for i in x])
plt.show()
"""
estim_diff = [i * FIRST_COEF - y_diff[i] for i in range(len(y_diff))]
"""
plt.plot(x[:-1], estim_diff)
plt.show()
"""
pic1 = 62
pic2 = 324

T = 324 - 62
print(T)

first_period = estim_diff[:T]
second_period = estim_diff[T : 2 * T]
third_period = estim_diff[2 * T : 3 * T]
fourth_period = estim_diff[3 * T : 4 * T]
"""
plt.plot(list(range(T)), first_period)
plt.plot(list(range(T)), second_period)
plt.plot(list(range(T)), third_period)
plt.plot(list(range(len(fourth_period))), fourth_period)


plt.show()
"""
print(
    second_period[97] - first_period[97],
    third_period[97] - second_period[97],
    fourth_period[97] - third_period[97],
)


diff_period = [second_period[i] - first_period[i] for i in range(len(first_period))]

"""
plt.plot(
    list(range(T)),
    [first_period[i] + 3 * diff_period[i] for i in range(len(first_period))],
)
plt.plot(list(range(len(fourth_period))), fourth_period)
plt.show()
"""


def diff_function(i):
    return FIRST_COEF * i - first_period[i % T] - (i // T) * diff_period[i % T]


"""
plt.plot(list(range(1300)), [diff_function(i) for i in range(1300)])
plt.plot(x[:-1], y_diff)
plt.show()
"""


def generate_function_up_to(f0, n):
    seq = [f0]
    for i in range(1, n):
        seq.append(seq[-1] + diff_function(i))
    return seq


plt.plot(list(range(1, 1201)), generate_function_up_to(y_real[0], 1200), color="red")
plt.plot(x, y_real, color="blue")
plt.show()

print(generate_function_up_to(y_real[1], 70)[64 - 1])
t0 = time()
print(int(generate_function_up_to(y_real[1], 26501370)[26501365 - 1]))
print(time() - t0)
