class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        result = []
        path = []
        currAvailable = range(1,n+1)
        self.combination(k,result,path,currAvailable)
        return result
        
    def combination(self,k,result,path,currAvailable):
        if k == 0:
            result.append(path)
            return
        '''
        if k == 1:
            end = len(currAvailable)
        else:
            end = -(k-1)
        '''
        end = len(currAvailable)-(k-1)
        for (i,key) in enumerate(currAvailable[:end]):
            temp = path+[key]
            self.combination(k-1,result,temp,currAvailable[(1+i):])
    