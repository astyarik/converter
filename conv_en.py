print("Select an action:")
print("1. Celsius to Kelvin.")
print("2. Kelvin to Celsius.")
print("3. Rubles to Hryvnias.")
print("4. Hryvnias to Rubles.")
print("5. Meters to Kilometers.")
print("6. Kilometers to Meters.")
print("7. Exit.")

while True:
    try:
        input_code = move = int(input())
    except ValueError:
        print("Invalid number! Please try again!")

    if move == 1:
        print("Celsius to Kelvin converter selected")
        numb = float(input("Enter the number to convert: "))
        answer = numb + 273.15
        print("That equals", round(answer, 2), "Kelvin!")
        continue

    if move == 2:
        print("Kelvin to Celsius converter selected")
        numb = float(input("Enter the number to convert: "))
        answer = numb - 273.15
        print("That equals", round(answer, 2), "Celsius!")
        continue

    if move == 3:
        print("Rubles to Hryvnias converter selected")
        print("Exchange rate as of 30.12.2025! (1 RUB = 0.5397 UAH)")
        numb = float(input("Enter the number to convert: "))
        answer = numb * 0.5397
        print("That equals", round(answer, 2), "Hryvnias!")
        continue

    if move == 4:
        print("Hryvnias to Rubles converter selected")
        print("Exchange rate as of 30.12.2025! (1 UAH = 1.85 RUB)")
        numb = float(input("Enter the number to convert: "))
        answer = numb / 0.5397
        print("That equals", round(answer, 2), "Rubles!")
        continue

    if move == 5:
        print("Meters to Kilometers converter selected")
        numb = float(input("Enter the number to convert: "))
        answer = numb / 1000
        print("That equals", round(answer, 2), "Kilometers!")

    if move == 6:
        print("Kilometers to Meters converter selected")
        numb = float(input("Enter the number to convert: "))
        answer = numb * 1000
        print("That equals", round(answer, 2), "Meters!")

    if move == 7:
        print("Exiting...")
        break

    else:
        print("Incorrect number! Please try again!")
        continue
