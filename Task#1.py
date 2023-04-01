# Заполните массив элементами арифметической прогрессии. Её
# первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = int(input("Enter first number: "))
d = int(input("Enter second number: "))
n = int(input("Enter third number: "))
def deg(a1, d, n):
    if d == 0:
        return a1
    else:
        return a1 + (n - 1) * d
print(deg(a1, d, n))