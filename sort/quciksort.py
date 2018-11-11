'''
# Quick sort

Best Case: O(nlogn) 
Average Case: O(nlogn)
Wrost Case: O(n^2) -> The data has been sorted.
'''
lst = [3,8,4,6,2,1]

def quicksort(lst, front, end):
    print(front, end)
    if front >= end:
        return
    key = lst[front]
    left_pivot = front
    right_pivot = end
    while left_pivot < right_pivot:
        while left_pivot < right_pivot and lst[right_pivot] >= key:
            right_pivot = right_pivot - 1
        while left_pivot < right_pivot and lst[left_pivot] <= key:
            left_pivot = left_pivot + 1
        print(lst)
        if left_pivot < right_pivot:
            lst[left_pivot], lst[right_pivot] = lst[right_pivot], lst[left_pivot]
    lst[front], lst[left_pivot] = lst[left_pivot], lst[front]
    print(lst)
    quicksort(lst, front, left_pivot-1)
    quicksort(lst, right_pivot+1, end)
    return lst
        

    

print(quicksort(lst, 0, len(lst)-1))
            
