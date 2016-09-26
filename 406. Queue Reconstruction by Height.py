class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        result = []
        for i in people:
            if i[1] in dic:
                dic[i[1]].append(i)
            else:
                dic[i[1]] = [i]
        
        for k in xrange(len(people)):
            if k not in dic:
                continue
            for j in dic[k]:
                place = self.findPlace(j,result)
                result.insert(place, j)
        return result
        
    def findPlace(self,j,result):
        standard = j[1]
        now = 0
        place = 0
        for (i,key) in enumerate(result):
            if now == standard and j[0] < key[0]:
                break
            elif now == standard and j[0] < key[0]:
                place += 1
                continue
            if j[0] <= key[0]:
                place +=1
                now += 1
            else:
                place += 1
        return place
            
        
        
        
        
        
        
        
        
        
        
        