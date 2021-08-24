A = [-963, -894, 35, 40, 264, 805, 842, 890]
# A = [-7, -4, -2, 1, 6, 8]

B = []
left = 0
right = len(A)-1

for i in range(len(A)):
    if A[left] < 0:
        if abs(A[left]) > abs(A[right]):
            d = A[left]*A[left]
            B.append(d)
            left = left+1
        else:
            d = A[right]*A[right]
            B.append(d)
            right = right-1
    else:
        d = A[right]*A[right]
        B.append(d)
        right = right-1
B.reverse()
print(B)
