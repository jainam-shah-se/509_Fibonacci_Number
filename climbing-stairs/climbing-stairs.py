class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0]*46
        a[2] = 2
        a[1] = 1
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2]
        return a[n]