#Сформировать из введенного с клавиатуры числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.Подсказка: Для извлечения последней цифры числа надо найти остаток от деления его на 10. Чтобы последнюю цифру из числа убрать, надо найти его целое от деления на 10. Далее все повторяется.

a = int(input())
b = str(a)
print(b[::-1])