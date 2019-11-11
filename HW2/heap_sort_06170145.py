class Solution():
    def heapify(self,arr, x, i):
        parents= i 
        children_left=2*i+1
        children_right=2*i+2
        
        if  children_left<x and arr[parents]<arr[children_left]:
            parents=children_left
        if  children_right<x and  arr[parents]<arr[children_right]:
            parents=children_right
        if parents!= i:
            arr[parents],arr[i]=arr[i],arr[parents]
            Solution().heapify(arr,x,parents)
        
    def heap(self,arr,x):
        x=len(arr)
        index=int(x/2-1) 
        while index >=0:
            Solution().heapify(arr,x,index)
            index=index-1
    def heap_sort(self,arr):
        x=len(arr)
        Solution().heap(arr,x)
        while x>1:
            arr[0], arr[x - 1] = arr[x - 1], arr[0]
            x =x-1
            Solution().heapify(arr,x, 0)
        return arr
