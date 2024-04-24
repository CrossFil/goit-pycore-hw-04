def total_salary(path):
    total_salary = 0
    num_developers = 0

    salaries = [
        "Alex Korp,3000",
        "Nikita Borisenko,2000",
        "Sitarama Raju,1000"
    ]

    # Записуємо ці рядки у файл salaries.txt
    with open("salaries.txt", "w", encoding="utf-8") as file:
        for salary in salaries:
            file.write(salary + "\n")

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # slit in line for name and salary
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)

                total_salary += salary
                num_developers += 1

        if num_developers == 0:
            return 0, 0
        
        average_salary = total_salary / num_developers
        return total_salary, average_salary
    
    except FileNotFoundError:
        print('File not found')
        return None, None

    except Exception as e:
        print(f'Error: {e}')
        return None, None


total, average = total_salary("salaries.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")