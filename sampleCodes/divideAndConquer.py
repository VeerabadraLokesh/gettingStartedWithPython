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


def matSum(x, y, sign=1):
    sumMat = [[0] * len(x[0]) for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            sumMat[i][j] = (x[i][j] + sign * y[i][j])
    return sumMat

def matmulEqualSize(x, y):
    
    if len(x) == 1:
        return [[x[0][0] * y[0][0]]]
    
    l = len(x)//2
    
    a = [x[i][:l] for i in range(l)]
    b = [x[i][l:] for i in range(l)]
    c = [x[i][:l] for i in range(l, len(x))]
    d = [x[i][l:] for i in range(l, len(x))]
    
    e = [y[i][:l] for i in range(l)]
    f = [y[i][l:] for i in range(l)]
    g = [y[i][:l] for i in range(l, len(y))]
    h = [y[i][l:] for i in range(l, len(y))]
    
#    print(a, b, c, d, e, f, g, h)
    p1 = matmulEqualSize(a, matSum(f, h, sign=-1))
    p2 = matmulEqualSize(matSum(a, b), h)
    p3 = matmulEqualSize(matSum(c, d), e)
    
    p4 = matmulEqualSize(d, matSum(g, e, sign = -1))
    
    p5 = matmulEqualSize(matSum(a, d), matSum(e, h))
    p6 = matmulEqualSize(matSum(b, d, sign = -1), matSum(g, h))
    p7 = matmulEqualSize(matSum(a, c, sign = -1), matSum(e, f))
    
    mulMat = [[0] * len(x[0]) for i in range(len(x))]
    
    aebg = matSum(matSum(matSum(p5, p4), p2, sign=-1), p6)
    afbh = matSum(p1, p2)
    cedg = matSum(p3, p4)
    cfdh = matSum(matSum(matSum(p1, p5), p3, sign=-1), p7, sign = -1)
    
    for i in range(l):
        for j in range(l):
            mulMat[i][j] = aebg[i][j]
    for i in range(l):
        for j in range(l, len(x)):
            mulMat[i][j] = afbh[i][j-l]
    for i in range(l, len(x)):
        for j in range(l):
            mulMat[i][j] = cedg[i-l][j]
    for i in range(l, len(x)):
        for j in range(l, len(x)):
            mulMat[i][j] = cfdh[i-l][j-l]
    
    return mulMat
    pass


if __name__ == '__main__':
    
    arr = [1, 3, 5, 7, 9, 2, 2, 4]
#    print(countInversion(arr, len(arr)))
    x = [[1, 2], [3, 4]]
    y = [[1, 0], [0, 1]]
    
    print(matmulEqualSize(x, y))
    
    