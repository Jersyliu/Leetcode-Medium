class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= 0 :
            return 0
        result = [1]+[0]*target
        for i in xrange(1,target+1):
            for k in nums:
                if i >= k:
                    result[i] += result[i-k]
        return result[-1]
'''
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= 0 :
            return 0
        dictNum = {}
        result = [0]
        for i in nums:
            dictNum[i] = 1
        for k in range(1,target+1):
            if k in dictNum:
                temp = 1
            else:
                temp = 0
            for j in range(1,k):
                if j in dictNum:
                    temp += result[k-j]
            result.append(temp)
        return result[-1]
'''
a=Solution()
a.combinationSum4([1,2,3],4)    
            
        
        