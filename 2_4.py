# начинается с 83, остальные 3 цифры не важны, дальше должна быть запятая и название города, до пробела


import re
pattern = re.compile("83\d{3}, \D+ ")
content = ''
matches = []
path = input('Введите название файла')
try:
    file = open('E:\\Python\\Lab2\\' + path, 'r', encoding='UTF-8')
    content = file.read().replace('\n', ' ')
    file.close()
except FileNotFoundError as e:
    print('File does not exist. ', e.args)

print(content)

result = re.findall(pattern, content)
print(result)