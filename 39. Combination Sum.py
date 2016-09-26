class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == []:
            return []
        result = []
        path = []
        currAvailable = candidates
        self.findAll(target,result,path,currAvailable)
        return result
        
    def findAll(self,target,result,path,currAvailable):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for (i,key) in enumerate(currAvailable):
            if target < key:
                continue
            self.findAll(target-key,result,path+[key],currAvailable[i:])