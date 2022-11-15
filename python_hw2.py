numbers = input("Введите числа через пробел: ").split()

def ListOddSum(numbers):
    counter = 0
    sum = 0
    for i in numbers:
        if counter % 2 != 0:
            sum += int(i)
        counter += 1
    return sum

print(ListOddSum(numbers))