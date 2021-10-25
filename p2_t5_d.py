# Найти все совершенные числа до числа вводимого с клавиатуры. Совершенное число — это такое число, которое равно сумме всех своих делителей, кроме себя самого. Например, число 6 является совершенным, т.к. кроме себя самого делится на числа 1, 2 и 3, которые в сумме дают 6.

a = int(input())
factorednumbers = []
for i in range(1, a):
  factors = []
  for t in range(1, i):
    if i % t == 0:
      factors.append(t)
  if sum(factors) == i:
    factorednumbers.append(i)
print(factorednumbers)


