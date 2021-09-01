def solve(A):
    stack = []

    for i in A:
        if i == "(":
            stack.append(i)
        elif stack == []:
            return 0
        else:
            stack.pop()
    if stack != []:
        return 0
    else:
        return 1


print(solve(")"))
