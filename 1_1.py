try:
    s = (input("Введите вещественное число: "))
    if float(s) < 0:
        raise ValueError
except ValueError as e:
    print("Некорректный формат", e)
else:
    res = s.split(".")
    print("{} руб. {} коп.".format(res[0], res[1]))