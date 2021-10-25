# Вывести на экран таблицу умножения 9X9, следующим образом:

for i in range(1, 10):
    for j in range(1, 10):
        print("%4d" % (i * j), end = ' ')
    print()