def count_consecutive_ones(num):
    binary = bin(num)[2:]  # Получаем двоичное представление числа, исключая префикс '0b'
    consecutive = 0
    start_position = -1

    for i in range(len(binary)):
        if binary[i] == '1':
            if consecutive == 0:
                start_position = i
            consecutive += 1
            if consecutive > 2:
                return -1  # Если найдена серия из более чем двух подряд идущих единиц, возвращаем -1
        else:
            consecutive = 0

    return start_position

# Перебираем все нечетные числа в диапазоне от 1 до 4096
for num in range(1, 4097, 2):
    start_position = count_consecutive_ones(num)

    if start_position != -1:
        digits = [int(digit) for digit in str(num) if digit != '1']
        print(f"Число: {num}")
        print(f"Цифры числа, исключая единицы: {digits}")
        print(f"Номер позиции, с которой начинается серия: {start_position}")
        print()
