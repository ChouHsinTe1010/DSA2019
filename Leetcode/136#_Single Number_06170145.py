class Solution(object):
    def singleNumber(self, nums):
        n=[]
        for k in nums:
            if k in n:
                n.remove(k)
            else:
                n.append(k)
        return n.pop()