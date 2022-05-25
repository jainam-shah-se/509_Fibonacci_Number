import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        l = []
        ans = 0
        r = n
        while n:
            s = n % 10
            l.append(s)
            n = int (n / 10)
        s = sum(l)
        p = numpy.prod(l)
        return p - s
        