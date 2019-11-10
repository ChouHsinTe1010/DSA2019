class solution():
    def heapify(arr, x, i):
        parents= i 
        children_left=2*i+1
        children_right=2*i+2
        
        if  arr[parents]<arr[children_left] and children_left<x:
            arr[parents],arr[children_left]=arr[children_left],arr[parents]
        if  arr[parents]<arr[children_right] and children_right<x:
            parents=children_right
        if parents!= i:
            arr[parents],arr[i]=arr[i],arr[parents]
            heapify(arr,x,parents)
    def heap_sort(arr):
        x=len(arr)
        heap(arr)
        while x > 1:
            arr[0], arr[x - 1] = arr[x - 1], arr[0]
            x =x-1
            heapify(arr,x, 0)
        return arr
    def heap(arr):
        x=len(arr)
        index=int(x/2-1) 
        while index >=0:
            heapify(arr,x,index)
            index=index-1
   