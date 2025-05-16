import json  # Підключаємо модуль JSON
import os    # Для перевірки існування файлу

# Створено список clients для зберігання клієнтів
# Якщо файл існує — завантажуємо з нього, інакше — створюємо порожній список
if os.path.exists("clients.json"):
    with open("clients.json", "r", encoding="utf-8") as file:
        clients = json.load(file)
else:
    clients = []

# Основне меню
while True:
    print("\nМеню:")
    print("1. Додати клієнта")
    print("2. Пошук клієнта")
    print("3. Оновити клієнта")
    print("4. Видалити клієнта")
    print("5. Вийти")

    choice = input("Ваш вибір: ")  # Вибір користувача

    if choice == "1":
        name = input("Введіть ім'я клієнта: ")
        email = input("Введіть email клієнта: ")
        clients.append({"ім'я": name, "email": email})  # Додаємо до списку
        print("Клієнта додано.")

    elif choice == "2":
        search = input("Введіть ім'я для пошуку: ")
        found = False
        for client in clients:
            if client["ім'я"].lower() == search.lower():
                print("Знайдено:", client)
                found = True
        if not found:
            print("Клієнта не знайдено.")

    elif choice == "3":
        name = input("Введіть ім'я клієнта для оновлення: ")
        for client in clients:
            if client["ім'я"].lower() == name.lower():
                new_email = input("Введіть новий email: ")
                client["email"] = new_email
                print("Email оновлено.")
                break
        else:
            print("Клієнта не знайдено.")

    elif choice == "4":
        name = input("Введіть ім'я клієнта для видалення: ")
        clients = [c for c in clients if c["ім'я"].lower() != name.lower()]
        print("Клієнта видалено.")

    elif choice == "5":
        break  # Вихід з циклу

    else:
        print("Невірний вибір. Спробуйте ще раз.")

    # Після кожної дії — зберігаємо зміни у файл
    with open("clients.json", "w", encoding="utf-8") as file:
        json.dump(clients, file, ensure_ascii=False, indent=4)
