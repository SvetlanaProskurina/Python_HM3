# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

#lst = [2, 3, 5, 6]

#lst = [2, 3, 4, 5, 6]

#lst = [2, 3, 5, 6, 2, 2, 5] 
lst = []

for i in range(11):
    lst.append(randint(-10,10)) # добавляется новый элемент в список
print(lst)

new_lst = []
sum = 0
m = len(lst)-1
lengt = int(len(lst)/2)

if len(lst)%2 != 0:
    lengt = int(len(lst)/2)+1
else:
    lengt = int(len(lst)/2)
    

for n in range(lengt):
    new_lst.append(lst[n]*lst[m])
    m=m-1
    
print(new_lst)