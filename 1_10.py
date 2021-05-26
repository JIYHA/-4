password = input("Введите пароль: ")
password1 = ""
if len(password) < 4:
     d = "Недопустимый пароль"
     print(d)
elif password.isdigit():
    d = "Ненадежный пароль"
    print(d)
if len(password) == 7:
   d = "Ненадежный пароль"
   print(d)
while True:
     for i in (password):
         if i.isupper() + i.islower():
            d = "Надежный пароль"
            print(d)
            exit(0)