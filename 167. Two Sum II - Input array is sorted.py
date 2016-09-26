class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target < numbers[0]:
            return [0,0]
        numdict={}
        for i in xrange(len(numbers)):
            if numbers[i] in numdict:
                numdict[numbers[i]].append(i)
            else:
                numdict[numbers[i]]=[i]
        for i in xrange(len(numbers)):
            if numbers[i] > target:
                return [0,0]
            if target-numbers[i] in numdict:
                if i == numdict[target-numbers[i]][0]:
                    if len(numdict[target-numbers[i]]) > 1:
                        return [i+1,numdict[target-numbers[i]][1]+1]
                return [i+1,numdict[target-numbers[i]][0]+1]
        return [0,0]