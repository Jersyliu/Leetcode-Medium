class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        
        dpPrev = []
        for i in matrix[0]:
            dpPrev.append(int(i))
        if sum(dpPrev) == 0:
            maxsque = 0
        else:
            maxsque = 1
        for i in xrange(1,row):
            #print dpPrev
            dpNow = [int(matrix[i][0])]
            for j in xrange(1,col):
                if int(matrix[i][j]) == 1:
                    temp = min(dpPrev[j-1],dpNow[j-1],dpPrev[j]) + 1
                    dpNow.append(temp)
                    if temp>maxsque:
                        maxsque = temp
                elif int(matrix[i][j]) == 0:
                    dpNow.append(0)
            dpPrev=dpNow
        #print dpPrev
        return maxsque**2