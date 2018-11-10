'''
# Insertion sort

Best Case: O(n) -> It means that data has already been sorted.
Average Case: O(n^2)
Wrost Case: O(n^2)
'''
lst = [2,8,4,6,8,7,10,9]

def insertionSort(lst):
    for i in range(1, len(lst)):
        value = lst[i]
        j = i - 1
        while (value < lst[j] and j >= 0):
            lst[j+1] = lst[j]
            j -= 1
        j += 1
        lst[j] = value
    return lst

print(insertionSort(lst))
            
