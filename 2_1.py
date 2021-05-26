 file = open('task1_lirics.txt', 'r')
 text = file.read()
 text_firstOnly = ''
 file.close()
 frequency = []
 symbol = []

 for i in range(len(text)):
     if text[i].isalpha():
         if text[i].isupper():
             text_firstOnly += text[i].lower()
         else:
             text_firstOnly += text[i]
 for i in range(len(text_firstOnly)):
     if symbol.count(text_firstOnly[i]) == 0:
         frequency.append(text_firstOnly.count(text_firstOnly[i]))
         symbol.append(text_firstOnly[i])
 print(frequency)
 print(symbol)

 for i in range(len(symbol)):
     k = frequency.index(max(frequency))
     print('Символ: {0} встречается {1} раз(а)'.format(symbol[k], max(frequency)))
     symbol.remove(symbol[k])
     frequency.remove(frequency[k])