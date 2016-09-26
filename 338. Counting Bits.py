class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result=[0,1]
        if num<=1:
            return result[:num+1]
        for i in xrange(2,num+1):
            if (i+1)%4 == 0:
                result.append(result[i-1]+1)
                continue
            if i%2 == 0:
                if result[i//2] == 1:
                    result.append(1)
                    continue
                result.append(result[i//2])
            if i%2 == 1:
                result.append(result[i//2+1])
        return result