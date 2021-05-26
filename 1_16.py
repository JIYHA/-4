import random
import datetime
import itertools

teams = ['Испания', 'Чехия', 'Франция', 'Великобритания', 'Германия', 'Швеция', 'Дания', 'Россия', 
		  'Греция', 'Бельгия', 'Ямайка', 'Аргентина', 'Уругвай', 'Турция', 'Португалия', 'Бразилия']
random.shuffle(teams)
teams = [teams[i*4:i*4+4] for i in range(0, 4)]
groups = [i for i in itertools.combinations(teams, 4)]
[print('Номер группы', i+1, groups[0][i]) for i in range(0, 4)]

now = datetime.datetime.now()
start = datetime.datetime(now.year, 9, 14, 22, 45)
for i in range(1, 16):
    print('Номер игры', i, start.strftime('%d/%m/%Y %H:%M'))
    start += datetime.timedelta(days=14)