def heapify(lst, lstLength, nodeIndex):
    largest = nodeIndex
    leftIndex = largest * 2 + 1
    rightIndex = largest * 2 + 2

    if leftIndex < lstLength and lst[largest] < lst[leftIndex]:
        largest = leftIndex
    if rightIndex < lstLength and lst[largest] < lst[rightIndex]:
        largest = rightIndex

    if largest != nodeIndex:
        lst[nodeIndex], lst[largest] = lst[largest], lst[nodeIndex]

        heapify(lst, lstLength, largest)
    print(lst)


def heapSort(lst):
    lstLength = len(lst)

    # Build a Maxheap
    # In order to do heapsort
    for i in range(lstLength//2, -1, -1):
        heapify(lst, lstLength, i)

    # Do Heapsort -> Destory the Maxheap
    # Reconstruct the Maxheap -> redo heapify again
    for i in range(lstLength-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

lst = [ 12, 11, 13, 5, 6, 7] 
heapSort(lst)

