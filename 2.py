# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: 6, 13
# [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
print('Введите диапазон поиска:')
a = int(input('От: '))
b = int(input('До: '))
print('Включительно.')

list = []
for i in range(20):
     list.append(randint(a-10,b+10))
print("Ищим в списке: ",list)

loot = []
for i in range(20):
     if a <= list[i] <= b:
        loot.append(i)
print("Значения найдены по индексам: ",loot)
