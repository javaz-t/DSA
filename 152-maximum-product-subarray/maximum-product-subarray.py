class Solution:
    def maxProduct(self, nums ):
        res =max(nums)                
        curmin, curmax = 1, 1       

        for n in nums:
            if n==0:
                curmin,curmax=1,1
                continue
            tmp = curmax * n
            curmax = max(tmp, curmin*n, n)
            curmin = min(tmp, curmin*n, n)

            res = max(res, curmax)

        return res