import os

os.startfile(r'say_hi.jpg')
stock = {1000: 22, 500: 55, 200: 75, 100: 65, 50: 32, 10: 45}
result = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 10: 0}
money = int(input('Введите сумму, которую хотите снять: '))
for key in stock.keys():
    current = money // key  
    if current > stock[key]:
        money = money - (stock[key] * key)
        result[key] = stock[key]
    else:
        money = money % key
        result[key] = current
print("Your money : " + str(sum([k * v for k, v in zip(result.keys(), result.values())])))
print(result)