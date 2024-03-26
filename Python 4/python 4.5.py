purchase_dict = {}
# Вводим количество записей о покупках
n = int(input("Введите количество записей о покупках: "))
# Считываем данные о покупках
for _ in range(n):
    entry = input().split()
    buyer_id = int(entry[0])
    product = entry[1]
    quantity = int(entry[2])

    # Обновляем словарь покупок
    if buyer_id in purchase_dict:
        if product in purchase_dict[buyer_id]:
            purchase_dict[buyer_id][product] += quantity
        else:
            purchase_dict[buyer_id][product] = quantity
    else:
        purchase_dict[buyer_id] = {product: quantity}

# Выводим список покупок для каждого покупателя
for buyer_id, purchases in purchase_dict.items():
    print(f"Покупатель {buyer_id}:")
    for product, quantity in purchases.items():
        print(f"Товар: {product}, Количество: {quantity}")