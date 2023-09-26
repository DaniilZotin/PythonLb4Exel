import csv
from faker import Faker
import random
import datetime

# Ініціалізуємо генератор випадкових даних
fake = Faker()

# Функція для генерації випадкової дати народження
def generate_birthdate():
    start_date = datetime.date(1938, 1, 1)
    end_date = datetime.date(2008, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Відкриваємо файл для запису з вказанням кодування
with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Surname', 'Name', 'Gender', 'Data of birth', 'Position', 'Place', 'Address',
                  'Telephone', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Записуємо заголовок
    writer.writeheader()

    # Кількість записів
    total_records = 2000
    female_percentage = 0.4
    male_percentage = 0.6

    # Генеруємо записи
    for i in range(total_records):
        gender = 'Male' if random.random() < male_percentage else 'Female'
        surname = fake.last_name()
        name = fake.first_name()

        writer.writerow({
            'Surname': surname,
            'Name': name,
            'Gender': gender,
            'Data of birth': generate_birthdate(),
            'Position': fake.job(),
            'Place': fake.city(),
            'Address': fake.address(),
            'Telephone': fake.phone_number(),
            'Email': fake.email()
        })

print("Готово. Файл employees.csv створено з успіхом.")
