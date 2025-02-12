import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

arr = [64, 25, 12, 22, 11]
print(heap_sort(arr))
