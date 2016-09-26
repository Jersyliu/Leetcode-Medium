class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0:
            return False
        result = [True]+[False]*len(s)
        for i in range(1,len(s)+1):
            for j in range(i):
                if (result[j] and (s[j:i] in wordDict)) == True:
                    result[i] = True
                    break
        return result[-1]
        