s = "Hello Worldff     ff   "
last_word_len = 0
stroke = True
for i in reversed(range(len(s))):
    if s[i] == " ":
        if stroke:
            continue
        else:
            break
    else:
        stroke = False
        last_word_len = last_word_len+1
print(last_word_len)
