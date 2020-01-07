def quick_sort(data):
        smaller=[]#比pivot1小的數，位於左側
        bigger=[]#比pivot1大的數，位於右側
        pivot1=[]#第二層以後的基準點
        

        if len(data)<=1:
                return data #當這個data裡面的數值總數小於1的時候，就直接回傳data
        else:
                pivot=data[0]#基準點選擇第一個數   
                for i in data:
                        if i < pivot:
                                smaller.append(i)#比pivot小的數加入smaller
                        elif i >pivot:
                                bigger.append(i)#比pivor的數加入bigger
                        else:
                                pivot1.append(i)#和pivot一樣大的數加入pivot1
        smaller = quick_sort(smaller)#後面的層數也要重複這個一次
        bigger = quick_sort(bigger)
        return smaller+pivot1+bigger



