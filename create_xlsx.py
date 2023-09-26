import csv
from faker import Faker
import datetime
from openpyxl import Workbook

# Ініціалізуємо генератор випадкових даних
fake = Faker()

# Функція для генерації випадкової дати народження
def generate_birthdate():
    start_date = datetime.date(1938, 1, 1)
    end_date = datetime.date(2008, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

try:
    with open('employees.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Створюємо нову книгу Excel
        wb = Workbook()
        ws_all = wb.active
        ws_all.title = "all"

        # Створюємо аркуші для різних категорій віку
        age_categories = ['younger_18', '18-45', '45-70', 'older_70']
        for category in age_categories:
            ws = wb.create_sheet(title=category)
            ws.append(['№', 'Прізвище', 'Ім’я', 'Дата народження', 'Вік'])

        # Записуємо заголовок на аркуш "all"
        all_headers = ['№', 'Прізвище', 'Ім’я', 'Дата народження', 'Вік']
        ws_all.append(all_headers)

        # Додавання данних на аркуш "all" і відповідні аркуші за категоріями віку
        for idx, row in enumerate(reader, start=1):
            surname = row['Surname']
            name = row['Name']
            birthdate = row['Data of birth']
            age = datetime.date.today().year - datetime.datetime.strptime(birthdate, '%Y-%m-%d').year

            # Записуємо дані на аркуш "all"
            ws_all.append([idx, surname, name, birthdate, age])

            # Додавання даних на відповідні аркуші за категоріями віку
            if age < 18:
                ws = wb['younger_18']
            elif 18 <= age <= 45:
                ws = wb['18-45']
            elif 45 < age <= 70:
                ws = wb['45-70']
            else:
                ws = wb['older_70']

            # Записуємо дані на відповідний аркуш
            ws.append([idx, surname, name, birthdate, age])

        # Зберігаємо результати у файл Excel
        wb.save('employees.xlsx')

    print("Готово. Файл employees.xlsx створено з успіхом.")

except FileNotFoundError:
    print("Sorry we cannot find the file employees.csv")
except PermissionError:
    print("Your file is open now, please close file")



