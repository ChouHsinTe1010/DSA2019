#!/usr/bin/env python
# coding: utf-8

# 參考資料來源：https://www.geeksforgeeks.org/merge-sort/
# 除了參考這個還有觀看影片了解邏輯。https://youtu.be/JSceec-wEyw
# 1首先我先透過畫結構圖來了解Merge Sort基本架構原則。
# 我初步想將num這串數分成兩部分，我要取的位置為第一個數跟最後一個數中間值。

# In[1]:


def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid=(low+high)/2
        left_num=num[:mid]
        right_num=num[mid:]
        
        


# 目前遇到一些瓶頸，不知道要怎麼繼續下去。發現python除法為//非/

# In[2]:


def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid=(low+high)//2
        left_num=num[:mid]
        right_num=num[mid:]
        
        mergesort(left_num)
        mergesort(right_num)


# 

# In[3]:


def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid=(low+high)//2
        left_num=num[:mid]
        right_num=num[mid:]
        
        mergesort(left_num)
        mergesort(right_num)
        
        index=a=b=0
        
    for index<left_num:
        num[k]=left_num[index]
        
        
    
        
        
       


# 

# In[2]:


def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid=(low+high)//2
        left_num=num[:mid]
        right_num=num[mid:]
        
        mergesort(left_num)
        mergesort(right_num)
        
        r=m=l=0#r為最右邊的第一值，l為最左邊的第一值
        
    while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
    
        if left_num[l]<= right_num[r]:
            num[m]=left_num[l]
            l=l+1


# 

# In[3]:


def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid=(low+high)//2
        left_num=num[:mid]
        right_num=num[mid:]
        
        mergesort(left_num)
        mergesort(right_num)
        
        r=m=l=0#r為最右邊的第一值，l為最左邊的第一值
        
    while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
    
        if left_num[l]< right_num[r]def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid=(low+high)//2
        left_num=num[:mid]
        right_num=num[mid:]
        
        mergesort(left_num)
        mergesort(right_num)
        
        r=m=l=0#r為最右邊的第一值，l為最左邊的第一值
        
    while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
    
        if right_num[r]< left_num[l]:
            num[m]=right[r]
            r=r+1
        else:
            num[m]=left_num[l]
            l=l+1
        m=m+1


# 

# In[4]:


def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid=(low+high)//2
        left_num=num[:mid]
        right_num=num[mid:]
        
        mergesort(left_num)
        mergesort(right_num)
        
        r=m=l=0#r為最右邊的第一值，l為最左邊的第一值
        
    while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
    
        if left_num[l]< right_num[r]def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid=(low+high)//2
        left_num=num[:mid]
        right_num=num[mid:]
        
        mergesort(left_num)
        mergesort(right_num)
        
        r=m=l=0#r為最右邊的第一值，l為最左邊的第一值
        
    while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
        if right_num[r]< left_num[l]:
            num[m]=right[r]
            r=r+1
        else:
            num[m]=left_num[l]
            l=l+1
        m=m+1
        
    while r< len(right_num):
        num[m]=right_num[r]
        
    while l <len(left_num):
        num[m]=left_num[l]
        


# 

# In[6]:





# In[7]:


num=[0,1,4,1,2]
mergesort(num)


# 

# 

# In[9]:


def mergesort(num):
    low=num[0]
    high=num[-1]
    if len(num)>1:
        mid1=len(low)+len(high)
        mid=mid1//2
        left_num=num[:mid]
        right_num=num[mid:]
        
        mergesort(left_num)
        mergesort(right_num)
        
        r=m=l=0 #r為最右邊的第一值，l為最左邊的第一值
        
    while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
        if right_num[r]< left_num[l]:
            num[m]=right[r]
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
num=[0,1,4,1,2]
mergesort(num)      


# 經過同學提醒，因為規定格式，所以前面必須統一用class來跑。
# 同時取中間數，不建議使用(high+low)//2這種語法，會減緩執行的速度。
# 只需要長度除2即可

# In[11]:


class Solution(objecjt):
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
            num[m]=right[r]
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
    


# 我的間隔好像是有問題的，重新排序。

# In[12]:


class Solution(objejct):
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
                    num[m]=right[r]
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
    


# In[13]:


class Solution(object):
    def mergesort(self,num):
        if len(num)>1:
            mid=len(num)
            left_num=num[:mid]
            right_num=num[mid:]
            Solution().mergesort(left_num)
            Solution().mergesort(right_num)
            r=m=l=0 #r為最右邊的第一值，l為最左邊的第一值
            
            while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
                if right_num[r]< left_num[l]:
                    num[m]=right[r]
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
    


# In[14]:


num=[0,3,1,5,1,2]
Solution().mergesort(num)
num


# 我發現我的mid忘記//2

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
                    num[m]=right[r]
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
    


# In[17]:


num=[0,3,1,5,1,2]
Solution().mergesort(num)
num


# 應該為right_num非right
# 
# 

# In[18]:


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
    


# In[19]:


num=[0,3,1,5,1,2]
Solution().mergesort(num)
num


# In[ ]:





# In[ ]:




