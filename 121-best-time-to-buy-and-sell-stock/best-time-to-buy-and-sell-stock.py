class Solution(object):
    def maxProfit(_self,prices):
        l,r =(0,1)
        profit =0
        while(r<len(prices)):
            if prices[r]>prices[l]:
                #profit
                profit=max(profit,prices[r]-prices[l])            
            else:
                #loss
                l=r
            #no matter waht need to mov e the right 
            r+=1
        return profit 


        
        
        