import csv
from faker import Faker
import random
import datetime

# Ініціалізуємо генератор випадкових даних
fake = Faker()

def generate_name_surname(gender):
    if(gender == 'Male'):
        male_surnames = [
            "Smith","Johnson","Brown","Davis","Wilson","Jones","Miller","Taylor",
            "Anderson","Thomas","Jackson","White","Harris","Martin","Thompson"
        ]
        male_names = [
            "James","John","Robert","Michael","William","David","Richard","Joseph",
            "Charles","Thomas","Daniel","Matthew","Anthony","Donald","Paul"
        ]
        surname = random.choice(male_surnames)
        name = random.choice(male_names)
        return surname, name
    else:
        female_first_names = [
            "Mary","Jennifer","Linda","Patricia","Elizabeth","Susan","Jessica",
            "Sarah","Karen","Nancy","Lisa","Margaret","Betty","Dorothy","Sandra"
        ]

        female_last_names = [
            "Smith","Johnson","Brown","Davis","Wilson","Jones","Miller","Taylor",
            "Anderson","Thomas","Jackson","White","Harris","Martin","Thompson"
        ]
        surname = random.choice(female_last_names)
        name = random.choice(female_first_names)
        return surname, name


def generate_by_gender_the_father_name(gender):
    if(gender == 'Male'):
        father_name = [
            "Mykolayovych","Volodymyrovych","Oleksandrovych","Ivanovych",
            "Vasyliovych","Serhiyovych","Viktorovych","Mykhailovych"
        ]
        return random.choice(father_name)
    else:
        father_name = [
            "Mykolaivna","Volodymyrivna","Olexandrivna","Ivanivna",
            "Vasylivna","Serhiivna","Viktorivna","Mykhailivna"
        ]
        return random.choice(father_name)

# Функція для генерації випадкової дати народження
def generate_birthdate():
    start_date = datetime.date(1938, 1, 1)
    end_date = datetime.date(2008, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Відкриваємо файл для запису з вказанням кодування
with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Surname', 'Name', 'Father`s name', 'Gender', 'Data of birth', 'Position', 'Place', 'Address',
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
        surname, name = generate_name_surname(gender)

        writer.writerow({
            'Surname': surname,
            'Name': name,
            'Father`s name': generate_by_gender_the_father_name(gender),
            'Gender': gender,
            'Data of birth': generate_birthdate(),
            'Position': fake.job(),
            'Place': fake.city(),
            'Address': fake.address(),
            'Telephone': fake.phone_number(),
            'Email': fake.email()
        })

print("Готово. Файл employees.csv створено з успіхом.")
