text = input("Введите текст: ")
for i in text:
    if text.count(i) == 1:
        print(i)