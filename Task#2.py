# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
min = int(input("Enter first number: "))
max = int(input("Enter second number: "))
for i in range(len(list)):
    if min <= list[i] <= max:
        print(i)