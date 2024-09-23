import numpy as np
import math

def cot(x):
    return 1 / math.tan(x)


# Інтервал та крок
a = 3
b = 6
h = 0.2

# Функції
def func1(x):
    return math.log(x) - math.cos(x)

def func2(x):
    return math.sin(x) + x**2

def func3(x):
    return math.exp(x) - x

# Табуляція
x_values = np.arange(a, b + h, h)

# Обчислення значень функцій
for x in x_values:
    if x < 4:
        y = func1(x)
    elif 4 <= x < 5:
        y = func2(x)
    else:
        y = func3(x)
    print(f"x = {x:.1f}, y = {y:.5f}")