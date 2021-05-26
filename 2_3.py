import os
from glob import glob
import os.path

path = "music"
os.chdir(path)

track = glob('*.mp3')

names = list(filter(None, [text.replace('\n', '') if text is not 'playlist.txt' else None for text in
                                open('playlist.txt', 'r', encoding='UTF-8')]))

cnt = 0
Done = False

for i in range(len(track)):
    try:
        os.rename(track[i], names[i])
        if cnt == len(track) - 1:
            Done = True
        cnt += 1
    except Exception as e:
        print('Error file ' + str(cnt) + ': ', e.args)

if Done:
    print('Я переименовал !!!')
else:
    print('Не вышло (((')
© 2021 GitHub, Inc.