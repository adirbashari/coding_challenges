A = [3, 4, 1, 4, 1]
a = [0] * (len(A))
for i in range(len(A)):
    a[A[i]-1] = a[A[i]-1]+1
    if a[A[i]-1] > 1:
        print(A[i])
