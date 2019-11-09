#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def mergesort(self,num):
        if len(num)>1:
            mid=len(num)//2
            left_num=num[:mid]
            right_num=num[mid:]
            Solution().mergesort(left_num)
            Solution().mergesort(right_num)
            r=m=l=0 #r為最右邊的第一值，l為最左邊的第一值
            
            while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
                if right_num[r]< left_num[l]:
                    num[m]=right_num[r]
                    r=r+1
                else:
                    num[m]=left_num[l]
                    l=l+1
                m=m+1
            while r< len(right_num):
                num[m]=right_num[r]
                r=r+1
                m=m+1
            while l <len(left_num):
                num[m]=left_num[l]
                l=l+1
                m=m+1
            return num
    

