class Solution(object):
    def maxProfit(_self,prices):
        l,r =(0,1)
        profit =0
        while(r<len(prices)):
            if prices[r]>prices[l]:
                #profit
                profit=max(profit,prices[r]-prices[l])
                r+=1
            
            else:
                #loss
                l=r
                r+=1
        return profit 


        
        
        