#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#def countSplitInv(arr, n):
    

def countInversion(arr, n):
    if n == 1 or n == 0:
        return arr, 0
    l = len(arr)//2
    x, n1 = countInversion(arr[:l], l)
    y, n2 = countInversion(arr[l:], len(arr[l:]))
    splitInversions = 0
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
                splitInversions += len(x) - xIndex
        elif xIndex >= len(x):
            sortedarr.extend(y[yIndex:])
            yIndex = len(y)
        else:
            sortedarr.extend(x[xIndex:])
            xIndex = len(x)
        
    return sortedarr, n1 + n2 + splitInversions
    pass



def matmul(a, b):
    
    pass


if __name__ == '__main__':
    
    arr = [1, 3, 5, 7, 9, 2, 2, 4]
    print(countInversion(arr, len(arr)))
    
    