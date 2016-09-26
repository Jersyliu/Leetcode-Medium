class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0,0,1]
        if n<3:
            return result[n]
            
        for i in xrange(3,n+1):
            if i%2 == 0:
                temp = 1+result[i//2]
                result.append(temp)
            if i%2 == 1:
                temp = 2+min(result[(i+1)//2],result[(i-1)//2])
                result.append(temp)
        return result[-1]
        
        
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n%2 == 0:
            return self.integerReplacement(n/2)+1
        return 1+min(self.integerReplacement(n+1),self.integerReplacement(n-1))