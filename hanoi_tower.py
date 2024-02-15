def hanoi_tower(n, source, target, auxiliary):
    """
    Функція для рекурсивного розв'язання головоломки "Ханойська вежа"
    
    :param n: Кількість дисків
    :param source: Початковий кілочок
    :param target: Кінцевий кілочок
    :param auxiliary: Допоміжний кілочок
    """
    if n == 1:
        print(f"Переміщення диска з {source} на {target}")
        return
    hanoi_tower(n-1, source, auxiliary, target)
    print(f"Переміщення диска з {source} на {target}")
    hanoi_tower(n-1, auxiliary, target, source)

# Приклад використання
n = 3  # Кількість дисків
hanoi_tower(n, 'A', 'C', 'B')  # 'A', 'B', 'C' - назви кілочків
