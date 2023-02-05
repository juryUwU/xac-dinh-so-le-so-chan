import random
x = random.randint(1,100)
y = random.randint(1,100)
if x%2 == 0 and y%2 == 0:
    print(x, y, "đều là số chẵn")
if x%2 != 0 and y%2 != 0:
    print(x, y, "đều là số lẻ")