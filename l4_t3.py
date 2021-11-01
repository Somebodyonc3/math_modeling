#в задаче 'Тело брошенное под углом' опущен главный элемент - угол под которым брошенно тело, а это меняет многое;)

from l4_const import g
from math import sin, cos
import numpy

print('Введите начальное положение в метрах:')
x0 = float(input())
print('Введите начальную высоту в метрах:')
y0 = float(input())
print('Введите начальную скорость, м/с:')
v0 = float(input())
if v0 == 0:
    print('И в школу не надо ходить, чтоб знать ответ:)')
    exit()
print('Под каким углом тело должно лететь?, в градусах:')
a = int(input())
if a == 0:
    print('Зачем ты хочешь решить задачу <<Тело брошенное под углом>> без угла?')
    exit()
print('Сколько тело будет лететь, в секундах:')
n = int(input())
if n == 0:
  print('Ты в пустую тратишь мое время')
  exit()
print('Решаем вашу задачу. Придется немного подождать. Можете попить чайку;)')

answers = []
for t in range(0, n + 1):
    x = round(abs(x0 + v0 * cos(a) * t))
    y = round(abs(y0 + v0 * sin(a) * t - ((g * t ** 2) / 2)))
    answers.append(t)
    answers.append(x)
    answers.append(y)

b = numpy.array(answers)
print(b)


