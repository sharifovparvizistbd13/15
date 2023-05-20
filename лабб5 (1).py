
import math
import time

# Рекурсивное вычисление функции F(n)
def recursive_F(n):
    if n == 1:
        return 1
    else:
        return 2 * recursive_F(n-1) * recursive_G(n-1)

# Рекурсивное вычисление функции G(n)
def recursive_G(n):
    if n == 1:
        return 1
    else:
        return recursive_F(n-1) + math.sin(n)

# Итерационное вычисление функции F(n)
def iterative_F(n):
    f_prev = 1
    g_prev = 1

    for i in range(2, n+1):
        f_curr = 2 * f_prev * g_prev
        g_curr = f_prev + math.sin(i)

        f_prev = f_curr
        g_prev = g_curr

    return f_prev

# Тестирование программы
n = int(input("Введите значение n: "))

# Рекурсивное вычисление
start_time = time.time()
recursive_result = recursive_F(n)
recursive_time = time.time() - start_time

# Итерационное вычисление
start_time = time.time()
iterative_result = iterative_F(n)
iterative_time = time.time() - start_time

# Вывод результатов
print(f"Рекурсивное вычисление: F({n}) = {recursive_result}")
print(f"Время выполнения рекурсивного вычисления: {recursive_time} секунд")
print(f"Итерационное вычисление: F({n}) = {iterative_result}")
print(f"Время выполнения итерационного вычисления: {iterative_time} секунд")
