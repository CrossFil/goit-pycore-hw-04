def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ідентифікатор, ім'я та вік кота
                cat_data = line.strip().split(',')
                
                # Перевіряємо, чи кожен рядок має правильний формат (ідентифікатор, ім'я, вік)
                if len(cat_data) == 3:
                    cat_info = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_list.append(cat_info)
                else:
                    print(f"Неправильний формат рядка: {line}")

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []

    return cats_list

# Функція для виведення списку котів у форматі, як у завданні
def print_cats_info(cats_info):
    print("[")

    for cat in cats_info:
        print(f"    {cat},")
    
    print("]")

# Приклад використання
cats_info = get_cats_info("cats_file.txt")
print_cats_info(cats_info)
