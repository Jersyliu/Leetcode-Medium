class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return self.kLength(n)
        result = 10
        for i in xrange(2,n+1):
            result += self.kLength(i)
        return result

    def kLength(self,k):
        if k == 0:
            return 1
        if k == 1:
            return 10
        result = 9
        for i in xrange(k-1):
            result *= (9-i)
            if result < 0:
                return 0
        return result