class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        end = len(t)-1
        location = -1
        for i in s:
            #print "This is "+str(i)
            location = self.binarySearch(t,i,location+1,end)
            #print location
            if type(location) != int:
                return False
        return True
        
   
    def binarySearch(self,string,char,start,end):
        #print "this is "+string
        if start > end:
            return False

        middle = (start+end)//2
        #print "This is middle "+str(middle)
        
        preResult = self.binarySearch(string,char,start,middle-1)
        
        if type(preResult) == int:
            return preResult 
        
        if string[middle] == char:
            return middle
        
        return self.binarySearch(string,char,middle+1,end)
        