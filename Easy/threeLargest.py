import heapq

def findThreeLargestNumbers(array):
    heap = []
    for n in array:
        count = len(heap)
        if count == 3 and heap[0] < n:
            heapq.heappop(heap)
            heapq.heappush(heap, n)
        elif count < 3:
            heapq.heappush(heap, n)

    heap.sort()
    return heap

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
ans = findThreeLargestNumbers(array)
print(ans)
