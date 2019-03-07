from random import choice


def fetch_user_input():
    return map(lambda x: int(x), input('Введите числа через пробел:\n').split(' '))


def modified_quick_sort(array):
    even = []
    uneven = []

    for elem in array:
        if elem % 2:
            uneven.append(elem)
        else:
            even.append(elem)

    return quick_sort(even) + quick_sort(uneven)[::-1]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = choice(array)

    left = []
    middle = []
    right = []

    for elem in array:
        if elem < pivot:
            left.append(elem)
        elif elem > pivot:
            right.append(elem)
        else:
            middle.append(elem)

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    n = int(input('Введите количество чисел в массиве:\n'))

    initial_array = list(fetch_user_input())

    if len(initial_array) == n:
        print('Отсортированный массив:\n', *modified_quick_sort(initial_array))
    else:
        print('Количество чисел в массиве не совпадает с указанным.')


