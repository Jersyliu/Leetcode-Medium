class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        result = []
        path = []
        currAvailable = range(1,10)
        self.findAll(n,k,result,path,currAvailable)
        return result
        
    def findAll(self,n,k,result,path,currAvailable):
        if k == 0 and n == 0:
            result.append(path)
        end = len(currAvailable)-(k-1)
        for (i,key) in enumerate(currAvailable[:end]):
            if n < key:
                return
            self.findAll(n-key,k-1,result,path+[key],currAvailable[1+i:])
            