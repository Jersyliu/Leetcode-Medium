class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le = len(nums)
        count = {}
        for i in nums:
            count[i] = 1
        for i in xrange(le+1):
            if i not in count:
                return i
            
        