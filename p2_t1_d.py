#Решить квадратное уравнение с коэффициентами, вводимыми с клавиатуры. Учесть разные случаи: нет корней, один корень, два корня. Вывести корни на экран.
import math 
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0: 
    print(-b / (2 * a))  
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep = '\n')