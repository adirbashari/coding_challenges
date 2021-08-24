A = 1
b = [[1], ]


def paskal():
    if A == 0:
        return []
    for i in range(A-1):
        c = []
        c.append(1)
        for j in range(1, len(b[i])):
            c.append(b[i][j-1]+b[i][j])
        c.append(1)
        b.append(c)
    print(b)
