class Solution(object):
    def arrangeCoins(self, n):
        k = 1
        c =0
        while n>=k:
            n=n-k
            k=k+1
            c=c+1
        return c