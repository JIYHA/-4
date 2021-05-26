lst = [7, 9, 2, 4, 1, 6, 5, 8, 3, 10]
lst = list(range(11))
for i in range(1, len(lst)):
   if lst[i - 1] > lst[i]:
     print("FALSE")
   break
else:
     print("TRUE")