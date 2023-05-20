# Структура, представляющая товар
class Product:
    def init(self, _id, _price, _quantity):
        self.id = _id  # Идентификатор товара
        self.price = _price  # Цена товара
        self.quantity = _quantity  # Количество товара

# Функция для генерации всех возможных вариантов списков товаров скидок
def generate_discount_lists(products, discount_list, current_index, remaining_quantity):
    # Базовый случай: все товары в списке скидок уже выбраны
    if current_index == len(products):
        # Выводим список товаров скидок
        for product in discount_list:
            print(product.id, end=" ")
        print()
        return

    # Рекурсивно генерируем все возможные комбинации
    for i in range(remaining_quantity + 1):
        # Устанавливаем количество текущего товара в списке скидок
        discount_list[current_index] = i

        # Рекурсивно генерируем остальные товары в списке скидок
        generate_discount_lists(products, discount_list, current_index + 1, remaining_quantity - i)

# Ввод количества товаров и максимального количества товаров для каждого артикула
num_products = int(input("Введите количество товаров: "))
max_quantity = int(input("Введите максимальное количество товаров для каждого артикула: "))

# Создаем список товаров
products = []
for i in range(1, num_products + 1):
    price = int(input("Введите цену товара {}: ".format(i)))
    quantity = int(input("Введите количество товара {}: ".format(i)))
    products.append(Product(i, price, quantity))

# Создаем список для хранения списка скидок
discount_list = [0] * num_products

# Генерируем все возможные варианты списков товаров скидок
generate_discount_lists(products, discount_list, 0, max_quantity)
