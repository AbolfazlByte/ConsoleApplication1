def missingNumber(array, n):
    base = []
    for i in range(1, n+1):
        base.append(i)
    for i in array:
        base.remove(i)
    return base[0]
        
print(missingNumber([1], 2))