class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        result = [(0,1)]
        for i in xrange(3,n):
            if result[i-3][0] != 0:
                result.append((result[i-3][0]-1,result[i-3][1]+1))
            else:
                result.append((result[i-3][0]+2,result[i-3][1]-1))
            
        return 2**result[-1][0] * 3**result[-1][1]
        