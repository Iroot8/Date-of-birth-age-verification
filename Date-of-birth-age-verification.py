from datetime import datetime

print("Проверка возраста по дате рождения")
date_str = input("Дата рождения (ДД.ММ.ГГГГ): ")

try:
    birth = datetime.strptime(date_str, "%d.%m.%Y")
    today = datetime.today()
    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1
    print(f"Ваш возраст: {age} полных лет.")
except:
    print("Ошибка: неверный формат даты.")