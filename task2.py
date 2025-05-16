import json  # Підключаємо модуль JSON

# Створено порожній словник contacts для збереження імен і номерів
contacts = {}

# Починаємо цикл, щоб вводити контакти
while True:
    name = input("Введіть ім'я (або натисніть Enter для завершення): ")
    if name == "":
        break  # Якщо ім'я порожнє — виходимо з циклу
    phone = input("Введіть номер телефону: ")
    contacts[name] = phone  # Додаємо пару "ім'я: номер" у словник

# Записуємо словник у файл contacts.json
with open("contacts.json", "w", encoding="utf-8") as file:
    json.dump(contacts, file, ensure_ascii=False, indent=4)

print("Контакти збережено.")

# Завантаження і вивід збережених контактів
with open("contacts.json", "r", encoding="utf-8") as file:
    loaded_contacts = json.load(file)

print("Завантажені контакти:")
print(loaded_contacts)
