A = "ABEC"
s = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
counter = 0
add = 0
not_find_first = True
for i in A:
    if i not in s:
        if not_find_first:
            continue
        else:
            counter = counter+add
    else:
        if not_find_first:
            not_find_first = False
        add = add+1
        counter = counter+add
print(counter % 10003)
