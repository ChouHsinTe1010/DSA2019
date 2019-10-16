def quick_sort(data):
        smaller=[]
        bigger=[]
        pivot1=[]
        

        if len(data)<=1:
                return data
        else:
                pivot=data[0]      
                for i in data:
                        if i < pivot:
                                smaller.append(i)
                        elif i >pivot:
                                bigger.append(i)
                        else:
                                pivot1.append(i)
        smaller = quick_sort(smaller)
        bigger = quick_sort(bigger)
        return smaller+pivot1+bigger



