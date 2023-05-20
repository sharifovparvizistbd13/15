def modify_matrix(A, B, C, E, k):
    # Получение количества чисел больших k в четных столбцах области 1
    count = sum([1 for i in range(0, len(E), 2) if any(num > k for num in E[i][:k])])
    
    # Получение суммы чисел в нечетных строках области 3
    total = sum([sum(E[i][k:]) for i in range(1, len(E), 2)])

    if count > total:
        # Меняем симметрично области 1 и 3 в матрице E
        for i in range(k):
            E[i][::2], E[i+k][1::2] = E[i+k][1::2], E[i][::2]
    else:
        # Меняем несимметрично матрицы B и C
        B, C = C, B

    return A, B, C, E

# Пример входных данных
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
C = [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
E = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

k = 2  # Заданный порог k

# Вызов функции для модификации матриц
A, B, C, E = modify_matrix(A, B, C, E, k)

# Вывод результатов
print("Матрица A:")
for row in A:
    print(row)
print("Матрица B:")
for row in B:
    print(row)
print("Матрица C:")
for row in C:
    print(row)
print("Матрица E:")
for row in E:
    print(row)
