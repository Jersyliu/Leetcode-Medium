class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sumA = sum(A)
        size = len(A)
        result = sum([x*n for x,n in enumerate(A)])
        maxR = result
        
        for i in xrange(1,size):
            result += sumA-size*A[size-i]
            maxR = max(maxR, result)
        
        return maxR