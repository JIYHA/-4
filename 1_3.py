while True:
    try:
        number = (input("Введите номер карты(16 цифр): "))
        if not len(number) == 16 or not number.isdigit():
            raise ValueError
    except ValueError as e:
        print("Невереный формат")
    else:
        print(number[:4] + '*' * 8 + number[-4:])