print("Выберите действие:")
print("1. Из Цельсия в Кельвины.")
print("2. Из Кельвина в Цельсии.")
print("3. Из Рублей в Гривны.")
print("4. Из Гривен в Рубли.")
print("5. Выход.")

while True:
    try:
        input_code = move = int(input())
    except ValueError:
        print("Некорректное число! Попробуйте снова!")

    if move == 1:
        print("Выбран конвертер Цельсий в Кельвины")
        numb = float(input("Введите конвертируемое число:"))
        answer = numb - 273.15
        print(f"И это равняется", round(answer, 2), "Кельвинов!")
        continue
    if move == 2:
        print("Выбран конвертер из Кельвинов в Цельсия")
        numb = float(input("Введите конвертируемое число:"))
        answer = numb + 273.15
        print(f"И это равняется", round(answer, 2), "Кельвинов!")
        continue
    if move == 3:
        print("Выбран конвертер Рублей в Гривны")
        print("Данные курса на момент 30.12.2025! (1 руб. = 0.5397 грн.)")
        numb = float(input("Введите конвертируемое число:"))
        answer = numb * 0.5397
        print(f"И это равняется ", round(answer, 2), " Гривен!")
        continue
    if move == 4:
        print("Выбран конвертер Рублей в Гривны")
        print("Данные курса на момент 30.12.2025! (1 грн. = 1,85 руб.)")
        numb = float(input("Введите конвертируемое число:"))
        answer = numb / 0.5397
        print(f"И это равняется ", round(answer, 2), " Гривен!")
        continue
    if move == 5:
        print("Выход...")
        break
    else:
        print("Неверное число! Попробуйте снова!")
        continue
