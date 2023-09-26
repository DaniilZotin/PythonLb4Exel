import csv
import datetime

import matplotlib.pyplot as plt
from collections import defaultdict

# Функція для відкриття файлу CSV і зчитування даних
def read_csv(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        return data
    except FileNotFoundError:
        print("Помилка: Файл CSV не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при відкритті файлу CSV: {str(e)}")
        return None

# Функція для підрахунку кількості співробітників чоловічої і жіночої статі
def count_gender(data):
    male_count = sum(1 for row in data if row['Gender'] == 'Male')
    female_count = len(data) - male_count
    return male_count, female_count

# Функція для підрахунку кількості співробітників в кожній віковій категорії
def count_age_categories(data):
    age_categories = defaultdict(int)
    for row in data:
        age = datetime.date.today().year - datetime.datetime.strptime(row['Data of birth'], '%Y-%m-%d').year
        if age < 18:
            age_categories['younger_18'] += 1
        elif 18 <= age <= 45:
            age_categories['18-45'] += 1
        elif 45 < age <= 70:
            age_categories['45-70'] += 1
        else:
            age_categories['older_70'] += 1
    return age_categories

# Функція для підрахунку кількості співробітників чоловічої та жіночої статі в кожній віковій категорії
def count_gender_by_age(data):
    gender_age_categories = defaultdict(lambda: defaultdict(int))
    for row in data:
        age = datetime.date.today().year - datetime.datetime.strptime(row['Data of birth'], '%Y-%m-%d').year
        gender = row['Gender']
        if age < 18:
            gender_age_categories['younger_18'][gender] += 1
        elif 18 <= age <= 45:
            gender_age_categories['18-45'][gender] += 1
        elif 45 < age <= 70:
            gender_age_categories['45-70'][gender] += 1
        else:
            gender_age_categories['older_70'][gender] += 1
    return gender_age_categories

# Функція для відображення результатів на графіках
def plot_results(data, title):
    labels = data.keys()
    values = data.values()

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel("Категорія")
    plt.ylabel("Кількість")
    plt.show()

if __name__ == "__main__":
    csv_file = 'employees.csv'
    employee_data = read_csv(csv_file)

    if employee_data:
        # Підрахунок кількості співробітників чоловічої і жіночої статі
        male_count, female_count = count_gender(employee_data)
        print(f"Кількість чоловіків: {male_count}")
        print(f"Кількість жінок: {female_count}")

        # Графік для кількості співробітників чоловічої і жіночої статі
        gender_data = {'Male': male_count, 'Female': female_count}
        plot_results(gender_data, "Кількість співробітників за статтю")
        plt.show()

        # Підрахунок кількості співробітників в кожній віковій категорії
        age_categories_count = count_age_categories(employee_data)
        print("Кількість співробітників в кожній віковій категорії:")
        for category, count in age_categories_count.items():
            print(f"{category}: {count}")

        # Графік для кількості співробітників в кожній віковій категорії
        plot_results(age_categories_count, "Кількість співробітників в кожній віковій категорії")
        plt.show()

        # Підрахунок кількості співробітників чоловічої та жіночої статі в кожній віковій категорії
        gender_by_age_categories = count_gender_by_age(employee_data)
        print("Кількість співробітників чоловічої та жіночої статі в кожній віковій категорії:")
        for age_category, gender_count in gender_by_age_categories.items():
            print(f"Вікова категорія: {age_category}")
            for gender, count in gender_count.items():
                print(f"{gender}: {count}")

        # Графіки для кількості співробітників чоловічої та жіночої статі в кожній віковій категорії
        for age_category, gender_count in gender_by_age_categories.items():
            plot_results(gender_count, f"Кількість співробітників за статтю в {age_category} категорії")
            plt.show()

