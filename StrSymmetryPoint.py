# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def solution(S):
    # write your code in Python 3.6
    left = 0
    right = len(S)-1

    for i in range(math.ceil(len(S)/2)):
        if S[left] == S[right]:
            if right-left > 0:
                left = left+1
                right = right-1
            if left == right:
                return math.floor(len(S)/2)
    return -1


s = 'racecar'
print(solution(s))
