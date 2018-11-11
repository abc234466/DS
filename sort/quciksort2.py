'''
# Quick sort

Best Case: O(nlogn) 
Average Case: O(nlogn)
Wrost Case: O(n^2) -> The data has been sorted.

These method makes more sense.

想法:
找出所有小於pivot的數 再交換 end 及 i(索引值)，便能夠區分兩邊
'''

def quicksort(lst, front, end):
    if front > end:
        return
    pivot = lst[end]
    i = front - 1
    for j in range(front, end):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
            print(lst)
    i += 1
    lst[i], lst[end] = lst[end], lst[i]
    quicksort(lst, front, i - 1)
    quicksort(lst, i + 1, end)
    return lst

lst = [2,7,5,4,3]
print(quicksort(lst, 0, len(lst)-1))
