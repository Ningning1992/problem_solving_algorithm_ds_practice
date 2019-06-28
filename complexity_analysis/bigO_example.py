# Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list. O(n^2)
# The second function should be linear. O(n)

# function 1
def compare_number(num_list):
    min_num = num_list[0]
    
    for i in num_list:
        is_min = True
        for j in num_list:
            if i > j:
                is_min = False
        if is_min:
            min_num = i
    
    return min_num


# function 2
def find_min(num_list):
    min_num = num_list[0]
    for i in num_list:
        if i < min_num:
            min_num = i
    
    return min_num


if __name__ == "__main__":
    import time

    x = [5, 9, 7, 6, 4, 1, -2, 3]
    start1 = time.time()
    min1 = compare_number(x)
    end1 = time.time()
    print("the first function result is %d with time %8.7f"%(min1, end1-start1))

    start2 = time.time()
    min2 = find_min(x)
    end2 = time.time()
    print("the first function result is %d with time %8.7f"%(min2, end2-start2))

