# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

numbers = int(input())
a = 2
result = 1

for i in range(numbers):
    result = result * a
    if result < numbers:
        print(result)
