import math

# Функція для обчислення одного члена ряду
def series_term(k, x):
    pryklad1 = (-1)**k * k * math.sin(k * x)
    pryklad2 = k**2 - 1
    return pryklad1 / pryklad2

# Функція для обчислення суми ряду з заданою похибкою d
def series_sum(x, d=0.01):
    total_sum = 0
    k = 2
    term = series_term(k, x)
    
    # Додаємо терміни до тих пір, поки термін за абсолютним значенням більший за похибку
    while abs(term) > d:
        total_sum += term
        k += 1
        term = series_term(k, x)
    
    return total_sum

a = -1
b = 1
h = 0.2
d = 0.001

# Обчислення значень ряду для кожного x в інтервалі з кроком h
x_values = [round(a + i * h, 2) for i in range(int((b - a) / h) + 1)]

# Виведення результатів для кожного значення x
for x in x_values:
    result = series_sum(x, d)
    print(f"x = {x:.2f}, сума ряду = {result:.5f}")
