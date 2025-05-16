import json  # Імпортуємо модуль для роботи з JSON

# Створено змінну name для збереження імені гравця, яке вводить користувач
name = input("Введіть ім'я гравця: ")

# Створено змінну wins для збереження кількості перемог
wins = int(input("Скільки перемог?: "))

# Створено змінну losses для збереження кількості поразок
losses = int(input("Скільки поразок?: "))

# Створено словник player_stats для зберігання статистики гравця
player_stats = {
    "ім'я": name,
    "перемоги": wins,
    "поразки": losses
}

# Відкриваємо файл для запису та зберігаємо словник у форматі JSON
with open("game_stats.json", "w", encoding="utf-8") as file:
    json.dump(player_stats, file, ensure_ascii=False, indent=4)

print("Статистика гравця збережена.")

