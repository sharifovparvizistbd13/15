import random

# Создание матрицы размером N*N и заполнение значениями из интервала [-10, 10]
def create_matrix(N):
    matrix = []
    for _ in range(N):
        row = [random.randint(-10, 10) for _ in range(N)]
        matrix.append(row)
    return matrix

# Формирование матрицы F
def create_matrix_F(E, B, C, D, K):
    N = len(E)
    F = [[0] * (2*N) for _ in range(2*N)]

    count_even = 0
    sum_odd = 0

    # Подсчет количества чисел больших K в четных столбцах области 1
    for i in range(N // 2):
        for j in range(N // 2):
            if E[i][j] > K:
                count_even += 1

    # Подсчет суммы чисел в нечетных строках области 3
    for i in range(N // 2, N):
        for j in range(N // 2):
            sum_odd += E[i][j]

    # Формирование матрицы F согласно описанным правилам
    if count_even > sum_odd:
        # Поменять в Е симметрично области 1 и 3 местами
        for i in range(N // 2):
            for j in range(N // 2):
                E[i][j], E[i + N // 2][j] = E[i + N // 2][j], E[i][j]
    else:
        # Поменять В и С несимметрично местами
        B, C = C, B

    # Сформировать матрицу F
    for i in range(N):
        for j in range(N):
            F[i][j] = E[i][j]
            F[i][j + N] = B[i][j]
            F[i + N][j] = D[i][j]
            F[i + N][j + N] = C[i][j]

    return F

# Транспонирование матрицы
def transpose_matrix(matrix):
    N = len(matrix)
    transposed = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            transposed[j][i] = matrix[i][j]

    return transposed

# Умножение матрицы на число
def multiply_matrix_by_scalar(matrix, scalar):
    N = len(matrix)
    multiplied = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            multiplied[i][j] = matrix[i][j] * scalar

    return multiplied

# Умножение двух матриц
def multiply_matrices(matrix1, matrix2):
    N = len(matrix1)
    multiplied = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                multiplied[i][j] += matrix1[i][k] * matrix2[k][j]

    return multiplied

# Вывод матрицы на экран
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))

# Тестирование программы
N = int(input("Введите размер матрицы N: "))
K = int(input("Введите значение K: "))

# Создание матрицы A
B = [[1] * (N // 2) for _ in range(N // 2)]
C = [[1] * (N // 2) for _ in range(N // 2)]
D = [[1] * (N // 2) for _ in range(N // 2)]
E = [[1] * (N // 2) for _ in range(N // 2)]

# Формирование матрицы F
F = create_matrix_F(E, B, C, D, K)

# Вычисление выражения А*F - КА^T
A = create_matrix(N)
AT = transpose_matrix(A)
AF = multiply_matrices(A, F)
KAT = multiply_matrix_by_scalar(AT, K)
result = [[AF[i][j] - KAT[i][j] for j in range(N)] for i in range(N)]

# Вывод результатов
print("Матрица A:")
print_matrix(A)
print("\nМатрица F:")
print_matrix(F)
print("\nВыражение А*F - КА^T:")
print_matrix(result)
