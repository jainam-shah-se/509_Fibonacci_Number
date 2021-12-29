class Solution:
    def tribonacci(self, n: int) -> int:
        tb = [0]*38
        tb[0] = 0
        tb[1] = 1
        tb[2] = 1
        for i in range(3, n+1):
            tb[i] = tb[i-1] + tb[i-2] + tb[i-3]
        return tb[n]
        