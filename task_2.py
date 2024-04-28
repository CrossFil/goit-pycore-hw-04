"""Home work #2"""
from pprint import pprint

def get_cats_info(path):
    """функція виведення інформації про котів"""
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ідентифікатор, ім'я та вік кота
                cat_id, name, age = line.strip().split(',')

                # Створюємо словник з інформацією про кота та додаємо його до списку
                cat_info = {"id": cat_id, "name": name, "age": age}
                cats_list.append(cat_info)
    except FileNotFoundError:
        print("Файл не знайдено.")
    return cats_list

cats_info = get_cats_info("cats_file.txt")
pprint(cats_info)
