class Solution(object):
    def isAnagram(self, s, t):
        i=sorted(s)
        k=sorted(t)
        if i!=k:
            return False
        else:
            return True
       