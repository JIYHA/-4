s = input("Введите текст: ")
lst = "".join([" " if not i.isalnum() else i for i in s]).split()
result = " ".join([i.upper() if i.istitle() else i for i in lst])
print(result)