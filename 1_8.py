import random
import math
import array
numbers = array.array('i', [random.randint(1, 9) for _ in range(1, random.randint(1, 10) + 1)])
two = math.ceil(math.log(len(numbers), 2))
print("Длина массива {}\n{}".format(len(numbers), numbers))
print("Степень двойки: {}\nДвойка в этой степени {}\nСколько надо добавить: {}".format(two, 2 ** two, 2 ** two - len(numbers)))
numbers += array.array('i', [0] * (2 ** two - len(numbers)))
print(numbers)