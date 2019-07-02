def binarySearch(alist, item):
    first = 0
    end = len(alist)-1
    found = False

    while first <= end and not found:
        midpoint = (first+end)//2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] < item:
                first = midpoint+1
            else:
                end = midpoint - 1
    
    return found

if __name__ == "__main__":
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
    