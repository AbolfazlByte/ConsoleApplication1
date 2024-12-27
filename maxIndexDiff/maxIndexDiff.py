def maxIndexDiff(arr,n):
    maxIndex = 0
    for i in range(n):
        for j in range(n):
            if arr[i] <= arr[j] and j-i > maxIndex:
                maxIndex = j-i
    return maxIndex

print(maxIndexDiff([34, 8, 10, 3, 2, 80, 30, 33, 1], 9))

            # print("i:", i)
            # print("j:", j)
            # print("max:", maxIndex)