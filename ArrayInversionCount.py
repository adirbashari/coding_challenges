def solution(A):
    # write your code in Python 3.6
    # write your code in Python 3.6
    a = {}
    for i in A:
        if a.get(i) == None:
            a[i] = 1
        else:
            a[i] = a[i]+1
    for i in a:
        if a[i] == 1:
            return i
    return -1


print(solution([2]))
