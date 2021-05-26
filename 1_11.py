  def frange(start, end, step):
    while start < end:
        yield round(start, 3)
        start += step


for i in frange(1, 6, 0.1):
    print(i)