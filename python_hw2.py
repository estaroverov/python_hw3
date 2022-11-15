import math
# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
numbers = input("Введите числа через пробел: ").split()


def ListOddSum(numbers):
    counter = 0
    sum = 0
    for i in numbers:
        if counter % 2 != 0:
            sum += int(i)
        counter += 1
    return sum


print("Summ: ", ListOddSum(numbers))

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def CalcMultPairs(numbers):
    counter = 0
    multList = []
    while counter < len(numbers)/2:
        multPair = int(numbers[counter])*int(numbers[len(numbers)-1-counter])
        multList.append(multPair)
        counter += 1
    return multList


print("Multiple pairs:", CalcMultPairs(numbers))

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
numbers = input("Введите вещественные числа через пробел: ").split()


def DiffMinMaxFract(numbers):
    fractList = []
    for i in numbers:
        fract = float(i)-math.floor(float(i))
        fractList.append(fract)
    minFract = fractList[0]
    maxFract = fractList[1]
    for i in fractList:
        if i < minFract:
            minFract = i
        if i > maxFract:
            maxFract = i
    return round(maxFract - minFract, 3)


print("Fract diff: ", DiffMinMaxFract(numbers))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input("Введите число: "))


def DecToBinary(number, base):
    binNumber = ""
    while (number >= base):
        binNumber += str(number % base)
        number = math.floor(number/base)
    return binNumber+"1"


print(DecToBinary(number, 2)[::-1])

# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

number = int(input("Введите число: "))


def NegaFibo(number):
    fiboList = [0,1]
    fibo = [0, 1]
    counter = 2
    while counter <= number:
        if counter == 2:
            fibo.append(fibo[0]+fibo[1])
        else:
            fibo.append(fibo[-2]+fibo[-1])
        fiboList.append(pow(-1, counter+1)*fibo[-1])
        counter += 1
    return fiboList[:0:-1]+fibo


print(NegaFibo(number))
