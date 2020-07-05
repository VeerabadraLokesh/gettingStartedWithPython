import os
import numpy as np
import random


def swap_elements(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def get_median_pivot(arr, start, end):
    middle_point_index = (start+end)//2
    subarr = [arr[start], arr[middle_point_index], arr[end-1]]
    if subarr[0] > subarr[1] and subarr[0] < subarr[2]:
        return start
    elif subarr[1] < subarr[2] and subarr[1] > subarr[0]:
        return middle_point_index
    else:
        return end-1

def quick_sort(arr, start, end, count=0):
    if start >= end:
        return 0
    # pivot_position = start
    # pivot_position = end - 1
    # pivot_position = get_median_pivot(arr, start, end)
    # pivot_position = start + (end - start)//2
    pivot_position = random.randint(start, end-1)
    if pivot_position != start:
        swap_elements(arr, start, pivot_position)
    pivot = arr[start]
    i = start + 1
    j = start + 1
    for j in range(start+1, end):
        if arr[j] < pivot:
            swap_elements(arr, i, j)
            i += 1
    swap_elements(arr, start, i-1)
    # print(start, end, pivot)
    # print(arr)
    count += quick_sort(arr, start, i-1)
    count += quick_sort(arr, i, end)
    return count + (end - start + 1)


if __name__ == '__main__':
    # print('hello world')
    a = np.random.randint(100, size=10)

    # a = [3, 1, 2, 4, 5, 6]
    # a = [39, 9, 47, 82, 27, 15, 27, 66, 90, 18]

    # print(a)
    # count = quick_sort(a, 0, len(a))
    # print(a)
    # print(count)

    # print(os.environ['HOME'])

    file_path = os.path.join(os.environ['HOME'], 'learning/algo1/_32387ba40b36359a38625cbb397eee65_QuickSort.txt')

    array = []
    with open(file_path) as f:
        for line in f: # read rest of lines
            array.append(int(line))
    # print(array[0])
    count = quick_sort(array, 0, len(array))
    print(count)
