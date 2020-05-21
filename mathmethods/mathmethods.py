

## Using integers
# def karatsuba(x, y):
#     k = 10 ** (max(len(str(x)), len(str(y)))//2)
#     if k == 1:
#         return x * y
#     a = x // k;
#     b = x % k;
#     c = y // k;
#     d = y % k;
#     ac = karatsuba(a, c)
#     bd = karatsuba(b, d)
#     bcPlusAd = karatsuba((a+b), (c+d)) - ac - bd
#     return ac * k * k + bcPlusAd * k + bd
#
#
# if __name__ == '__main__':
#     print(karatsuba(12341234, 12341234))


## using Strings
def karatsuba(x, y):
    l = (max(len(x), len(y)) // 2)
    if l == 0:
        return int(x) * int(y)
    k = 10 ** l
    a = x[:-l] if len(x[:-l]) > 0 else '0'
    b = x[-l:]
    c = y[:-l] if len(y[:-l]) > 0 else '0'
    d = y[-l:]
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    bcPlusAd = karatsuba(str(int(a)+int(b)), str(int(c)+int(d))) - ac - bd
    return ac * k * k + bcPlusAd * k + bd


if __name__ == '__main__':
    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627
    print(karatsuba(str(a), str(b)))
    print(a*b)

