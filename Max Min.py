A = [-2, 1, -4, 5, 3]
max = A[0]
min = A[0]
for i in A:
    if i < min:
        min = i
    if i > max:
        max = i

max(A)+min(A)
