# Вывести на экран, из каких простых множителей состоит введенное с клавиатуры натуральное число.

a = int(input())
factors = []
for t in range(1, a + 1):
  if a % t == 0:
    factors.append(t)
print(factors)