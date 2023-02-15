print("Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.")
print("Введите песню")
song = input()
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
parts = song.split()
itog = list()
for item in parts:
    k = 0
    for letter in item:
        if letter in volwes:
            k += 1
    itog.append(k)
if len(set(itog)) == 1:
    print('Парам пам-пам :)')
else:
    print('Пам парам :(')
        
print("Задача 36: Напишите функцию, которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.")

from math import log10

def printOperationTable(operation, numRows=9, numColumns=9):
    if operation(1,1)==2:
        print(1,end='\t')

    colSize = int(log10(operation(numRows+1, numColumns+1)))+2

    for row in range(1, numRows+1):
        for column in range(1, numColumns+1):
            if operation(1,1)==2:
                column=column-1
            print("{:>{}}".format(operation(row,column), colSize), end='\t')
        print()