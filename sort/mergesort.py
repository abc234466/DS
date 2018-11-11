def mergeSort(lst):
    if len(lst) > 1:
        middle = len(lst) // 2
        leftlst = lst[:middle]
        rightlst = lst[middle:]
        mergeSort(leftlst)
        mergeSort(rightlst)

        leftIndex = rightIndex = mergeIndex = 0

        while leftIndex < len(leftlst) and rightIndex < len(rightlst):
            if leftlst[leftIndex] < rightlst[rightIndex]:
                lst[mergeIndex] = leftlst[leftIndex]
                leftIndex += 1
            elif leftlst[leftIndex] >= rightlst[rightIndex]:
                lst[mergeIndex] = rightlst[rightIndex]
                rightIndex += 1
            mergeIndex += 1

        while leftIndex < len(leftlst):
            lst[mergeIndex] = leftlst[leftIndex]
            leftIndex += 1
            mergeIndex += 1
        while rightIndex < len(rightlst):
            lst[mergeIndex] = rightlst[rightIndex]
            rightIndex += 1
            mergeIndex += 1
    return lst

a = [5,4,2,6,3,5,3]
print(mergeSort(a))
