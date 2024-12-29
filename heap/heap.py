def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        return 1 + heapify(arr, n, largest)
    else:
        return 0


def build_heap(arr):
    n = len(arr)
    swaps = 0
    for i in range(n // 2 - 1, -1, -1):
        swaps += heapify(arr, n, i)
    return swaps


# Input
n = int(input())
sequence = list(map(int, input().split()))

# Output
result = build_heap(sequence)
print(result)