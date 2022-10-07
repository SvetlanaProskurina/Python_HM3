# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

r = int(input("введите десятичное число \n"))
binar = []

while r != 0:
    if r%2==0:
        binar.append(str(0))
        r = r//2
    else:
        binar.append(str(1))
        r = r//2
binar.reverse()
binar_res = ''.join(binar)

print(binar_res)
