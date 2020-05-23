#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def mergeSort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return [arr[0], arr[1]] if arr[0] < arr[1] else [arr[1], arr[0]]
    l = len(arr)//2
    x = mergeSort(arr[:l])
    y = mergeSort(arr[l:])
    xIndex = 0
    yIndex = 0
    sortedarr = []
    while xIndex + yIndex < len(arr):
        if xIndex < len(x) and yIndex < len(y):
            if x[xIndex] <= y[yIndex]:
                sortedarr.append(x[xIndex])
                xIndex += 1
            else:
                sortedarr.append(y[yIndex])
                yIndex += 1
        elif xIndex >= len(x):
            sortedarr.extend(y[yIndex:])
            yIndex = len(y)
        else:
            sortedarr.extend(x[xIndex:])
            xIndex = len(x)
    return sortedarr
    
if __name__ == '__main__':
    
    arr = [1, 3, 5, 3, 4, 9, 9, 3, 5]
    
    print(mergeSort(arr))