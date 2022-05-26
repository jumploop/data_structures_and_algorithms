"""
冒泡排序
"""


def bubble_sort(array):
    length = len(array)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return array


if __name__ == '__main__':
    result = bubble_sort([0, 5, 2, 3, 2])
    print(result)