def get_cats_info(path):
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
    except Exception as e:
        print(f"Виникла помилка: {e}")

    return cats_list

def print_cats_info(cats_info):
    print("[")

    for cat in cats_info:
        print(f"    {cat},")
    
    print("]")

# Приклад використання
cats_info = get_cats_info("cats_file.txt")
print_cats_info(cats_info)
