
# time complexity:  𝑂(N^2) 
# less number of swap compares with bubble sort

def SelectionSort(alist):
    numpass=len(alist)-1
    while numpass > 0:
        max_index = 0
        for i in range(numpass+1):
            if alist[max_index] < alist[i]:
                max_index = i
        
        alist[numpass], alist[max_index] = alist[max_index], alist[numpass]
        numpass += -1



alist=[54,26,93,17,77,31,44,55,20]
SelectionSort(alist)
print(alist)