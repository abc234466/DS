'''
The question we'll work through is the following: return a new sorted merged list from K sorted lists,
each with size N. Before we move on any further, you should take some time to think about the solution!

First, go through an example. This buys time, makes sure you understand the problem,
and lets you gain some intuition for the problem. For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].
'''

'''
使用 Python  heapq (priority queue) 的資料結構來實作，每一次的 pop 所需的時間複雜度是 O(logn), 若 k 個序列各自有 n 個排序好的值
則所需要花費的時間複雜度是 O(knlogn)
'''
import heapq

def mergeksort(lists):
    merge_list=[]

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        value, listIndex, eleIndex = heapq.heappop(heap)

        merge_list.append(value)

        if eleIndex + 1 < len(lists[listIndex]):
            heapq.heappush(heap, (lists[listIndex][eleIndex+1], listIndex, eleIndex + 1))
        print(heap)
    return merge_list

# TEST
lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
print(mergeksort(lists))
