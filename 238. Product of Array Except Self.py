class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[1]*len(nums)
        #result2=[1]*len(nums)
        p=1
        for i in xrange(1,len(nums)):
            p=p*nums[i-1]
            result[i] = p
            #result1[i] = result1[i-1] * nums[i-1]
        #print result
        #print result1
        p=1    
        for i in xrange(len(nums)-2,-1,-1):
            p=p*nums[i+1]
            result[i] *= p
            #result2[i] = result2[i+1] * nums[i+1]
        #print result2
        
        return result