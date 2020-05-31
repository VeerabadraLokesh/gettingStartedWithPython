#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt as sqrt

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


def getDistance(p1, p2):
    return sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )

def getClosestSplitPair(stripArr, delta):
    if len(stripArr) == 0:
        return None, None
    
    minDistance = delta
    minPair = None
    for i in range(len(stripArr) - 7):
        for j in range(i+1, i+8):
            d = getDistance(stripArr[i], stripArr[j])
            if d < minDistance:
                minPair = [stripArr[i], stripArr[j]]
                minDistance = d
    
    return minPair, minDistance
    pass


def getClosestPair(sortedX):
    
#    if (len(sortedX) == 2):
#        return sorted(sortedX , key=lambda k: [k[0], k[1]]), getDistance(sortedX[0], sortedX[1]), sorted(sortedX , key=lambda k: k[1])
    if (len(sortedX) == 3 or len(sortedX) == 2):
        minDistance = getDistance(sortedX[0], sortedX[1])
        minPair = [sortedX[0], sortedX[1]]
        for i in range(2):
            for j in range(i+1, 3):
                d = getDistance(sortedX[i], sortedX[j])
                if d < minDistance:
                    minDistance = d
                    minPair = [sortedX[i], sortedX[j]]
        return minPair, minDistance, sorted(sortedX , key=lambda k: k[1])
    
    l = len(sortedX)//2
    points1, d1, sortedY1 = getClosestPair(sortedX[:l])
    points2, d2, sortedY2 = getClosestPair(sortedX[l:])
    
    if d1 < 0 or d2 < 0:
        return points1 if d1 == 0 else points2, 0, None
    
    xmean = (sortedX[l-1][0] + sortedX[l][0])/2
    delta = min(d1, d2)
    
    index1 = 0
    index2 = 0
    sortedY = []
    stripArr = []
    for i in range(len(sortedX)):
        if index1 < len(sortedY1) and index2 < len(sortedY2):
            if sortedY1[index1][1] <= sortedY2[index2][1]:
                sortedY.append(sortedY1[index1])
                index1 += 1
            else:
                sortedY.append(sortedY2[index2])
                index2 += 1
        elif index1 >= len(sortedY1):
            sortedY.extend(sortedY2[index2:])
            break
        else:
            sortedY.extend(sortedY1[index1:])
            break
#    print(sortedY1, sortedY2,sortedY)
    for i in range(len(sortedY)):
        if sortedY[i][0] <= xmean + delta and sortedY[i][0] >= xmean - delta:
            stripArr.append(sortedY[i])
            
    pointsSplit, dSplit = getClosestSplitPair(stripArr, delta)
    
    if dSplit is not None and dSplit < min(d1, d2) and pointsSplit is not None:
        return pointsSplit, dSplit, sortedY
    elif d1 < d2:
        return points1, d1, sortedY
    else:
        return points2, d2, sortedY
    
    pass


def closestPair(arr):
    sortedX = sorted(arr, key=lambda p: p[0])
#    sortedY = sorted(arr, key=lambda p: p[1])
    return getClosestPair(sortedX)
    pass


if __name__ == '__main__':
    
    arr = [1, 3, 5, 7, 9, 2, 2, 4]
#    print(countInversion(arr, len(arr)))
    x = [[1, 2], [3, 4]]
    y = [[1, 0], [0, 1]]
    
    x = [
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            ]
    y = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            ]
    
#    print(matmulEqualSize(x, y))
    
    points = [[1, 2], [3, 4], [3, 3]]
    print(closestPair(points))