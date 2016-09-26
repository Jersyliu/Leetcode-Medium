class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        currLevel = 0
        path = ""
        self.findAllCombination(digits,dict,result,currLevel,path)
        return result
        
    def findAllCombination(self,digits,dict,result,currLevel,path):
        if currLevel == len(digits):
            result.append(path)
            return
        for i in dict[digits[currLevel]]:
            self.findAllCombination(digits,dict,result,currLevel+1,path+i)
        
        