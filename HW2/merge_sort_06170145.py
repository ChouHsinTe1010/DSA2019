class Solution(object):
    def merge_sort(self,List):
        if len(List)>1:
            mid=len(List)//2
            left_num=List[:mid]
            right_num=List[mid:]
            Solution().merge_sort(left_num)
            Solution().merge_sort(right_num)
            r=m=l=0 #r為最右邊的第一值，l為最左邊的第一值
            
            while l <len(left_num) and r<len(right_num):#左的第幾位數在小於這串樹以前都不會停止。同理右邊也是。
                if right_num[r]< left_num[l]:
                    List[m]=right_num[r]
                    r=r+1
                else:
                    List[m]=left_num[l]
                    l=l+1
                m=m+1
            while r< len(right_num):
                List[m]=right_num[r]
                r=r+1
                m=m+1
            while l <len(left_num):
                List[m]=left_num[l]
                l=l+1
                m=m+1
            return List
