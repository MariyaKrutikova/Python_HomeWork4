# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint
N = int(input("Укажите количество элементов первого набора целых чисел: "))
M = int(input("Укажите количество элементов второго набора целых чисел: "))

list_1 = [randint(0, 10) for _ in range(0, N)]
list_2 = [randint(0, 10) for _ in range(0, M)]

print(list_1)
print(list_2)
print()

set_1 = set(list_1)
set_2 = set(list_2)

print(set_1)
print(set_2)
print()

set_3 = set_1.intersection(set_2)
print(set_3)
print()

list_3 = list(set_3)
print(list_3)
print()

list_3.sort()
print(list_3)


# Эталонное решение:
# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]

# set_1 = set()
# set_2 = set()
# list_1 = list()

# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# print(set_1)


# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# print(set_2)

# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
# print(kool)


