class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            return  prices[1]-prices[0] if prices[1]-prices[0]>0 else 0
            
        profit = 0
        if prices[1]-prices[0] >= 0:
            min = prices[0]
        else:
            min = 0
        temp = 0
        for i in xrange(1,len(prices)-1):
            
            if temp != 0:
                pretrand = temp
                temp = 0 
            else:
                pretrand = prices[i]-prices[i-1]
            trand = prices[i+1]-prices[i]
            if trand == 0:
               temp = pretrand
               continue
            if trand > 0 and pretrand < 0:
                min = prices[i]
            if trand < 0 and pretrand > 0:
                profit += prices[i]-min
                min = 0
        if (prices[-1] > prices[-2]) or (prices[-1] == prices[-2] and temp > 0) :
            profit += prices[-1]-min
        return profit
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1]-prices[i]
        return profit