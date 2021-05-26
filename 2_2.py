import os
import hashlib

path = r'C:\Users\Admin\PycharmProjects\Lab2\Task2_files'
files = os.listdir(path)
number = []
for file in files:
    with open(path + '\\' + file, 'rb') as f:
        content = f.read()
        number.append(hashlib.md5(content).hexdigest())

for i in range(len(files) - 1):
    for j in range(i + 1, len(files)):
        if number[i] == number[j]:
            print(files[i], ' копия это, отвечаю ', files[j])