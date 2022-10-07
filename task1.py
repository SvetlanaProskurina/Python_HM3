# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint


lst = [2, 3, 5, 9, 3]

# lst = []
# for i in range(11):
#     lst.append(randint(-10,10)) # добавляется новый элемент в список
print(lst)


sum = 0

for n in range(len(lst)):
    if n%2 != 0:
        sum = sum + int(lst[n])
        print("нечетное =",int(lst[n]))
print(sum)