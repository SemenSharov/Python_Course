# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = input("Введите натуральное число больше 1 :")

status = True

fib1 = 0
fib2 = 1
i = 2

while status:
    result = fib1 + fib2
    fib1 = fib2
    fib2 = result
    i = i + 1

    if a == result:
        print(i)
        status = False
    elif result > a:
        print(-i)
        status = False
