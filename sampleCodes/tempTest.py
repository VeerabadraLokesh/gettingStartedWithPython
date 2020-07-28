# def find_pivot_index(arr):
#     # if arr[index] < arr[index-1] and arr[index] > arr[index+1]
#     #     and arr[index] < arr[0]:
#     #     return index
#     # elif (arr[index] > arr[0]):
#     #     return find_pivot_index(arr, (len(arr)+index)//2)
#     # else:
#     #     return find_pivot_index(arr, index//2)
#     start_index = 0
#     end_index = len(arr) - 1
#     index = len(arr)//2
#     i = 0
#     while True:
#         print(start_index, index, end_index)
#         if arr[index] < arr[index-1] and arr[index] < arr[index+1] \
#             and arr[index] < arr[0]:
#             break
#         elif (arr[index] >= arr[start_index]):
#             start_index = index
#             index = (index + end_index)//2
#         else:
#             end_index = index
#             index = (index + start_index)//2
#         if start_index == index:
#             index += 1
#             break
#         if end_index == index:
#             index -= 1
#             break
#     return index
#
#
# def binary_search(arr, s, e, x):
#     if s == e or s == e - 1:
#         if arr[s] == x:
#             return s
#         elif arr[e] == x:
#             return e
#         else:
#             return -1
#     index = (s + e) // 2
#     if arr[index] == x:
#         return index
#     else:
#         if arr[index] > x:
#             return binary_search(arr, s, index, x)
#         else:
#             return binary_search(arr, index, e, x)

def search(A, B):
    def find_pivot_index(arr):
        # if arr[index] < arr[index-1] and arr[index] > arr[index+1]
        #     and arr[index] < arr[0]:
        #     return index
        # elif (arr[index] > arr[0]):
        #     return find_pivot_index(arr, (len(arr)+index)//2)
        # else:
        #     return find_pivot_index(arr, index//2)
        start_index = 0
        end_index = len(arr) - 1
        index = len(arr) // 2
        i = 0
        while True:
            # print(start_index, index, end_index)
            if arr[index] < arr[index - 1] and arr[index] < arr[index + 1] \
                    and arr[index] < arr[0]:
                break
            elif (arr[index] >= arr[start_index]):
                start_index = index
                index = (index + end_index) // 2
            else:
                end_index = index
                index = (index + start_index) // 2
            if start_index == index:
                index += 1
                break
            if end_index == index:
                index -= 1
                break
        return index

    pivot_index = find_pivot_index(A)

    def binary_search(arr, s, e, x):
        if s == e or s == e - 1:
            if arr[s] == x:
                return s
            elif arr[e] == x:
                return e
            else:
                return -1
        index = (s + e) // 2
        if arr[index] == x:
            return index
        else:
            if arr[index] > x:
                return binary_search(arr, s, index, x)
            else:
                return binary_search(arr, index, e, x)
    # print(pivot_index)
    # print(binary_search(A, 0, pivot_index, B))
    # print(binary_search(A, pivot_index, len(A) - 1, B))
    return max(binary_search(A, 0, pivot_index, B), binary_search(A, pivot_index, len(A) - 1, B))


def findMedianSortedArrays(A, B):
    def find_median(arr):
        if len(arr) % 2 == 0:
            return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2
        else:
            return arr[len(arr) // 2]

    if len(A) == 0:
        return find_median(B)
    if len(B) == 0:
        return find_median(A)

    target_length = (len(A) + len(B)) // 2
    is_even_length = ((len(A) + len(B)) % 2 == 0)

    indexA = 0
    indexB = 0
    count = 0
    while (True):
        if A[indexA] > B[indexB]:
            indexB += (target_length - indexA) // 2
            indexB = min(indexB, len(B)-1)
        elif A[indexA] < B[indexB]:
            indexA += (target_length - indexB) // 2
            indexA = min(indexA, len(A)-1)
        else:
            indexA += 1
            indexB += 1

        # print(indexA, indexB, target_length)
        if is_even_length and indexA + indexB >= target_length - 1:
            break
        if not is_even_length and indexA + indexB >= target_length - 1:
            break
        count += 1
        if count > 20:
            break
    # print(A[indexA])
    # print(B[indexB])
    if is_even_length:
        # return (A[indexA] + B[indexB]) / 2
        if A[indexA] < B[indexB]:
            if A[indexA-1] < B[indexB]:
                return (A[indexA] + A[indexA-1]) / 2
            return (A[indexA] + B[indexB]) / 2
        else:
            if B[indexB-1] < A[indexA]:
                return (B[indexB] + B[indexB-1]) / 2
            return (A[indexA] + B[indexB]) / 2
    else:
        if A[indexA] < B[indexB]:
            return min(B[indexB], A[indexA+1])
        else:
            return min(B[indexB+1], A[indexA])


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 8, 1, 2, 3]
    # arr = [2, 5, 1]
    # print(find_pivot_index(arr))
    # print(binary_search(arr, 0, len(arr)-1, 4))
    # print(search(arr, 4))

    # A = [-50, -41, -40, -19, 5, 21, 28]
    # B = [-50, -21, -10]
    B = [-50, -41, -40, -19, 5, 21, 28]
    A = [-50, -21, -10]
    A = [-45, -26, 23]
    B = [-41, -39, -33, -23, 8, 33, 41, 43, 48]
    print(findMedianSortedArrays(A, B))
    c = sorted([*A, *B])
    print(c)