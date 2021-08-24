class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_sum = sum(A[0:B])
        last_sum = sum(A[0:B])
        length = len(A)
        for i in range(B):
            last_sum = last_sum-A[B-1-i]+A[length-1-i]
            if(last_sum > max_sum):
                max_sum = last_sum
        return max_sum
