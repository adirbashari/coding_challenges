import math


def solve(A, B):
    if len(A) == 0:
        return 0
    elif A[0] > B:
        return 0

    size = len(A)
    index = math.floor((len(A)-1)/2)
    size = math.ceil(size/4)
    while size > 0:
        el = A[index]
        if el <= B:
            if index+size < len(A):
                index = index+size
        else:
            if index-size >= 0:
                index = index-size
        if size == 1:
            size = 0
        else:
            size = math.ceil(size/2)
    if A[index] > B:
        return index
    else:
        return index+1


A = [4, 4, 12, 12, 15, 19, 23, 24, 34, 42]
B = 48
print(solve(A, B))
